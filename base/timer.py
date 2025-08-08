from dataclasses import dataclass
from typing import Callable, Optional, Union


@dataclass
class Timer:
    frame: int
    func: Callable
    args: Optional[tuple] = None

    index: int = 0

    def __post_init__(self):
        if not self.args:
            self.args = tuple()

    def execute(self):
        self.func(*self.args)
