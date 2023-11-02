import random
from functools import cached_property, cache


# import gradio as gr


class C:
    def __init__(self):
        self.a = 3

    @property
    def p1(self):
        return self.a

    @p1.setter
    def p1(self, a):
        self.a = a
        delattr(self, "p3")

    @cached_property
    def p2(self):
        return self.p1 + random.random()

    @cached_property
    def p3(self):
        print(self.p2)
        return self.p2 + random.random()


c = C()

print(c.p3)
print(c.p3)
c.p1 += 3
print(c.p3)
print(c.p3)
