from base import BaseSetting
from base.utils import apply_haste
from settings import cooldown_settings
from tools.regex import camel_to_snake


class CooldownInSetting(BaseSetting):
    _aliases = {
        "ID": "cooldown_id"
    }

    cooldown_id: int = 0

    duration: int = 0
    min_duration: int = 0

    max_count: int = 0
    max_over_draft_count: int = 0
    can_accelerate: int = 0

    def __init__(self):
        setting_row = cooldown_settings[cooldown_settings['ID'] == self.cooldown_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)


class CooldownInPython(CooldownInSetting):
    index: int

    left_duration: int
    used_count: int
    draft_count: int

    def get_duration(self, haste: float):
        if self.can_accelerate:
            return max(apply_haste(self.duration, haste), self.min_duration)
        return self.duration


class Cooldown(CooldownInPython):
    def __init__(self, cooldown_id):
        self.cooldown_id = cooldown_id
        super().__init__()
