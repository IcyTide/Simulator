from base import BaseSetting
from settings import skill_event_settings


class SkillEventInSetting(BaseSetting):
    event_id: int
    event_type: str

    odds: int
    event_mask_1: int
    event_mask_2: int

    skill_id: int
    skill_level: int

    skill_caster: str
    skill_target: str

    def __init__(self):
        setting_row = skill_event_settings[skill_event_settings['ID'] == self.event_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)


class SkillEventInPython(SkillEventInSetting):
    index: int = 0


class SkillEvent(SkillEventInPython):
    def __init__(self, event_id: int):
        self.event_id = event_id
        super().__init__()
