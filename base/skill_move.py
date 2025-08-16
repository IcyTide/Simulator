from base import BaseSetting
from settings import skill_move_settings


class SkillMoveInSetting(BaseSetting):
    skill_move_id: int
    column: int

    def __init__(self):
        setting_row = skill_move_settings[skill_move_settings['SkillMoveID'] == self.skill_move_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)


class SkillMove(SkillMoveInSetting):
    def __init__(self, skill_move_id: int):
        self.skill_move_id = skill_move_id
        super().__init__()