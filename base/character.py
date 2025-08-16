from copy import deepcopy
from typing import List, Optional, Set

from base import BaseSetting
from base.attribute import Attribute
from base.buff import Buff
from base.cooldown import Cooldown
from base.damage import Damage
from base.scene import scene
from base.script import Effect, Script
from base.skill import CheckBuff, Skill
from base.skill_event import SkillEvent
from base.skill_move import SkillMove
from base.skill_recipe import SkillRecipe
from base.timer import Timer
from base.utils import arrange_interval
from enums.script import *
from tools.dataframe import DataFrame


class CharacterInSetting(BaseSetting):
    id: int
    level: int

    target: "Character"

    is_player: bool
    employer_id: int = 0
    formation_leader: bool = True

    left_interval: int = 0

    prepare_state: bool = False
    direct_cast_mask: int = 0

    next_buff_count: int = 0

    mount_id: int = 0
    move_state: MOVE_STATE = MOVE_STATE.ON_STAND
    silences: Set[int]
    immunities: Set[int]

    current_life: int = 0
    max_life: int = 0

    x: int = 0
    y: int = 0
    z: int = 0
    face_direction: int = 0
    battle_field_side: int = -1
    identity_visiable_id: int = 0
    bird_move: bool = False


class CharacterInScript(CharacterInSetting):

    def __init__(self, *args):
        super().__init__()
        self.attribute = Attribute()

        self.buff: Optional[Buff] = None
        self.skill: Optional[Skill] = None
        self.damage = None

        self.silences = set()
        self.immunities = set()

        self.timer_map = DataFrame(columns=["index", "frame", "func", "args"])
        self.buff_map = DataFrame(columns=[
            "index", "buff_id", "buff_level", "append_type", "source_id",
            "stack_num", "next_active_frame", "left_active_count"
        ])
        self.skill_map = DataFrame(columns=["skill_id", "skill_level"])
        self.cd_map = DataFrame(columns=["cooldown_id", "left_interval", "used_count"])
        self.skill_recipe_map = DataFrame(columns=[
            "recipe_id", "recipe_level", "skill_id", "skill_level", "skill_recipe_type"
        ])
        self.skill_event_map = DataFrame(columns=[
            "event_id", "event_type", "odds", "event_mask_1", "event_mask_2"
        ])

    # Useless func
    def play_sfx(self, *args):
        ...

    def turn_to_skill_target(self):
        ...

    def get_direction_skill_target(self):
        return 0, 0

    def is_in_morph(self):
        return False

    def get_scene(self):
        return scene

    def get_employer(self):
        if self.employer_id:
            return Script.get_player(self.employer_id)
        return None

    def copy_player_simple_fight_attr(self, player_id: int):
        player = Script.get_player(player_id)
        self.attribute = deepcopy(player.attribute)

    def get_kungfu_mount(self):
        return self.mount_id

    def get_actual_kungfu_mount_id(self):
        return self.mount_id

    def mount_kungfu(self, skill_id: int, skill_level: int):
        self.mount_id = skill_id

    def is_formation_leader(self):
        return self.formation_leader

    # Effect func
    def _apply_effect(
            self, effect: Effect, target: "CharacterInScript"
    ):
        effect_type = effect.attribute_type
        param_1, param_2 = effect.param_1, effect.param_2
        if effect_type == ATTRIBUTE_TYPE.USELESS:
            pass
        elif effect_type == ATTRIBUTE_TYPE.SILENCE:
            target.silences.add(int(param_1))
        elif effect_type == ATTRIBUTE_TYPE.IMMUNITY:
            target.immunities.add(int(param_1))
        elif effect_type == ATTRIBUTE_TYPE.SET_NEXT_BUFF_COUNT:
            target.next_buff_count = int(param_1)
        elif effect_type == ATTRIBUTE_TYPE.CALL_SUB_BUFF:
            buff = self.buff
            target.add_buff(self.id, self.level, int(param_1), int(param_2), count=self.next_buff_count)
            buff.sub_buffs.append(self.buff)
        elif effect_type == ATTRIBUTE_TYPE.DIRECT_CAST_MASK:
            target.direct_cast_mask = int(param_1)
        elif effect_type == ATTRIBUTE_TYPE.SET_TALENT_RECIPE:
            target.add_skill_recipe(int(param_1), int(param_2))
        elif effect_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
            target.add_skill_event(int(param_1))
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT:
            Script(param_1).apply(target.id, self.skill.source_id)
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT_SETUP:
            Script(param_1).apply_setup(target.id)
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT_BULLET_TO_DEST:
            Script(param_1).apply_bullet_to_dest(target.id, self.skill.source_id)
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT_BULLET_TO_DEST_AND_ROLLBACK:
            Script(param_1).apply_bullet_to_dest_and_rollback(target.id, self.skill.source_id)
        elif effect_type == ATTRIBUTE_TYPE.CALL_PHYSICS_DAMAGE:
            target.call_physical_damage(param_1, param_2, self.skill)
        elif effect_type == ATTRIBUTE_TYPE.CALL_SURPLUS_PHYSICS_DAMAGE:
            target.call_surplus_physical_damage(param_1, param_2, self.skill)
        elif (attribute := ATTRIBUTE_TYPE(effect_type).name.lower()) in dir(target.attribute):
            setattr(target.attribute, attribute, getattr(target.attribute, attribute) + (int(param_1) or int(param_2)))
        else:
            raise Exception(f"AttributeType Error: {ATTRIBUTE_TYPE(effect_type).name} not implement")

    def _unapply_effect(
            self, effect: Effect, target: "CharacterInScript"
    ):
        effect_type = effect.attribute_type
        param_1, param_2 = effect.param_1, effect.param_2
        if effect_type == ATTRIBUTE_TYPE.USELESS:
            pass
        elif effect_type == ATTRIBUTE_TYPE.SILENCE:
            self.silences.discard(int(param_1))
        elif effect_type == ATTRIBUTE_TYPE.IMMUNITY:
            self.immunities.discard(int(param_1))
        elif effect_type == ATTRIBUTE_TYPE.SET_NEXT_BUFF_COUNT:
            self.next_buff_count = 0
        elif effect_type == ATTRIBUTE_TYPE.CALL_SUB_BUFF:
            pass
        elif effect_type == ATTRIBUTE_TYPE.DIRECT_CAST_MASK:
            self.direct_cast_mask = 0
        elif effect_type == ATTRIBUTE_TYPE.SET_TALENT_RECIPE:
            self.del_skill_recipe(int(param_1), int(param_2))
        elif effect_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
            self.del_skill_event(int(param_1))
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT:
            Script(param_1).unapply(self.target.id)
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT_SETUP:
            Script(param_1).unapply_setup(self.id)
        elif effect_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT_BULLET_TO_DEST_AND_ROLLBACK:
            Script(param_1).unapply_bullet_to_dest_and_rollback(self.target.id, self.id)
        elif (attribute := ATTRIBUTE_TYPE(effect_type).name.lower()) in dir(target.attribute):
            setattr(target.attribute, attribute, getattr(target.attribute, attribute) - (int(param_1) or int(param_2)))
        else:
            raise Exception(f"ATTRIBUTE_TYPE error: {ATTRIBUTE_TYPE(effect_type).name} not implement")

    # Buff func

    def _add_buff(self, buff: Buff):
        self.buff = buff
        refresh_buff = buff
        if buffs := self.buff_map[self.buff_map.index == buff.index]:
            refresh_buff = buffs.first()
            self._del_buff(refresh_buff)
        if (buffs := self.buff_map[self.buff_map.append_type == buff.append_type]) and not buff.coexist:
            refresh_buff = buffs.first()
            self._del_buff(refresh_buff)
        if buff.count > 1:
            buff.next_active_frame = refresh_buff.next_active_frame
        for effect in buff.begin_effects:
            self._apply_effect(effect, self)
        self.buff_map.append(buff)
        if not buff.left_active_count:
            self._buff_end(buff)

    def _del_buff(self, buff: Buff):
        self.buff = buff
        for effect in buff.begin_effects:
            self._unapply_effect(effect, self)
        for sub_buff in buff.sub_buffs:
            self._del_buff(sub_buff)
        self.buff_map.remove(buff.index)

    def _buff_active(self, buff: Buff):
        self.buff = buff
        self.skill = buff.source_skill
        for effect in buff.active_effects:
            self._apply_effect(effect, self)
        self._settle_damage(buff.buff_name)
        buff.left_active_count -= 1
        buff.next_active_frame += buff.active_frame

    def _buff_end(self, buff: Buff):
        self.buff = buff
        for effect in buff.end_effects:
            self._apply_effect(effect, self)
        buff.script.on_remove(self.id, buff)
        for sub_buff in buff.sub_buffs:
            self._buff_end(sub_buff)
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

    # Cooldown func

    def _set_cooldown(self, cooldown_id: int):
        if not cooldown_id:
            return
        if cooldowns := self._get_cooldown(cooldown_id):
            cooldown = cooldowns.first()
        else:
            cooldown = Cooldown(cooldown_id)
            self.cd_map.append(cooldown)
        if not cooldown.left_interval:
            cooldown.left_interval = cooldown.get_interval(self.attribute.haste)
        cooldown.used_count += 1

    def _get_cooldown(self, cooldown_id: int):
        return self.cd_map[self.cd_map.cooldown_id == cooldown_id]

    def _cooldown_end(self, cooldown: Cooldown):
        if cooldown.max_over_draft_count:
            self.cd_map.remove(cooldown.index)
        else:
            cooldown.used_count -= 1
            if cooldown.used_count > 0:
                cooldown.left_interval += cooldown.get_interval(self.attribute.haste)
            else:
                self.cd_map.remove(cooldown.index)

    def _get_cooldown_left_count(self, cooldown_id: int):
        if cooldowns := self._get_cooldown(cooldown_id):
            cooldown = cooldowns.first()
        else:
            cooldown = Cooldown(cooldown_id)
        if cooldown.draft_count:
            return cooldown.max_over_draft_count - cooldown.draft_count
        return cooldown.max_count - cooldown.used_count

    # Skill Recipe func
    def _get_skill_recipe(self, recipe_id: int, recipe_level: int):
        skill_recipes = self.skill_recipe_map[self.skill_recipe_map.recipe_id == recipe_id]
        skill_recipes = skill_recipes[skill_recipes.recipe_level == recipe_level]
        return skill_recipes

    def _apply_recipe(self, skill: Skill):
        pass

    def _apply_all_recipe(self, skill: Skill):
        pass

    def _unapply_recipe(self, skill: Skill):
        pass

    def _unapply_all_recipe(self, skill: Skill):
        pass

    # Skill func
    def _get_skill(self, skill_id: int, skill_level: int):
        skill = Skill(self.id, skill_id, skill_level)
        self._apply_all_recipe(skill)
        for normal_cooldown, cooldown_add in zip(skill.normal_cooldowns, skill.cooldown_adds):
            if not normal_cooldown:
                continue
            if not self._get_cooldown(normal_cooldown):
                cooldown, cooldown.cooldown_add = Cooldown(normal_cooldown), cooldown_add
                self.cd_map.append(cooldown)
        self.skill_map.append(skill)
        return skill

    def _check_target(self, target_type: TARGET, target_id: int):
        if not target_id:
            return self.target
        if target_type == TARGET.PLAYER:
            self.target = Script.get_player(target_id)
        elif target_type == TARGET.NPC:
            self.target = Script.get_npc(target_id)
        return self.target

    def _check_state(self, skill: Skill):
        if self.prepare_state and not skill.ignore_prepare_state:
            return False
        return True

    def _check_cooldown(self, skill: Skill):
        if cooldown_id := skill.public_cooldown:
            if not self._get_cooldown_left_count(cooldown_id):
                return False
        for cooldown_id in skill.normal_cooldowns + skill.check_cooldowns:
            if not cooldown_id:
                continue
            if not self._get_cooldown_left_count(cooldown_id):
                return False
        return True

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

    def _set_normal_cooldown(self, skill: Skill):
        for cooldown_id in skill.normal_cooldowns:
            self._set_cooldown(cooldown_id)

    def _apply_skill_effects(self, skill: Skill):
        for effect in skill.self_rollback_effects:
            self._apply_effect(effect, self)
        for effect in skill.dest_rollback_effects:
            self._apply_effect(effect, self.target)
        for effect in skill.self_effects:
            self._apply_effect(effect, self)
        for effect in skill.dest_effects:
            self._apply_effect(effect, self.target)

    def _unapply_skill_effects(self, skill: Skill):
        for effect in skill.self_rollback_effects:
            self._unapply_effect(effect, self)
        for effect in skill.dest_rollback_effects:
            self._unapply_effect(effect, self.target)

    def _bullet_create(self, skill: Skill):
        self._apply_skill_effects(skill)
        skill.script.on_bullet_destroy(self.id, 1)
        self._unapply_skill_effects(skill)
        self.target._settle_damage(skill.skill_name)

    def _prepare_end(self, skill: Skill):
        self.prepare_state = False
        self._set_normal_cooldown(skill)

    def _channel_end(self, skill: Skill):
        self.prepare_state = False
        skill.script.on_channel_end(self, True)

    def _prepare_skill(self, skill: Skill, prepare_frames: int):
        if self.direct_cast_mask & skill.cast_mask:
            self._direct_skill(skill)
        else:
            self.prepare_state = True
            skill.timer_index.append(self.timer_map.append(Timer(prepare_frames, self._bullet_create, (skill,))))
            skill.timer_index.append(self.timer_map.append(Timer(prepare_frames, self._prepare_end, (skill,))))

    def _channel_skill(self, skill: Skill, channel_frame: int):
        self.prepare_state = True
        count = skill.get_channel_count(self.attribute.haste)
        for interval in arrange_interval(channel_frame, count):
            skill.timer_index.append(self.timer_map.append(Timer(interval, self._bullet_create, (skill,))))
        skill.timer_index.append(self.timer_map.append(Timer(channel_frame, self._channel_end, (skill,))))
        for i, interval in enumerate(arrange_interval(channel_frame, len(skill.delay_sub_skills))):
            skill.delay_sub_skills[i].interval = interval
        if skill.instant_channel:
            self._bullet_create(skill)
        self._set_normal_cooldown(skill)

    def _direct_skill(self, skill: Skill):
        self._set_normal_cooldown(skill)
        self._bullet_create(skill)

    def _settle_damage(self, damage_name: str):
        if self.damage:
            print(f"got damage from {damage_name}")
            self.damage = None
            self.attribute.coming_damage_coefficient = 0

    # Open func
    def cast_skill(self, skill_id: int, skill_level: int, target_type: TARGET = None, target_id: int = 0):
        self.skill = skill = self._get_skill(skill_id, skill_level)

        if not self._check_target(target_type, target_id):
            return False
        if not self._check_state(skill):
            return False
        if not self._check_all_buff(skill):
            return False
        if not self._check_cooldown(skill):
            return False
        if not skill.script.can_cast(self):
            return False

        self._set_cooldown(skill.public_cooldown)

        if prepare_frames := skill.get_prepare_frames(self.attribute.haste):
            self._prepare_skill(skill, prepare_frames)
        elif channel_frame := skill.get_channel_frame(self.attribute.haste):
            self._channel_skill(skill, channel_frame)
        else:
            self._direct_skill(skill)

        for sub_skill in skill.delay_sub_skills:
            skill.timer_index.append(self.timer_map.append(
                Timer(sub_skill.interval, self.cast_skill, (sub_skill.skill_id, sub_skill.skill_level,))
            ))

        return True

    def set_timer(self, frame: int, script_file: str, param_1, param_2):
        self.timer_map.append(Timer(frame, Script(script_file).on_timer, (self, param_1, param_2)))

    def stop(self):
        if self.prepare_state:
            for index in self.skill.timer_index:
                self.timer_map.remove(index)
            self.prepare_state = False

    def get_skill_level(self, skill_id: int):
        if skills := self.skill_map[self.skill_map.skill_id == skill_id]:
            return skills.first().skill_level
        return 0

    def learn_skill_level(self, skill_id: int, skill_level: int, _: int):
        if skills := self.skill_map[self.skill_map.skill_id == skill_id]:
            skill = skills.first()
            if skill.skill_level < skill_level:
                self.forget_skill(skill_id)
            else:
                return
        self.skill = skill = self._get_skill(skill_id, skill_level)
        skill.script.on_skill_level_up(skill, self)
        self._apply_skill_effects(skill)

    def forget_skill(self, skill_id: int):
        if skills := self.skill_map[self.skill_map.skill_id == skill_id]:
            self.skill = skill = skills.first()
            self._unapply_skill_effects(skill)
            self.skill_map.remove(skill.index)

    def add_skill_recipe(self, recipe_id: int, recipe_level: int):
        if not self._get_skill_recipe(recipe_id, recipe_level):
            skill_recipe = SkillRecipe(recipe_id, recipe_level)
            self.skill_recipe_map.append(skill_recipe)

    def skill_move(self, skill_move_id: int, _: bool):
        skill_move = SkillMove(skill_move_id)
        self.prepare_state = True
        self.skill.timer_index.append(self.timer_map.append(Timer(skill_move.column, self.stop)))

    def del_skill_recipe(self, recipe_id: int, recipe_level: int):
        if skill_recipes := self._get_skill_recipe(recipe_id, recipe_level):
            skill_recipe = skill_recipes.first()
            self.skill_recipe_map.remove(skill_recipe.index)

    def is_skill_recipe_active(self, recipe_id: int, recipe_level: int):
        return bool(self._get_skill_recipe(recipe_id, recipe_level))

    def add_skill_event(self, event_id):
        if not self.skill_event_map[self.skill_event_map.event_id == event_id]:
            self.skill_event_map.append(SkillEvent(event_id))

    def del_skill_event(self, event_id):
        if skill_events := self.skill_event_map[self.skill_event_map.event_id == event_id]:
            skill_event = skill_events.first()
            self.skill_event_map.remove(skill_event.index)

    def is_have_buff(self, buff_id: int, buff_level: int):
        return bool(self._get_buff(buff_id, buff_level))

    def is_have_buff_by_owner(self, buff_id: int, buff_level: int, owner_id: int):
        return bool(self._get_buff(buff_id, buff_level, owner_id))

    def get_buff_by_owner(self, buff_id: int, buff_level: int, owner_id: int):
        return self._get_buff(buff_id, buff_level, owner_id).first()

    def add_buff(
            self, source_id: int, source_level: int, buff_id: int, buff_level: int,
            count: int = 0, _: int = 0, stack_num: int = 0, index: int = 0):
        source = Script.get_player(source_id)
        buff = Buff(source_id, source_level, buff_id, buff_level, source.skill)
        buff.left_active_count = int(count or buff.count)
        buff.stack_num = int(stack_num or buff.stack_num)
        buff.index = -index
        buff.next_active_frame = buff.active_frame = buff.get_active_frame(self.attribute.haste)
        self._add_buff(buff)

    def del_buff(self, buff_id: int, buff_level: int):
        if buffs := self._get_buff(buff_id, buff_level):
            self._del_buff(buffs.first())

    def del_buff_by_index(self, index: int):
        buff = self.buff_map[index]
        self._del_buff(buff)

    def reset_cd(self, cooldown_id: int):
        if cooldowns := self._get_cooldown(cooldown_id):
            cooldown = cooldowns.first()
            self.cd_map.remove(cooldown.index)

    def modify_cool_down(self, cooldown_id: int, interval: int):
        if cooldowns := self._get_cooldown(cooldown_id):
            cooldown = cooldowns.first()
            cooldown.left_interval += interval
            if cooldown.left_interval <= 0:
                self._cooldown_end(cooldown)

    def add_cd_time(self, cooldown_id: int, interval: int):
        self.modify_cool_down(cooldown_id, interval)

    def get_skill_cd_interval(self, skill_id: int, skill_level: int, cooldown_id: int):
        if cooldowns := self._get_cooldown(cooldown_id):
            cooldown = cooldowns.first()
        else:
            cooldown = Cooldown(cooldown_id)
            skill = self._get_skill(skill_id, skill_level)
            if cooldown_id in skill.normal_cooldowns:
                cooldown.cooldown_add = skill.cooldown_adds[skill.normal_cooldowns.index(cooldown_id)]

        return cooldown.get_interval(self.attribute.haste)

    def get_over_draft_cool_down(self, cooldown_id: int):
        if cooldowns := self._get_cooldown(cooldown_id):
            cooldown = cooldowns.first()
        else:
            cooldown = Cooldown(cooldown_id)
        return cooldown.max_over_draft_count, cooldown.draft_count

    def set_over_draft_cool_down(self, cooldown_id: int, draft_count: int):
        if cooldowns := self._get_cooldown(cooldown_id):
            cooldown = cooldowns.first()
        else:
            cooldown = Cooldown(cooldown_id)
        cooldown.used_count = 0
        cooldown.draft_count = draft_count

    def add_coming_damage_coefficient(self, damage_coefficient: int):
        self.attribute.coming_damage_coefficient += damage_coefficient

    def call_physical_damage(self, damage_base, damage_rand, skill: Skill):
        if not self.damage:
            self.damage = Damage(skill)

    def call_surplus_physical_damage(self, damage_base, damage_rand, skill: Skill):
        if not self.damage:
            self.damage = Damage(skill)


class CharacterInPython(CharacterInScript):
    attribute: Attribute

    def __init__(self, *args):
        super().__init__(*args)

    def process(self, frame: int = 1):
        self.process_timer(frame)
        self.process_buff(frame)
        self.process_cooldown(frame)

    def process_timer(self, frame: int = 0):
        self.timer_map.frame -= frame
        process_rows = self.timer_map[self.timer_map.frame <= 0]
        for timer in process_rows:
            timer.execute()
            self.timer_map.remove(timer.index)

    def process_buff(self, frame: int = 0):
        self.buff_map.next_active_frame -= frame
        process_rows = self.buff_map[self.buff_map.next_active_frame <= 0]
        for buff in process_rows:
            self._buff_active(buff)
        process_rows = self.buff_map[self.buff_map.left_active_count <= 0]
        for buff in process_rows:
            self._buff_end(buff)

    def process_cooldown(self, frame: int = 0):
        self.cd_map.left_interval -= frame
        for cooldown in self.cd_map[self.cd_map.left_interval <= 0]:
            self._cooldown_end(cooldown)


class Character(CharacterInPython):
    def __init__(self, character_id: int, character_level: int):
        self.id = character_id
        self.level = character_level
        super().__init__()
