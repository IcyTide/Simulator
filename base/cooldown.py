from base import BaseSetting
from base.constant import FRAME_PER_SECOND
from base.utils import apply_haste
from settings import cooldown_settings


class CooldownInSetting(BaseSetting):
    _aliases = {
        "ID": "cooldown_id"
    }

    cooldown_id: int = 0

    cooldown_add: int = 0

    duration: int = 0
    min_duration: int = 0

    max_count: int = 0
    max_over_draft_count: int = 0
    can_accelerate: int = 0

    def __init__(self):
        setting_row = cooldown_settings[cooldown_settings['ID'] == self.cooldown_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)

    @property
    def interval(self):
        return int(self.duration * FRAME_PER_SECOND + self.cooldown_add)

    @property
    def min_interval(self):
        return int(self.min_duration * FRAME_PER_SECOND)


class CooldownInPython(CooldownInSetting):
    index: int = 0

    left_interval: int = 0
    used_count: int = 0
    draft_count: int = 0

    def get_interval(self, haste: float):
        if self.can_accelerate:
            return max(apply_haste(self.interval, haste), self.min_interval)
        return self.interval


class Cooldown(CooldownInPython):
    def __init__(self, cooldown_id):
        self.cooldown_id = cooldown_id
        super().__init__()
