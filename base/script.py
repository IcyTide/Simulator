import random
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Union

import lupa.lua51 as lupa

from enums.script import ENV_VARIABLES

if TYPE_CHECKING:
    from base.buff import Buff  # noqa
    from base.character import Character  # noqa
    from base.skill import Skill  # noqa

from enums.script import ATTRIBUTE_TYPE


@dataclass
class Effect:
    attribute_type: ATTRIBUTE_TYPE
    param_1: Union[int, float, str]
    param_2: int


class GlobalScript:
    base_path = Path("../jx3_hd_src")

    is_player: Callable[[int], bool]
    is_enemy: Callable[[int, int], bool]
    get_player: Callable[[int], "Character"]
    get_npc: Callable[[int], "Character"]

    def __init__(self, lua_path: str = None):
        self.engine = lupa.LuaRuntime(unpack_returned_tuples=True, encoding="gbk")
        self.prepare_engine()
        if lua_path:
            self.lua_path = lua_path
            if not lua_path.startswith("scripts"):
                self.lua_path = Path("scripts") / self.lua_path
            self.execute(self.lua_path)

    def prepare_engine(self):
        self.engine.globals().GetEditorString = self.get_editor_string
        self.engine.globals().IsClient = self.is_client
        self.engine.globals().Include = self.include
        self.engine.globals().Random = self.random
        self.engine.globals().RemoteCallToClient = self.remote_call_to_client

        self.engine.globals().IsPlayer = self.is_player
        self.engine.globals().IsEnemy = self.is_enemy
        self.engine.globals().GetPlayer = self.get_player
        self.engine.globals().GetNpc = self.get_npc

        for enum_class in ENV_VARIABLES:
            setattr(self.engine.globals(), enum_class.__name__, enum_class)

    def include(self, file):
        self.execute(file)

    def random(self, min_value, max_value):
        return random.randint(min_value, max_value)

    def get_editor_string(self, *params):
        return "\t".join(str(e) for e in params)

    def is_client(self):
        return True

    @staticmethod
    def remote_call_to_client(*args):
        ...

    def execute(self, lua_path):
        lua_path = self.base_path / lua_path
        try:
            with open(lua_path, encoding="utf-8") as f:
                lua_code = f.read()
            self.engine.execute(lua_code)
        except:
            with open(lua_path, "rb") as f:
                lua_code = f.read()
            self.engine.execute(lua_code)


class Script(GlobalScript):

    def get_skill_level_data(self, skill: "Skill"):
        if func := self.engine.globals().GetSkillLevelData:
            return func(skill)
        return None

    def can_cast(self, player: "Character", pre_result: bool = True):
        if func := self.engine.globals().CanCast:
            return func(player, pre_result)
        return None

    def apply(self, character_id: int, skill_source_id: int):
        return self.engine.globals().Apply(character_id, skill_source_id)

    def unapply(self, character_id: int):
        return self.engine.globals().UnApply(character_id)

    def apply_setup(self, setuper_id: int):
        return self.engine.globals().ApplySetup(setuper_id)

    def unapply_setup(self, setuper_id: int):
        return self.engine.globals().UnApplySetup(setuper_id)

    def apply_bullet_to_dest(self, target_id: int, caster_id: int):
        return self.engine.globals().ApplyBulletToDest(target_id, caster_id)

    def apply_bullet_to_dest_and_rollback(self, target_id: int, caster_id: int):
        return self.engine.globals().ApplyBulletToDestAndRollback(target_id, caster_id)

    def unapply_bullet_to_dest_and_rollback(self, target_id: int, caster_id: int):
        return self.engine.globals().UnApplyBulletToDestAndRollback(target_id, caster_id)

    def on_skill_level_up(self, skill: "Skill", player: "Character"):
        if func := self.engine.globals().OnSkillLevelUp:
            return func(skill, player)
        return None

    def on_skill_forgotten(self, skill: "Skill", player: "Character"):
        if func := self.engine.globals().OnSkillForgotten:
            return func(skill, player)
        return None

    def on_bullet_destroy(self, caster_id: int, hit_count: int):
        if func := self.engine.globals().OnBulletDestroy:
            return func(caster_id, hit_count)
        return None

    def on_channel_end(self, caster: "Character", is_complete: bool):
        if func := self.engine.globals().OnChannelEnd:
            return func(caster, is_complete)
        return None

    def on_remove(self, character_id, buff: "Buff"):
        if func := self.engine.globals().OnRemove:
            return func(
                character_id, buff.buff_id, buff.buff_level, buff.left_frame, buff.custom_value,
                buff.source_skill.source_id,  # skill_src_id
                buff.stack_num, buff.index,
                buff.source_id,  # caster_id
                buff.source_skill.skill_id  # caster_skill_id
            )
        return None

    def on_timer(self, player: "Character", param_1, param_2):
        if func := self.engine.globals().OnTimer:
            return func(player, param_1, param_2)
        return None
