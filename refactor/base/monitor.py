from dataclasses import dataclass


@dataclass
class Temp:
    a: int = 2

    def p(self, a=a):
        print(a)


Temp().p(4)