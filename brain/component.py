# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Oliver Geer

from abc import ABC, abstractmethod
import weakref

class Component(ABC):
    """A component calls an on_init callback when it is constructed, and an on_del
    callback when it is deleted or garbage collected.

    Example:
    ```python
    from typing import Int
    from random import randint

    class MyComponent(Component):
        \"\"\"Produces the results of rolling dice and tossing coins, and when it has
        stopped being used prints debug logs of how many numbers it has produced.\"\"\"

        def on_init():
            self._num_dice = 0
            self._num_coins = 0

        def roll_die():
            self._num_dice += 1
            return randint(1, 6)

        def toss_coin():
            self._num_coins += 1
            return "HT"[randint(0, 1)]

        def on_del():
            print("Debug statistics for MyComponent:")
            print(f"\tDie rolls: {self._num_dice}")
            print(f"\tCoin tosses: {self._num_coins}")
    ```
    """


    @abstractmethod
    def on_init(self, *args, **kwargs) -> None:
        """Runs when a new instance of the task is created, for example `my_task = new MyTask(...)`."""
        pass

    @abstractmethod
    def on_del(self) -> None:
        """Runs when the task is deleted or garbage collected, for example `del my_task`."""
        pass


    def __init__(self, *args, **kwargs):
        """Initialise a task with parameters specific to the task"""
        print(f"Initialising {self}")

        self.on_init(*args, **kwargs)

        print(f"Initialised {self}")

        # Make __del__ be called on garbage collection as well as on explicit deletion of
        # this object
        self._finalizer = new weakref.finalize(self, self.__del__)

    def __del__(self):
        """Delete this task."""
        print(f"Deleting {self}")

        self.on_del(*args, **kwargs)

        print(f"Deleted {self}")

        pass

