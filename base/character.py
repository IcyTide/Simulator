from typing import List, TYPE_CHECKING

from base import BaseSetting
from base.attribute import Attribute
from base.buff import Buff
from base.cooldown import Cooldown
from base.damage import Damage
from base.script import Effect, Script
from base.skill import CheckBuff, Skill
from base.timer import Timer
from base.utils import arrange_interval
from enums.script import *
from tools.dataframe import DataFrame


class CharacterInScript(BaseSetting):
    id: int
    level: int

    target: "Character"

    def __init__(self, *args):
        super().__init__()
        self.attribute = Attribute()

        self.skill = None
        self.damage = None

        self.buff_map = DataFrame(columns=[
            "index", "buff_id", "buff_level", "append_type", "source_id",
            "stack_num", "next_active_frame", "left_active_count"
        ])
        self.cd_map = DataFrame(columns=["cooldown_id", "left_duration", "used_count"])
        self.timer_map = DataFrame(columns=["index", "frame", "func", "args"])

    # Effect func
    def _apply_effect(
            self, effect: Effect, target: "CharacterInScript"
    ):
        effect_type = effect.attribute_type
        param_1, param_2 = effect.param_1, effect.param_2
        if effect_type == ATTRIBUTE_TYPE.USELESS:
            pass
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT:
            Script(param_1).apply(self.id, self.skill.source_id)
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT_SETUP:
            Script(param_1).apply_setup(self.id)
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT_BULLET_TO_DEST_AND_ROLLBACK:
            Script(param_1).apply_bullet_to_dest_and_rollback(self.target.id, self.id)
        elif effect_type == ATTRIBUTE_TYPE.CALL_PHYSICS_DAMAGE:
            target.call_physical_damage(param_1, param_2, self.skill)
        elif (attribute := ATTRIBUTE_TYPE(effect_type).name.lower()) in dir(target.attribute):
            setattr(target.attribute, attribute, getattr(target.attribute, attribute) + (param_1 or param_2))
        else:
            raise Exception(f"AttributeType Error: {ATTRIBUTE_TYPE(effect_type).name} not implement")

    def _unapply_effect(
            self, effect: Effect, target: "CharacterInScript"
    ):
        effect_type = effect.attribute_type
        param_1, param_2 = effect.param_1, effect.param_2
        if effect_type == ATTRIBUTE_TYPE.USELESS:
            pass
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT:
            Script(param_1).unapply(self.id)
        elif (attribute := ATTRIBUTE_TYPE(ATTRIBUTE_TYPE).name.lower()) in dir(target.attribute):
            setattr(target.attribute, attribute, getattr(target.attribute, attribute) - (param_1 or param_2))
        else:
            raise Exception(f"ATTRIBUTE_TYPE error: {ATTRIBUTE_TYPE(ATTRIBUTE_TYPE).name} not implement")

    # Buff func

    def _add_buff(self, buff: Buff):
        refresh_buff = buff
        if buffs := self.buff_map[self.buff_map.index == buff.index]:
            refresh_buff = buffs.first()
            self._del_buff(refresh_buff)
        if buffs := self.buff_map[self.buff_map.append_type == buff.append_type] and not buff.coexist:
            refresh_buff = buffs.first()
            self._del_buff(refresh_buff)
        if buff.count > 1:
            buff.next_active_frame = refresh_buff.next_active_frame
        for effect in buff.begin_effects:
            self._apply_effect(effect, self)
        self.buff_map.append(buff)

    def _del_buff(self, buff: Buff):
        for effect in buff.begin_effects:
            self._unapply_effect(effect, self)
        self.buff_map.remove(buff.index)

    def _buff_end(self, buff: Buff):
        for effect in buff.end_effects:
            self._apply_effect(effect, self)
        self._del_buff(buff)

    def _get_buff(self, buff_id: int = 0, buff_level: int = 0, source_id: int = 0):
        buffs = self.buff_map
        if buff_id:
            buffs = buffs[buffs.buff_id == buff_id]
        if buff_level:
            buffs = buffs[buffs.buff_level == buff_level]
        if source_id is not None:
            buffs = buffs[buffs.source_id == source_id]
        return buffs

    def _get_buff_by_level(self, buffs: DataFrame, buff_level, buff_level_flag):
        if buff_level_flag == BUFF_COMPARE_FLAG.EQUAL:
            if not buff_level:
                return buffs
            buffs = buffs[buffs.buff_level == buff_level]
        elif buff_level_flag == BUFF_COMPARE_FLAG.NOT_EQUAL:
            buffs = buffs[buffs.buff_level != buff_level]
        elif buff_level_flag == BUFF_COMPARE_FLAG.GREATER_EQUAL:
            buffs = buffs[buffs.buff_level >= buff_level]
        elif buff_level_flag == BUFF_COMPARE_FLAG.LESS_EQUAL:
            buffs = buffs[buffs.buff_level <= buff_level]
        elif buff_level_flag == BUFF_COMPARE_FLAG.GREATER:
            buffs = buffs[buffs.buff_level > buff_level]
        elif buff_level_flag == BUFF_COMPARE_FLAG.LESS:
            if buff_level == 1:
                return self._get_buff_by_level(buffs, 0, BUFF_COMPARE_FLAG.EQUAL)
            buffs = buffs[buffs.buff_level < buff_level]
        else:
            raise Exception("buff_level_flag error")
        return buffs

    def _get_buff_by_stack(self, buffs: DataFrame, stack_num, stack_num_flag):
        if stack_num_flag == BUFF_COMPARE_FLAG.EQUAL:
            if not stack_num and not buffs:
                return True
            buffs = buffs[buffs.stack_num == stack_num]
        elif stack_num_flag == BUFF_COMPARE_FLAG.NOT_EQUAL:
            buffs = buffs[buffs.stack_num != stack_num]
        elif stack_num_flag == BUFF_COMPARE_FLAG.GREATER_EQUAL:
            buffs = buffs[buffs.stack_num >= stack_num]
        elif stack_num_flag == BUFF_COMPARE_FLAG.LESS_EQUAL:
            buffs = buffs[buffs.stack_num <= stack_num]
        elif stack_num_flag == BUFF_COMPARE_FLAG.GREATER:
            buffs = buffs[buffs.stack_num > stack_num]
        elif stack_num_flag == BUFF_COMPARE_FLAG.LESS:
            if stack_num == 1:
                return self._get_buff_by_stack(buffs, 0, BUFF_COMPARE_FLAG.EQUAL)
            buffs = buffs[buffs.stack_num < stack_num]
        else:
            raise Exception("stack_num_flag error")
        return buffs

    def _check_buff(self, check_buffs: List[CheckBuff], source_id: int = 0):
        for check_buff in check_buffs:
            buffs = self._get_buff(buff_id=check_buff.buff_id, source_id=source_id)
            buffs = self._get_buff_by_level(buffs, check_buff.level, check_buff.level_compare_flag)
            buffs = self._get_buff_by_stack(buffs, check_buff.stack_num, check_buff.stack_num_compare_flag)
            if not buffs:
                return False
        return True

    def _check_all_buff(self, skill: Skill):
        if not self._check_buff(skill.check_self_own_buffs, self.id):
            return False
        if not self._check_buff(skill.check_dest_own_buffs, self.id):
            return False
        if not self._check_buff(skill.check_self_buffs, self.id):
            return False
        if not self._check_buff(skill.check_dest_buffs, self.id):
            return False
        return True

    # Cooldown func

    def _check_cooldown(self, skill: Skill):
        if cooldown_id := skill.public_cooldown:
            if not self._get_cooldown_left_count(cooldown_id):
                return False
        for cooldown_id in skill.normal_cooldowns:
            if not cooldown_id:
                continue
            if not self._get_cooldown_left_count(cooldown_id):
                return False
        return True

    def _set_cooldown(self, cooldown_id: int):
        if not cooldown_id:
            return
        self._get_cooldown(cooldown_id).used_count += 1

    def _get_cooldown(self, cooldown_id: int):
        if cooldowns := self.cd_map[self.cd_map.cooldown_id == cooldown_id]:
            return cooldowns.first()
        cooldown = Cooldown(cooldown_id)
        cooldown.left_duration = cooldown.get_duration(self.attribute.haste)
        cooldown.used_count = cooldown.draft_count = 0
        return cooldown

    def _cooldown_end(self, cooldown: Cooldown):
        if cooldown.max_over_draft_count:
            cooldown.used_count = cooldown.draft_count = 0
            self.cd_map.remove(cooldown.index)
        else:
            cooldown.used_count -= 1
            if cooldown.used_count:
                cooldown.left_duration += cooldown.get_duration(self.attribute.haste)
            else:
                self.cd_map.remove(cooldown.index)

    def _get_cooldown_left_count(self, cooldown_id: int):
        cooldown = self._get_cooldown(cooldown_id)
        return cooldown.max_count - cooldown.used_count

    def _cast_skill(self, skill: Skill):
        for normal_cooldown in skill.normal_cooldowns:
            self._set_cooldown(normal_cooldown)

        for effect in skill.self_rollback_effects:
            self._apply_effect(effect, self)
        for effect in skill.dest_rollback_effects:
            self._apply_effect(effect, self.target)
        for effect in skill.self_effects:
            self._apply_effect(effect, self)
        for effect in skill.dest_effects:
            self._apply_effect(effect, self.target)
        self._bullet_hit(skill)
        return True

    def _bullet_hit(self, skill: Skill):
        for effect in skill.self_rollback_effects:
            self._unapply_effect(effect, self)
        for effect in skill.dest_rollback_effects:
            self._unapply_effect(effect, self.target)
        skill.script.on_bullet_destroy(self.id, 1)
        self._settle_damage()
        self.process_timer()

    def _channel_end(self, skill: Skill):
        skill.script.on_channel_end(self, True)

    # Call Damage

    def _settle_damage(self):
        if self.damage:
            self.damage = None

    def call_physical_damage(self, damage_base, damage_rand, skill: Skill):
        if not self.damage:
            self.damage = Damage()

    def cast_skill(self, skill_id: int, skill_level: int):
        self.skill = skill = Skill(self.id, skill_id, skill_level)
        if not self._check_all_buff(skill):
            return False
        if not self._check_cooldown(skill):
            return False
        if not skill.script.can_cast(self):
            return False

        self._set_cooldown(skill.public_cooldown)

        if prepare_frames := skill.get_prepare_frames(self.attribute.haste):
            skill.timer_index.append(self.timer_map.append(Timer(prepare_frames, self._cast_skill, (skill,))))
        elif channel_frame := skill.get_channel_frame(self.attribute.haste):
            if skill.instant_channel:
                self._cast_skill(skill)
            count = skill.get_channel_count(self.attribute.haste)
            for interval in arrange_interval(channel_frame, count):
                skill.timer_index.append(self.timer_map.append(Timer(interval, self._cast_skill, (skill,))))
            for i, interval in enumerate(arrange_interval(channel_frame, len(skill.delay_sub_skills))):
                skill.delay_sub_skills[i].interval = interval
            skill.timer_index.append(self.timer_map.append(Timer(channel_frame, self._channel_end, (skill,))))
        else:
            self._cast_skill(skill)

        for sub_skill in skill.delay_sub_skills:
            skill.timer_index.append(
                self.timer_map.append(
                    Timer(sub_skill.interval, self.cast_skill, (sub_skill.skill_id, sub_skill.skill_level))
                )
            )

        return True

    def is_have_buff(self, buff_id: int, buff_level: int):
        return bool(self._get_buff(buff_id, buff_level))

    def add_buff(
            self, source_id: int, source_level: int, buff_id: int, buff_level: int,
            count: int = 0, _: int = 0, stack_num: int = 0, index: int = 0):
        buff = Buff(source_id, source_level, buff_id, buff_level, self.skill)
        if count:
            buff.left_active_count = count
        if stack_num:
            buff.stack_num = stack_num
        if index:
            buff.index = -index
        self._add_buff(buff)

    def del_buff(self, buff_id: int, buff_level: int):
        if buffs := self._get_buff(buff_id, buff_level):
            self.buff_map.remove(buffs.first()._index)

    def get_over_draft_cool_down(self, cooldown_id: int):
        cooldown = self._get_cooldown(cooldown_id)
        return cooldown.draft_count, cooldown.max_over_draft_count

    def add_over_draft_count(self, cooldown_id: int):
        cooldown = self._get_cooldown(cooldown_id)
        cooldown.used_count -= 1
        cooldown.draft_count += 1


class CharacterInPython(CharacterInScript):
    is_player: bool

    attribute: Attribute

    def __init__(self, *args):
        super().__init__(*args)

    def process(self, frame: int = 1):
        self.process_timer(frame)
        self.process_buff(frame)
        self.process_cooldown(frame)

    def process_timer(self, frame: int = 1):
        self.timer_map.frame -= frame
        process_rows = self.timer_map[self.timer_map.frame <= 0]
        for timer in process_rows:
            timer.execute()
            self.timer_map.remove(timer.index)

    def process_buff(self, frame: int = 1):
        self.buff_map.next_active_frame -= frame
        self.buff_map[self.buff_map.next_active_frame <= 0].left_active_count -= 1
        process_rows = self.buff_map[self.buff_map.left_active_count <= 0]
        for buff in process_rows:
            self._buff_end(buff)

    def process_cooldown(self, frame: int = 1):
        self.cd_map.left_duration -= frame
        for cooldown in self.cd_map[self.cd_map.left_duration <= 0]:
            self._cooldown_end(cooldown)


class Character(CharacterInPython):
    def __init__(self, character_id: int, character_level: int):
        self.id = character_id
        self.level = character_level
        super().__init__()
