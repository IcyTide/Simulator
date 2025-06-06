from collections import defaultdict
from dataclasses import dataclass
from typing import Union, TYPE_CHECKING, Callable, Dict, List
import lupa.lua54 as lupa

from enums.script import *
from tools import read_script
if TYPE_CHECKING:
    from base.character import BaseCharacter


@dataclass
class AttributeEffect:
    attribute_effect_mode: ATTRIBUTE_EFFECT_MODE
    attribute_type: ATTRIBUTE_TYPE
    param_1: Union[int, float, str]
    param_2: int



class Timer:
    timer_function: Callable
    args: tuple
    set_frame: int
    delay_frame: int

    def __init__(self, set_frame: int, delay_frame: int, timer_function: Callable, *args):
        self.timer_function = timer_function
        self.set_frame = set_frame
        self.delay_frame = delay_frame
        self.args = args

    @property
    def tick_frame(self):
        return self.set_frame + self.delay_frame

    def __call__(self):
        self.timer_function(*self.args)


class BaseScript:
    engine: lupa.LuaRuntime
    character_map: Dict[int, 'BaseCharacter']
    time_map: Dict[int, List[Timer]]
    frame: int

    def __init__(self):
        self.character_map = {}
        self.timer_map = defaultdict(list)
        self.frame = 0

    def get_character_by_id(self, character_id):
        return self.character_map.get(character_id)

    def add_character(self, character: 'BaseCharacter'):
        self.character_map[character.id] = character

    def set_timer(self, delay_frame: int, timer_function: Callable, *args):
        self.timer_map[self.frame + delay_frame].append(Timer(self.frame, delay_frame, timer_function, *args))

    def process_timer(self):
        for frame, timers in self.timer_map.items():
            if frame > self.frame:
                break
            for timer in timers:
                timer()
        self.timer_map.pop(self.frame)

class Script(BaseScript):
    engine: lupa.LuaRuntime = None

    @staticmethod
    def get_editor_string(*params):
        return "\t".join(str(e) for e in params)

    @staticmethod
    def is_client():
        return True

    def get_player(self, character_id):
        return self.get_character_by_id(character_id)

    def get_npc(self, character_id):
        return self.get_character_by_id(character_id)

    def prepare_script(self):
        if not self.engine:
            self.engine = lupa.LuaRuntime()
            for enum_class in ENV_VARIABLES:
                setattr(self.engine.globals(), enum_class.__name__, enum_class)
            self.engine.globals().GetEditorString = self.get_editor_string
            self.engine.globals().IsClient = self.is_client
            self.engine.globals().GetPlayer = self.get_player
            self.engine.globals().GetNpc = self.get_npc
            self.engine.execute(read_script("include", "skill.lh"))
            self.engine.execute(read_script("include", "newskill.lh"))
        return self.engine

    def load_script(self, *script_file):
        if script_content := read_script(*script_file):
            self.prepare_script()
            self.engine.execute(script_content)
            return self.engine
        return None

    def execute(self, execute_type: EXECUTE_TYPE, *args):
        return self.engine.globals()[execute_type.value](*args)
