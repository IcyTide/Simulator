from base.attribute import Attribute
from base.constant import BINARY_SCALE, FRAME_PER_SECOND


class CooldownInSetting:
    cooldown_id: int = 0
    duration: int = 0
    min_duration: int = 0
    max_duration: int = 0

    max_count: int = 0
    max_overdraft_count: int = 0
    can_accelerate: int = 0


class CooldownInScript(CooldownInSetting):
    attribute: Attribute

    left_active_frame: int = 0
    used_count: int = 0

    @property
    def active_frame(self):
        if not self.can_accelerate:
            return self.duration * FRAME_PER_SECOND
        active_frame = int(self.duration * FRAME_PER_SECOND * BINARY_SCALE / (BINARY_SCALE + self.attribute.haste))
        active_frame = min(active_frame, self.max_duration * FRAME_PER_SECOND)
        active_frame = max(active_frame, self.min_duration * FRAME_PER_SECOND)
        return active_frame


class Cooldown(CooldownInScript):
    def __init__(self, cooldown_id):
        self.cooldown_id = cooldown_id
