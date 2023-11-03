import random
from dataclasses import dataclass
from functools import cached_property, cache


# import gradio as gr


@dataclass
class P:
    MAP = {
        1: 2,
        2: 3
    }
    a: int = 1
    b: int = MAP[a]

    @property
    def p1(self):
        return self.a

    @p1.setter
    def p1(self, a):
        self.a = a
        delattr(self, "p2")

    @cached_property
    def p2(self):
        return self.p1 + random.random()

    @cached_property
    def p3(self):
        return self.p2 + random.random()


c = P(a=2)
print(c.p2)
print(c.p2)
c.p1 = 3
print(c.p2)
print(c.p2)
