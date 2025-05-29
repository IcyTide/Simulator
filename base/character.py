from copy import deepcopy
from typing import Dict, Optional, List

from base import BaseSetting
from base.attribute import Attribute
from base.buff import Buff
from base.cooldown import Cooldown
from base.damage import Damage
from base.skill_event import SkillEvent
from tools.dataframe import DataFrame
from base.script import Script, AttributeEffect
from base.skill import Skill
from base.skill_recipe import SkillRecipe
from enums.script import EXECUTE_TYPE, ATTRIBUTE_TYPE, ATTRIBUTE_EFFECT_MODE
from enums.skill import BUFF_CHECK_TYPE, BUFF_COMPARE_FLAG, SKILL_COMPARE_FLAG
from enums.skill_event import SKILL_EVENT_TYPE


class BaseCharacter(BaseSetting):
    _aliases = {
        "dwID": "character_id",
        "nLevel": "character_level"
    }


class CharacterWithMethod(BaseCharacter):
    character_id: int
    character_level: int

    mount_id: int
    kungfu_id: int

    is_fight: bool = False
    is_player: bool
    select_target: Optional[int]
    current_target: Optional[int]

    attribute: Attribute

    current_damage: Optional[Damage]
    current_skill: Optional[Skill]

    buff_map: DataFrame
    skill_map: DataFrame
    skill_recipe_map: DataFrame
    skill_event_map: DataFrame
    cooldown_map: Dict[int, Cooldown]

    def __init__(self, character_id: int, mount_id: int, script: Script):
        super().__init__()
        self.character_id = character_id
        self.character_level = 1
        self.mount_id = mount_id
        self.attribute = Attribute()
        self.current_target, self.select_target = None, None
        self.current_damage = None
        self.current_skill = None
        self.script = script
        self.script.add_character(self)

        self.buff_map = DataFrame(columns=["source_id", "buff_id", "buff_level", "stack_num"])
        self.skill_map = DataFrame(columns=["skill_id", "skill_level"])
        self.skill_recipe_map = DataFrame(columns=["recipe_id", "recipe_level"])
        self.skill_event_map = DataFrame(columns=["skill_event_id"])
        self.cooldown_map = {}

    def _apply_effect_to_target(
            self, attribute_effect: AttributeEffect, target: "CharacterWithMethod"
    ):
        attribute_type = attribute_effect.attribute_type
        param_1, param_2 = attribute_effect.param_1, attribute_effect.param_2
        if attribute_type == ATTRIBUTE_TYPE.ACTIVE_THREAT_COEFFICIENT:
            pass
        elif attribute_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT:
            self.script.load_script(param_1)
            self.script.execute(EXECUTE_TYPE.APPLY, target.character_id, self.character_id)
        elif attribute_type == ATTRIBUTE_TYPE.CAST_SKILL:
            self.script.set_timer(0, self.cast_skill, param_1, param_2, target.character_id)
        elif attribute_type == ATTRIBUTE_TYPE.CALL_BUFF:
            target.add_buff(self.character_id, self.character_level, int(param_1), int(param_2))
        elif attribute_type == ATTRIBUTE_TYPE.SET_TALENT_RECIPE:
            target._set_skill_recipe(param_1, param_2)
        elif attribute_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
            target._set_skill_event(param_1 or param_2)
        elif attribute_type == ATTRIBUTE_TYPE.SET_ADAPTIVE_SKILL_TYPE:
            target.attribute.adaptive_skill_type = param_1
        elif attribute_type == ATTRIBUTE_TYPE.KUNGFU_TYPE:
            target.attribute.kungfu_type = param_1
        elif attribute_type == ATTRIBUTE_TYPE.CALL_PHYSICS_DAMAGE:
            target.call_physical_damage(param_1, param_2, self.current_skill)
        elif attribute_type == ATTRIBUTE_TYPE.CALL_SOLAR_DAMAGE:
            target.call_solar_damage(param_1, param_2, self.current_skill)
        elif attribute_type == ATTRIBUTE_TYPE.CALL_LUNAR_DAMAGE:
            target.call_lunar_damage(param_1, param_2, self.current_skill)
        elif attribute_type == ATTRIBUTE_TYPE.CALL_NEUTRAL_DAMAGE:
            target.call_neutral_damage(param_1, param_2, self.current_skill)
        elif attribute_type == ATTRIBUTE_TYPE.CALL_POISON_DAMAGE:
            target.call_poison_damage(param_1, param_2, self.current_skill)
        elif (attribute := ATTRIBUTE_TYPE(attribute_type).name.lower()) in dir(target.attribute):
            setattr(target.attribute, attribute, getattr(target.attribute, attribute) + (param_1 or param_2))
        else:
            raise Exception(f"AttributeType Error: {ATTRIBUTE_TYPE(attribute_type).name} not implement")

    # Script Method
    def _unapply_effect_to_target(
            self, attribute_effect: AttributeEffect, target: "CharacterWithMethod"
    ):
        attribute_type = attribute_effect.attribute_type
        param_1, param_2 = attribute_effect.param_1, attribute_effect.param_2
        if attribute_type == ATTRIBUTE_TYPE.ACTIVE_THREAT_COEFFICIENT:
            pass
        elif attribute_type == ATTRIBUTE_TYPE.EXECUTE_SCRIPT:
            self.script.load_script(param_1)
            self.script.execute(EXECUTE_TYPE.UNAPPLY)
        elif attribute_type == ATTRIBUTE_TYPE.SET_TALENT_RECIPE:
            target._del_skill_recipe(param_1, param_2)
        elif attribute_type == ATTRIBUTE_TYPE.SKILL_EVENT_HANDLER:
            target._del_skill_event(param_1 or param_2)
        elif attribute_type == ATTRIBUTE_TYPE.SET_ADAPTIVE_SKILL_TYPE:
            pass
        elif attribute_type == ATTRIBUTE_TYPE.KUNGFU_TYPE:
            pass
        elif (attribute := ATTRIBUTE_TYPE(attribute_type).name.lower()) in dir(target.attribute):
            setattr(target.attribute, attribute, getattr(target.attribute, attribute) - (param_1 or param_2))
        else:
            raise Exception(f"attribute_type error: {ATTRIBUTE_TYPE(attribute_type).name} not implement")

    # Buff Method
    def is_have_buff(self, buff_id, buff_level):
        if self.get_buff(buff_id, buff_level):
            return True
        return False

    def is_have_buff_by_owner(self, buff_id, buff_level, source_id):
        if self.get_buff_by_owner(buff_id, buff_level, source_id):
            return True
        return False

    def _get_buff(self, buff_id: int = 0, buff_level: int = 0, source_id: int = 0):
        buffs = self.buff_map
        if buff_id:
            buffs = buffs[buffs.buff_id == buff_id]
        if buff_level:
            buffs = buffs[buffs.buff_level == buff_level]
        if source_id:
            buffs = buffs[buffs.source_id == source_id]
        return buffs

    def get_buff(self, buff_id: int, buff_level: int) -> Optional[Buff]:
        buffs = self._get_buff(buff_id, buff_level)
        if buffs:
            return buffs.first()
        return None

    def get_buff_by_owner(self, buff_id: int, buff_level: int, source_id) -> Optional[Buff]:
        buffs = self._get_buff(buff_id, buff_level, source_id)
        if buffs:
            return buffs[0]
        return None

    def get_buff_by_index(self, index):
        buffs = self.buff_map[index]
        return buffs

    @staticmethod
    def _get_buff_by_level(buffs: DataFrame, buff_level, buff_level_flag=BUFF_COMPARE_FLAG.EQUAL):
        if not buffs:
            return None
        if not buff_level:
            return buffs  # no filter
        if buff_level_flag == BUFF_COMPARE_FLAG.EQUAL:
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
            buffs = buffs[buffs.buff_level < buff_level]
        else:
            raise Exception("buff_level_flag error")
        return buffs

    @staticmethod
    def _get_buff_by_stack(buffs: DataFrame, stack_num, stack_num_flag):
        if not buffs:
            return None
        if not stack_num:
            return buffs  # no filter
        if stack_num_flag == BUFF_COMPARE_FLAG.EQUAL:
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
            buffs = buffs[buffs.stack_num < stack_num]
        else:
            raise Exception("stack_num_flag error")
        return buffs

    def add_buff(self, source_id, source_level, buff_id, buff_level, count=0, duration=0, stack_num=1):
        buff = Buff(source_id, source_level, buff_id, buff_level)
        self.buff_map.append(buff)
        if character := self.script.get_character_by_id(source_id):
            buff.attribute = deepcopy(character.attribute)
        buff.source_skill = self.current_skill

        # buff count
        buff.left_active_count = count or buff.count

        # buff interval
        if buff.exclude:
            buff.next_active_frame = buff.active_frame

        self.script.set_timer(buff.next_active_frame, self._buff_active, buff)

        # buff stack
        if buff.is_countable:
            if not buff.stack_num:
                self._buff_begin(buff)
            buff.stack_num = min(buff.max_stack_num, buff.stack_num + stack_num)
        elif buff.is_stackable:
            stack_num_add = min(stack_num, buff.max_stack_num - buff.stack_num)
            buff.stack_num += stack_num_add
            for _ in range(stack_num_add):
                self._buff_begin(buff)
        else:
            if not buff.stack_num:
                self._buff_begin(buff)
            buff.stack_num = 1

    def _del_buff(self, buff: Buff):
        if buff.stack_num > 1:
            buff.stack_num -= 1
        else:
            self._buff_end(buff)
            self.buff_map.remove(buff.indexindex)

    def del_buff(self, buff_id, buff_level):
        buff = self.get_buff(buff_id, buff_level)
        if not buff:
            return
        self._del_buff(buff)

    def del_buff_by_index(self, index):
        buff = self.get_buff_by_index(index)
        if not buff:
            return
        self._del_buff(buff)

    def del_multi_group_buff_by_id(self, buff_id):
        buffs = self._get_buff(buff_id)
        for buff in buffs:
            self._buff_end(buff)

    def _buff_begin(self, buff: Buff):
        for attribute_effect in buff.begin_attributes:
            self._apply_effect_to_target(attribute_effect, self)
        if self.script.load_script("skill", buff.script_file):
            self.script.execute(EXECUTE_TYPE.APPLY, self.character_id, buff.source_id)

    def _buff_active(self, buff: Buff):
        for attribute_effect in buff.active_attributes:
            self._apply_effect_to_target(attribute_effect, self)
        buff.left_active_count -= 1
        if not buff.left_active_count:
            self._buff_end(buff)

    def _buff_end(self, buff: Buff):
        for attribute_effect in buff.begin_attributes:
            self._unapply_effect_to_target(attribute_effect, self)
        for attribute_effect in buff.end_attributes:
            self._apply_effect_to_target(attribute_effect, self)
        if self.script.load_script("skill", buff.script_file):
            self.script.execute(EXECUTE_TYPE.ON_REMOVE, self.character_id, buff.source_id)
        self.buff_map.remove(buff.index)

    # Cooldown Method
    def _add_cooldown(self, cooldown_id):
        if cooldown_id not in self.cooldown_map:
            self.cooldown_map[cooldown_id] = Cooldown(cooldown_id)
        cooldown = self.cooldown_map[cooldown_id]
        cooldown.attribute = deepcopy(self.attribute)
        if not cooldown.used_count:
            cooldown.left_active_frame = cooldown.active_frame
        cooldown.used_count += 1

    def _get_available_count(self, cooldown_id):
        if cooldown_id not in self.cooldown_map:
            self.cooldown_map[cooldown_id] = Cooldown(cooldown_id)
        cooldown = self.cooldown_map[cooldown_id]
        max_count = cooldown.max_count or cooldown.max_overdraft_count
        return max_count - cooldown.used_count, cooldown.left_active_frame

    def get_overdraft_cooldown(self, cooldown_id):
        if cooldown_id not in self.cooldown_map:
            self.cooldown_map[cooldown_id] = Cooldown(cooldown_id)
        cooldown = self.cooldown_map[cooldown_id]
        return cooldown.max_overdraft_count, cooldown.used_count

    def modify_cooldown(self, cooldown_id, frame):
        if cooldown_id not in self.cooldown_map:
            self.cooldown_map[cooldown_id] = Cooldown(cooldown_id)
        cooldown = self.cooldown_map[cooldown_id]
        cooldown.left_active_frame += frame

        if cooldown.left_active_frame < 0:
            if cooldown.max_overdraft_count:
                cooldown.used_count = 0
            elif cooldown.used_count:
                cooldown.used_count -= 1
                cooldown.left_active_frame += cooldown.active_frame
            else:
                cooldown.left_active_frame = 0

    def reset_cd(self, cooldown_id):
        self.cooldown_map[cooldown_id] = Cooldown(cooldown_id)

    # Skill Event Method
    def _trigger_skill_event(self, skill: Skill, event_type: SKILL_EVENT_TYPE):
        pass

    def _get_skill_event(self, skill_event_id: int = 0):
        skill_events = self.skill_event_map
        if skill_event_id:
            skill_events = skill_events[skill_events.skill_event_id == skill_event_id]
        return skill_events

    def _set_skill_event(self, skill_event_id):
        skill_event = SkillEvent(skill_event_id)
        self.skill_event_map.append(skill_event)

    def _del_skill_event(self, skill_event_id):
        skill_events = self._get_skill_event(skill_event_id)
        if not skill_events:
            return
        skill_event = skill_events.first()
        self.skill_event_map.remove(skill_event.index)

    def _get_talent_recipe(self, recipe_id: int = 0, recipe_level: int = 0):
        skill_recipes = self.skill_recipe_map
        if recipe_id:
            skill_recipes = skill_recipes[skill_recipes.recipe_id == recipe_id]
        if recipe_level:
            skill_recipes = skill_recipes[skill_recipes.recipe_level == recipe_level]
        return skill_recipes

    def _set_skill_recipe(self, recipe_id, recipe_level):
        skill_recipe = SkillRecipe(recipe_id, recipe_level)
        self.skill_recipe_map.append(skill_recipe)

    def _del_skill_recipe(self, recipe_id, recipe_level):
        skill_recipes = self._get_talent_recipe(recipe_id, recipe_level)
        if not skill_recipes:
            return
        skill_recipe = skill_recipes.first()
        self.skill_recipe_map.remove(skill_recipe.index)

    def is_skill_recipe_active(self, recipe_id, recipe_level):
        skill_recipes = self._get_talent_recipe(recipe_id, recipe_level)
        if not skill_recipes:
            return False
        return True

    def _apply_recipe(self, skill: Skill):
        for recipe in self.skill_recipe_map:
            if recipe.skill_id != skill.skill_id:
                continue
            if not recipe.skill_recipe_type & skill.recipe_type:
                continue
            recipe.execute(EXECUTE_TYPE.GET_SKILL_RECIPE_DATA, skill)

    # Skill Method
    def cast_skill(self, skill_id, skill_level, *args):
        if len(args) == 2:
            target_type, target_id = args
        elif len(args) == 1:
            target_id = args[0]
        else:
            target_id = self.select_target

        self.current_skill = skill = Skill(self.character_id, skill_id, skill_level)
        target = self.script.get_character_by_id(target_id)
        self._cast_skill(skill, target)

    def cast_skill_x_y_z(self, skill_id, skill_level, x, y, z):
        self.cast_skill(skill_id, skill_level)
        self.current_target = None

    def _get_skill(self, skill_id: int = 0, skill_level: int = 0):
        skills = self.skill_map
        if skill_id:
            skills = skills[skills.skill_id == skill_id]
        if skill_level:
            skills = skills[skills.skill_level == skill_level]
        return skills

    def get_skill_level(self, skill_id):
        if skill_id in self.skill_map:
            return self.skill_map[skill_id].skill_level
        return 0

    def learn_skill_level(self, skill_id, skill_level):
        self.forget_skill(skill_id)
        skill = Skill(self.character_id, skill_id, skill_level)
        self.skill_map.append(skill)
        self._learn_skill(skill)

    def forget_skill(self, skill_id):
        skills = self._get_skill(skill_id)
        if not skills:
            return
        skill = skills.first()
        self.skill_map.remove(skill.index)
        self._forget_skill(skill)

    # Casting Skill
    def _check_mount_request(self, skill: Skill):
        if skill.mount_request_type and skill.mount_request_type != self.mount_id:
            return False
        if skill.mount_request_detail and skill.mount_request_detail != self.kungfu_id:
            return False
        return True

    def _check_target(self, skill: Skill, target: Optional[BaseCharacter] = None):
        if skill.target_relation_self:
            target = self
        if target is not None:
            if not skill.target_type_player and target.is_player:
                return None
            if not skill.target_type_npc and not target.is_player:
                return None
        return target

    def _check_buff(self, skill: Skill, target: BaseCharacter):
        for skill_check_buff in skill.slow_check_buffs:
            if skill_check_buff.check_type == BUFF_CHECK_TYPE.SELF:
                check_character = self
            elif skill_check_buff.check_type == BUFF_CHECK_TYPE.DEST:
                check_character = target
            elif skill_check_buff.check_type == BUFF_CHECK_TYPE.SELF_OWN:
                check_character = self
            elif skill_check_buff.check_type == BUFF_CHECK_TYPE.DEST_OWN:
                check_character = target
            else:
                raise Exception("skill_check_buff.check_type error")

            source_id, buff_id = check_character.character_id, skill_check_buff.buff_id
            buffs = self.buff_map[self.buff_map.source_id == source_id & self.buff_map.buff_id == buff_id]
            buff_level, buff_level_flag = skill_check_buff.level, skill_check_buff.level_compare_flag
            buffs = self._get_buff_by_level(buffs, buff_level, buff_level_flag)
            stack_num, stack_num_flag = skill_check_buff.stack_num, skill_check_buff.stack_num_compare_flag
            buffs = self._get_buff_by_stack(buffs, stack_num, stack_num_flag)

            if not buffs:
                return False
        return True

    def _check_learnt_skill(self, skill: Skill):
        for check_self_learnt_skill in skill.check_self_learnt_skills:
            skill_id = check_self_learnt_skill.skill_id
            learn_level = self.get_skill_level(skill_id)
            level, level_flag = check_self_learnt_skill.level, check_self_learnt_skill.level_compare_flag
            if level_flag == SKILL_COMPARE_FLAG.EQUAL:
                if learn_level != level:
                    return False
            elif level_flag == SKILL_COMPARE_FLAG.NOT_EQUAL:
                if learn_level == level:
                    return False
            elif level_flag == SKILL_COMPARE_FLAG.GREATER_EQUAL:
                if learn_level < level:
                    return False
            elif level_flag == SKILL_COMPARE_FLAG.LESS_EQUAL:
                if learn_level > level:
                    return False
            elif level_flag == SKILL_COMPARE_FLAG.GREATER:
                if learn_level <= level:
                    return False
            elif level_flag == SKILL_COMPARE_FLAG.LESS:
                if learn_level >= level:
                    return False
            else:
                raise Exception("check_self_learnt_skill.level_compare_flag error")
        return True

    def _check_cooldown(self, skill: Skill):
        if public_cooldown := skill.cooldowns.public_cooldown:
            available_count = self._get_available_count(public_cooldown)
            if not available_count:
                return False
        for normal_cooldown in skill.cooldowns.normal_cooldowns:
            if not normal_cooldown:
                continue
            available_count = self._get_available_count(normal_cooldown)
            if not available_count:
                return False
        for check_cooldown in skill.cooldowns.check_cooldowns:
            if not check_cooldown:
                continue
            available_count = self._get_available_count(check_cooldown)
            if not available_count:
                return False
        return True

    def _set_cooldown(self, skill: Skill):
        if public_cooldown := skill.cooldowns.public_cooldown:
            self._add_cooldown(public_cooldown)
        for normal_cooldown in skill.cooldowns.normal_cooldowns:
            if not normal_cooldown:
                continue
            self._add_cooldown(normal_cooldown)
        for check_cooldown in skill.cooldowns.check_cooldowns:
            if not check_cooldown:
                continue
            self._add_cooldown(check_cooldown)

    def _set_delay_skills(self, skill: Skill):
        pass

    def _set_bind_buff(self, skill: Skill, target: "CharacterWithMethod"):
        for bind_buff in skill.bind_buffs:
            if not bind_buff:
                continue
            buff_id, buff_level = bind_buff.buff_id, bind_buff.buff_level
            target.add_buff(self.character_id, self.character_id, buff_id, buff_level)

    def _apply_effect(self, skill: Skill, target: "CharacterWithMethod"):
        for attribute_effect in skill.attribute_effects:
            if attribute_effect.attribute_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_AND_ROLLBACK:
                self._apply_effect_to_target(attribute_effect, self)
            elif attribute_effect.attribute_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_AND_ROLLBACK:
                self._apply_effect_to_target(attribute_effect, target)
        for attribute_effect in skill.attribute_effects:
            if attribute_effect.attribute_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_NOT_ROLLBACK:
                self._apply_effect_to_target(attribute_effect, self)
            elif attribute_effect.attribute_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_NOT_ROLLBACK:
                self._apply_effect_to_target(attribute_effect, target)

    def _unapply_effect(self, skill: Skill, target: "CharacterWithMethod"):
        for attribute_effect in skill.attribute_effects:
            if attribute_effect.attribute_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_SELF_AND_ROLLBACK:
                self._unapply_effect_to_target(attribute_effect, self)
            elif attribute_effect.attribute_effect_mode == ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_AND_ROLLBACK:
                self._unapply_effect_to_target(attribute_effect, target)

    def _learn_skill(self, skill: Skill):
        self.script.load_script("skill", skill.script_file)
        self.script.execute(EXECUTE_TYPE.GET_SKILL_LEVEL_DATA, skill)
        self._apply_effect(skill, self)

    def _forget_skill(self, skill: Skill):
        self.script.load_script("skill", skill.script_file)
        self.script.execute(EXECUTE_TYPE.GET_SKILL_LEVEL_DATA, skill)
        self._unapply_effect(skill, self)

    def _cast_skill(self, skill: Skill, target: Optional[BaseCharacter] = None):
        # checking in setting
        if not self._check_mount_request(skill):
            return False
        target = self._check_target(skill, target)
        if not target:
            return False
        # checking in script
        self.script.load_script("skill", skill.script_file)
        self.script.execute(EXECUTE_TYPE.GET_SKILL_LEVEL_DATA, skill)
        self._apply_recipe(skill)

        if not self._check_buff(skill, target):
            return False
        if not self._check_learnt_skill(skill):
            return False
        if not self._check_cooldown(skill):
            return False

        # pre casting
        self._set_cooldown(skill)
        self._set_delay_skills(skill)
        self._set_bind_buff(skill, target)
        self._trigger_skill_event(skill, SKILL_EVENT_TYPE.PRE_CAST)

        self._apply_effect(skill, target)
        self._unapply_effect(skill, target)
        self.script.process_timer()
        self._settle_damage()
        self._trigger_skill_event(skill, SKILL_EVENT_TYPE.CAST)
        self._trigger_skill_event(skill, SKILL_EVENT_TYPE.HIT)
        return True

    # Call Damage
    def call_physical_damage(self, damage_base, damage_rand, skill: Skill):
        if not self.current_damage:
            self.current_damage = Damage()

    def call_solar_damage(self, damage_base, damage_rand, skill: Skill):
        if not self.current_damage:
            self.current_damage = Damage()

    def call_lunar_damage(self, damage_base, damage_rand, skill: Skill):
        if not self.current_damage:
            self.current_damage = Damage()

    def call_neutral_damage(self, damage_base, damage_rand, skill: Skill):
        if not self.current_damage:
            self.current_damage = Damage()

    def call_poison_damage(self, damage_base, damage_rand, skill: Skill):
        if not self.current_damage:
            self.current_damage = Damage()

    def _settle_damage(self):
        if self.current_damage:
            self.current_damage = None


class Character(CharacterWithMethod):
    pass


def test():
    script = Script()
    character = Character(1, 8, script)
    target = Character(2, 0, script)
    character.learn_skill_level(10242, 13)
    character.learn_skill_level(10242, 14)
    print(character)

if __name__ == '__main__':
    test()
