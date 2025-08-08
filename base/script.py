from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Union

import lupa.lua51 as lupa

from enums.script import ENV_VARIABLES

if TYPE_CHECKING:
    from base.character import Character  # noqa
    from base.skill import Skill  # noqa

from enums.script import ATTRIBUTE_TYPE


@dataclass
class Effect:
    attribute_type: ATTRIBUTE_TYPE
    param_1: Union[int, float, str]
    param_2: int


class BaseScript:
    base_path = Path("../jx3_hd_src")

    def __init__(self, lua_path: str):
        self.engine = lupa.LuaRuntime(encoding="gbk")
        self.prepare_engine()
        lua_path = Path("scripts") / lua_path
        self.execute(lua_path)

    def prepare_engine(self):
        self.engine.globals().GetEditorString = self.get_editor_string
        self.engine.globals().IsClient = self.is_client
        self.engine.globals().Include = self.include
        for enum_class in ENV_VARIABLES:
            setattr(self.engine.globals(), enum_class.__name__, enum_class)

    def include(self, file):
        self.execute(file)

    @staticmethod
    def get_editor_string(*params):
        return "\t".join(str(e) for e in params)

    @staticmethod
    def is_client():
        return True

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


class Script(BaseScript):

    def get_skill_level_data(self, skill: "Skill"):
        return self.engine.globals().GetSkillLevelData(skill)

    def apply_by_editor(self, skill: "Skill"): ...

    def can_cast(self, player: "Character", pre_result: bool = True):
        return self.engine.globals().CanCast(player, pre_result)

    def apply(self, character_id: int, skill_source_id: int):
        return self.engine.globals().Apply(character_id, skill_source_id)

    def unapply(self, character_id: int):
        return self.engine.globals().UnApply(character_id)

    def apply_setup(self, setuper_id: int):
        return self.engine.globals().ApplySetup(setuper_id)

    def unapply_setup(self, setuper_id: int):
        return self.engine.globals().UnApplySetup(setuper_id)

    def apply_bullet_to_dest_and_rollback(self, target_id: int, caster_id: int):
        return self.engine.globals().ApplyBulletToDestAndRollback(target_id, caster_id)

    def unapply_bullet_to_dest_and_rollback(self, target_id: int, caster_id: int):
        return self.engine.globals().UnApplyBulletToDestAndRollback(target_id, caster_id)

    def on_bullet_destroy(self, caster_id: int, hit_count: int):
        return self.engine.globals().OnBulletDestroy(caster_id, hit_count)

    def on_channel_end(self, caster: "Character", is_complete: bool):
        return self.engine.globals().OnChannelEnd(caster, is_complete)
