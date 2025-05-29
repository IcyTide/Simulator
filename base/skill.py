from dataclasses import dataclass
from typing import List, Optional

from base import BaseSetting
from base.script import AttributeEffect
from enums.skill import *
from settings import skill_settings


@dataclass
class SlowCheckBuff:
    check_type: BUFF_CHECK_TYPE
    buff_id: int
    stack_num: int
    stack_num_compare_flag: BUFF_COMPARE_FLAG
    level: int
    level_compare_flag: BUFF_COMPARE_FLAG


@dataclass
class CheckSelfLearntSkill:
    skill_id: int
    level: int
    level_compare_flag: SKILL_COMPARE_FLAG


@dataclass
class DelaySubSkill:
    delay: int
    skill_id: int
    skill_level: int


@dataclass
class BindBuff:
    buff_id: int
    buff_level: int


class BindBuffs(list):
    def bind(self, index, buff_id, buff_level):
        if len(self) < index:
            for i in range(len(self), index):
                self.append(None)
        self[index - 1] = BindBuff(buff_id, buff_level)


class CoolDowns:
    public_cooldown: int
    normal_cooldowns: List[Optional[int]]
    check_cooldowns: List[Optional[int]]

    def __init__(self):
        self.public_cooldown = 0
        self.normal_cooldowns = []
        self.check_cooldowns = []

    def set_public(self, cooldown_id):
        self.public_cooldown = cooldown_id

    def set_normal(self, index, cooldown_id):
        if len(self.normal_cooldowns) < index:
            for i in range(len(self.normal_cooldowns), index):
                self.normal_cooldowns.append(None)
        self.normal_cooldowns[index - 1] = cooldown_id

    def set_check(self, index, cooldown_id):
        if len(self.check_cooldowns) < index:
            for i in range(len(self.check_cooldowns), index):
                self.check_cooldowns.append(None)
        self.check_cooldowns[index - 1] = cooldown_id


class SkillInSetting(BaseSetting):
    _aliases = {
        "dwSkillID": "skill_id",
        "dwLevel": "skill_level"
    }

    index: int
    skill_id: int

    max_level: int
    kind_type: int

    mount_request_type: int
    mount_request_detail: int

    target_relation_none: int
    target_relation_self: int
    target_relation_enemy: int

    target_type_player: int
    target_type_npc: int

    skill_event_mask_1: int
    skill_event_mask_2: int

    recipe_type: int

    script_file: str

    def __init__(self):
        setting_row = skill_settings[skill_settings['SkillID'] == self.skill_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)



class SkillInScript(SkillInSetting):
    attribute_effects: List[AttributeEffect]
    slow_check_buffs: List[SlowCheckBuff]
    check_self_learnt_skills: List[CheckSelfLearntSkill]
    bind_buffs: BindBuffs[Optional[BindBuff]]
    cooldowns: CoolDowns
    delay_sub_skills: List[DelaySubSkill]

    def __init__(self):
        super().__init__()
        self.attribute_effects = []
        self.slow_check_buffs = []
        self.check_self_learnt_skills = []
        self.bind_buffs = BindBuffs()
        self.cooldowns = CoolDowns()
        self.delay_sub_skills = []

    def add_attribute(self, attribute_effect_mode, attribute_type, param_1, param_2):
        self.attribute_effects.append(AttributeEffect(attribute_effect_mode, attribute_type, param_1, param_2))

    def add_slow_check_self_buff(self, buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag):
        self.slow_check_buffs.append(SlowCheckBuff(
            BUFF_CHECK_TYPE.SELF, buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag
        ))

    def add_slow_check_dest_buff(self, buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag):
        self.slow_check_buffs.append(SlowCheckBuff(
            BUFF_CHECK_TYPE.DEST, buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag
        ))

    def add_slow_check_self_own_buff(self, buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag):
        self.slow_check_buffs.append(SlowCheckBuff(
            BUFF_CHECK_TYPE.SELF_OWN, buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag
        ))

    def add_slow_check_dest_own_buff(self, buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag):
        self.slow_check_buffs.append(SlowCheckBuff(
            BUFF_CHECK_TYPE.DEST_OWN, buff_id, stack_num, stack_num_compare_flag, level, level_compare_flag
        ))

    def add_check_self_learnt_skill(self, skill_id, level, level_compare_flag):
        self.check_self_learnt_skills.append(CheckSelfLearntSkill(skill_id, level, level_compare_flag))

    def bind_buff(self, index, buff_id, buff_level):
        self.bind_buffs.bind(index, buff_id, buff_level)

    def set_public_cool_down(self, cooldown_id):
        self.cooldowns.set_public(cooldown_id)

    def set_normal_cool_down(self, index, cooldown_id):
        self.cooldowns.set_normal(index, cooldown_id)

    def set_check_cool_down(self, index, cooldown_id):
        self.cooldowns.set_check(index, cooldown_id)

    def set_delay_sub_skill(self, delay, skill_id, skill_level):
        self.delay_sub_skills.append(DelaySubSkill(delay, skill_id, skill_level))


class Skill(SkillInScript):
    source_id: int

    def __init__(self, source_id, skill_id, skill_level):
        self.source_id = source_id
        self.skill_id = skill_id
        self.skill_level = skill_level
        super().__init__()
