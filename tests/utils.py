from typing import Callable


class Call:
    def __init__(self, method: Callable, params: dict):
        self.method = method
        self.params = params


class CallStack:
    def __init__(self):
        self._stack = []

    def append(self, method: Callable, **kwargs):
        self._stack.append(Call(method=method, **kwargs))

    def call(self, number: int) -> Call:
        number -= 1
        return self._stack[number]
