import asyncio
import serial
import logging
import json

from hardware.utils import parse_partial_json

logger = logging.getLogger(__name__)


class HardwareBridge:
    def __init__(self, port, baudrate):
        loop = asyncio.get_running_loop()
        if port is None:
            # TODO: detect arduino automatically
            pass
        self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=.1)
        self.serial_lock = asyncio.Lock()
        # Note: possible separate lock for ser.flush()?
        # self.flush_lock = asyncio.Lock()
        self.logger = logging.getLogger("HardwareBridge")
        self._read_buffer = ""
        self._read_data = []
        self._read_process_task = loop.create_task(self._read_process())

    async def start_read_process(self):
        if self._read_process_task is None:
            self._read_process_task = asyncio.get_running_loop().create_task(self._read_process())

    async def _read_process(self):
        self._read_buffer = ""
        while True:
            await asyncio.sleep(0.1)
            if self.ser.in_waiting:
                data = await self.read()
                self._read_buffer += data
                parsed_data, new_buffer = parse_partial_json(self._read_buffer)
                self._read_data.extend(parsed_data)
                self._read_buffer = new_buffer

    async def write(self, command):
        async with self.serial_lock:
            self.ser.write(command.encode(encoding='UTF-8'))
            self.ser.flush()

    async def read(self):
        async with self.serial_lock:
            return self.ser.readline().decode(encoding='UTF-8').strip()

    async def test(self):
        ...

    async def close(self):
        try:
            if self._read_process_task is not None:
                self._read_process_task.cancel()
                try:
                    await self._read_process_task
                except asyncio.CancelledError:
                    pass
        finally:
            async with self.serial_lock:
                self.ser.close()


class RobotArmBridge:
    def __init__(self, port='COM3', baudrate=115200):
        self.hardware_bridge = HardwareBridge(port=port, baudrate=baudrate)
        self.logger = logging.getLogger("RobotArmBridge")

    async def test_connection(self):
        self.logger.info("Testing bridge...")
        start_time = asyncio.get_event_loop().time()
        response = await self.test_command()
        end_time = asyncio.get_event_loop().time()
        self.logger.info(f"Received response: {response}")
        self.logger.info(f"Test succeeded, latency={end_time - start_time:.2f} seconds")

    async def test_command(self):
        await self.send_command({"test": True})
        response = await self.receive_response()
        assert response == {"test": True}

    async def send_command(self, command):
        # TODO: change to json.dump for streaming the data
        data = json.dumps(command)
        self.logger.info("> " + data)
        await self.hardware_bridge.write(data + "\n")

    async def receive_response(self, max_wait=0.1, poll_delay=0.01):
        if max_wait < 0:
            raise ValueError("max_wait must be non-negative")
        if poll_delay <= 0:
            raise ValueError("poll_delay must be positive")

        await self.hardware_bridge.start_read_process()
        self.logger.debug("Waiting for response...")
        loop = asyncio.get_running_loop()
        deadline = loop.time() + max_wait

        while not self.hardware_bridge._read_data:
            remaining = deadline - loop.time()
            if remaining <= 0:
                raise TimeoutError("Timed out waiting for a hardware response")
            await asyncio.sleep(min(poll_delay, remaining))

        response = self.hardware_bridge._read_data.pop(0)
        self.logger.info("\033[95mReply from Arduino:\033[0m")
        self.logger.info("< " + json.dumps(response))
        return response
        

    async def move_motor(self, motor_id, position):
        motor_key = f"motor_{motor_id}"
        match motor_id:
            case 0:
                factor = 30
            case 1:
                factor = 10
            case 2:
                factor = 50
            case 3:
                factor = 30
            case _:
                raise ValueError(f"Invalid motor_id: {motor_id}")
        await self.send_command({motor_key: {"position": position  * factor}})
