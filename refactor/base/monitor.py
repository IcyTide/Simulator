from dataclasses import dataclass, field
from broadcast_service import broadcast_service


@dataclass
class A:
    a: int = 2
    x: int = 0

    def __post_init__(self):
        broadcast_service.subscribe("x", self.update)

    def update(self, x):
        self.x = x


inst = A()
print(inst.x)
broadcast_service.broadcast("x", 4)
print(inst.x)