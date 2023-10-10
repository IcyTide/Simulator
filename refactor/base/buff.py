from dataclasses import dataclass


@dataclass
class Buff:
    uid: str
    name: str
    suffix: str

    interval: int
    stack: int

    def add(self):
        pass

    def remove(self):
        pass

    def trigger(self):
        pass

    def refresh(self):
        pass

    def clear(self):
        pass
