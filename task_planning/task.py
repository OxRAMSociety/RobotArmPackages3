from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from task_planning.component import Component

CallReturnType = TypeVar('CallReturnType')

# TODO: Log nested level

class Task[CallReturnType](Component):
    """A task can be initialised with parameters, run asynchronously (which returns a
    result, maybe None), and torn down (to de-initialise its parameters).

    Example:
    ```python
    from typing import Int

    class MyTask(Task[ComponentResult]):
        \"\"\"Use my_component to input an integer and output the result of the component after doing something that integer number of times.\"\"\"
        # Format: Use <sub-tasks/components passed into on_init and torn down in on_del>
        #         to input <parameters to on_call> and output <return value of on_call>.

        def on_init(my_component: MyComponent):
            self._component = my_component

        def on_call(num_repeats) -> ComponentResult:
            for i in range(num_repeats):
                self._component.do_something()
            return self._component.get_result()

        def on_del():
            del self._component
    ```
    """


    @abstractmethod
    def on_call(self, *args, **kwargs) -> CallReturnType:
        """Runs when the task is called, for example `my_task(...)`. Returns a value of the generic type this task class uses."""
        pass

    async def __call__(self, *args, **kwargs) -> CallReturnType:
        """Run this task once, asynchronously."""
        print(f"Starting {self}")

        result = self.on_call(*args, **kwargs)

        print(f"Finished {self}")

        return result
