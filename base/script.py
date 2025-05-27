from dataclasses import dataclass
from typing import Union, Dict
import lupa.lua54 as lupa

from base.character import Character
from enums.script import *
from tools import read_script


@dataclass
class AttributeEffect:
    attribute_effect_mode: ATTRIBUTE_EFFECT_MODE
    attribute_type: ATTRIBUTE_TYPE
    param_1: Union[int, float, str]
    param_2: int


class Global:
    engine: lupa.LuaRuntime
    character_map: Dict[int, Character]

    @staticmethod
    def get_editor_string(*params):
        return "\t".join(str(e) for e in params)

    @staticmethod
    def is_client():
        return True

    def get_player(self, character_id):
        return self.character_map.get(character_id)

    def prepare_script(self):
        engine = lupa.LuaRuntime()
        for enum_class in ENV_VARIABLES:
            setattr(engine.globals(), enum_class.__name__, enum_class)
        engine.globals().GetEditorString = self.get_editor_string
        engine.globals().IsClient = self.is_client
        engine.globals().GetPlayer = self.get_player
        engine.execute(read_script("include", "skill.lh"))
        engine.execute(read_script("include", "newskill.lh"))
        return engine

    def load_script(self, script_file):
        self.engine = self.prepare_script()
        self.engine.execute(read_script("skill", script_file))


    def execute(self, execute_type: EXECUTE_TYPE, *args):
        return self.engine.globals()[execute_type.value](*args)
