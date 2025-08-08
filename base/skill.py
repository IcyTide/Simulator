from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from base import BaseSetting
from base.script import Effect, Script
from base.utils import apply_haste
from enums.script import *
from settings import skill_settings


@dataclass
class CheckBuff:
    buff_id: int
    stack_num: int
    stack_num_compare_flag: BUFF_COMPARE_FLAG
    level: int
    level_compare_flag: BUFF_COMPARE_FLAG


@dataclass
class SubSkill:
    interval: int
    skill_id: int
    skill_level: int


class SkillInSetting(BaseSetting):
    _aliases = {
        "dwSkillID": "skill_id",
        "dwLevel": "skill_level"
    }

    skill_id: int

    max_level: int
    kind_type: int

    skill_event_mask_1: int
    skill_event_mask_2: int

    recipe_type: int

    path: str
    script_file: str

    def __init__(self):
        setting_row = skill_settings[skill_settings['SkillID'] == self.skill_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)


class SkillInScript(SkillInSetting):
    self_rollback_effects: List[Effect]
    dest_rollback_effects: List[Effect]
    self_effects: List[Effect]
    dest_effects: List[Effect]

    check_self_own_buffs: List[CheckBuff]
    check_dest_own_buffs: List[CheckBuff]
    check_self_buffs: List[CheckBuff]
    check_dest_buffs: List[CheckBuff]

    public_cooldown: int = 0
    normal_cooldowns: List[Optional[int]]
    check_cooldowns: List[Optional[int]]

    delay_sub_skills: List[SubSkill]

    prepare_frames: int = 0
    min_prepare_frames: int = 0
    instant_channel: bool = False
    channel_interval: int = 0
    min_channel_interval: int = 0
    channel_frame: int = 0
    min_channel_frame: int = 0

    def __init__(self):
        super().__init__()
        self.self_rollback_effects = []
        self.dest_rollback_effects = []
        self.self_effects = []
        self.dest_effects = []

        self.check_self_own_buffs = []
        self.check_dest_own_buffs = []
        self.check_self_buffs = []
        self.check_dest_buffs = []

        self.normal_cooldowns = []

        self.delay_sub_skills = []

        self.script = Script(str(Path(self.path, self.script_file)))

    def add_attribute(
            self, attribute_effect_mode: ATTRIBUTE_EFFECT_MODE, attribute_type: ATTRIBUTE_TYPE, param_1, param_2
    ):
        if attribute_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_AND_ROLLBACK:
            self.self_rollback_effects.append(Effect(attribute_type, param_1, param_2))
        elif attribute_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_AND_ROLLBACK:
            self.dest_rollback_effects.append(Effect(attribute_type, param_1, param_2))
        elif attribute_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_NOT_ROLLBACK:
            self.self_effects.append(Effect(attribute_type, param_1, param_2))
        elif attribute_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_NOT_ROLLBACK:
            self.dest_effects.append(Effect(attribute_type, param_1, param_2))

    def add_slow_check_self_own_buff(
            self, buff_id: int,
            stack_num: int, stack_num_compare_flag: BUFF_COMPARE_FLAG,
            level: int, level_compare_flag: BUFF_COMPARE_FLAG
    ):
        self.check_self_own_buffs.append(CheckBuff(
            buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag
        ))

    def add_slow_check_dest_own_buff(
            self, buff_id: int,
            stack_num: int, stack_num_compare_flag: BUFF_COMPARE_FLAG,
            level: int, level_compare_flag: BUFF_COMPARE_FLAG
    ):
        self.check_dest_own_buffs.append(CheckBuff(
            buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag
        ))

    def add_slow_check_self_buff(
            self, buff_id: int,
            stack_num: int, stack_num_compare_flag: BUFF_COMPARE_FLAG,
            level: int, level_compare_flag: BUFF_COMPARE_FLAG
    ):
        self.check_self_buffs.append(CheckBuff(
            buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag
        ))

    def add_slow_check_dest_buff(
            self, buff_id: int,
            stack_num: int, stack_num_compare_flag: BUFF_COMPARE_FLAG,
            level: int, level_compare_flag: BUFF_COMPARE_FLAG
    ):
        self.check_dest_buffs.append(CheckBuff(
            buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag
        ))

    def set_public_cool_down(self, cooldown_id):
        self.public_cooldown = cooldown_id

    def set_normal_cool_down(self, index, cooldown_id):
        if len(self.normal_cooldowns) < index:
            for _ in range(len(self.normal_cooldowns), index):
                self.normal_cooldowns.append(None)
        self.normal_cooldowns[index - 1] = cooldown_id


class SkillInPython(SkillInScript):

    def __init__(self):
        super().__init__()
        self.timer_index = []

    def get_prepare_frames(self, haste: float):
        if not self.prepare_frames:
            return 0
        if 0 < self.min_prepare_frames < self.prepare_frames:
            return max(apply_haste(self.prepare_frames, haste), self.min_prepare_frames)
        return self.prepare_frames

    def get_channel_interval(self, haste: float):
        if not self.channel_interval:
            return 0
        if 0 < self.min_channel_interval < self.channel_interval:
            return max(apply_haste(self.channel_interval, haste), self.min_channel_interval)
        return self.channel_interval

    def get_channel_frame(self, haste: float):
        if not self.channel_frame:
            return 0
        if 0 < self.min_channel_frame < self.channel_frame:
            return max(apply_haste(self.channel_frame, haste), self.min_channel_frame)
        return self.channel_frame

    def get_channel_count(self, haste: float):
        channel_frame, channel_interval = self.get_channel_frame(haste), self.get_channel_interval(haste)
        return int(channel_frame / channel_interval)


class Skill(SkillInPython):
    index: int

    source_id: int

    def __init__(self, source_id, skill_id, skill_level):
        self.source_id = source_id
        self.skill_id = skill_id
        self.skill_level = skill_level
        super().__init__()
        self.script.get_skill_level_data(self)
