from itertools import accumulate

from base.constant import BINARY_SCALE


def apply_haste(base: int, haste: float = 0.):
    return int(base * BINARY_SCALE / (BINARY_SCALE + haste))


def arrange_interval(frames: int, count: int):
    if not count:
        return []
    quotient, remainder = divmod(frames, count)
    return accumulate([quotient + 1 if i < remainder else quotient for i in range(count)])
