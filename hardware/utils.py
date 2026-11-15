
import json
import serial


def parse_partial_json(buffer):
    decoder = json.JSONDecoder()
    parsed_data = []
    offset = 0

    while True:
        while offset < len(buffer) and buffer[offset].isspace():
            offset += 1

        if offset == len(buffer):
            return parsed_data, ""

        if buffer[offset] != "{":
            raise json.JSONDecodeError("Expected a JSON object", buffer, offset)

        try:
            data, end = decoder.raw_decode(buffer, offset)
        except json.JSONDecodeError:
            depth = 0
            in_string = False
            escaped = False

            for char in buffer[offset:]:
                if in_string:
                    if escaped:
                        escaped = False
                    elif char == "\\":
                        escaped = True
                    elif char == '"':
                        in_string = False
                elif char == '"':
                    in_string = True
                elif char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
                    if depth == 0:
                        raise

            return parsed_data, buffer[offset:]

        if not isinstance(data, dict):
            raise json.JSONDecodeError("Expected a JSON object", buffer, offset)

        parsed_data.append(data)
        offset = end

# Michael - detect arduino usb port (linux)
def get_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "ttyACM0" in p.description or "Arduino" in p.description:
            return p.device


