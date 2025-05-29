from base import BaseSetting
from settings import skill_event_settings as settings


class SkillEventInSetting(BaseSetting):
    index: int

    skill_event_id: int = 0

    odds: int = 0
    skill_id: int = 0
    skill_level: int = 0

    event_mask_1: int = 0
    event_mask_2: int = 0

    def __init__(self):
        setting_row = settings[settings['ID'] == self.skill_event_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)

class SkillEvent(SkillEventInSetting):
    def __init__(self, skill_event_id: int):
        self.skill_event_id = skill_event_id
        super().__init__()