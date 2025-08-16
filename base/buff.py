from pathlib import Path
from typing import List

from base import BaseSetting
from base.script import Effect, Script
from base.skill import Skill
from base.utils import apply_haste
from enums.script import ATTRIBUTE_TYPE
from settings import buff_settings
from tools.regex import camel_to_capital


class BuffInSetting(BaseSetting):
    _aliases = {
        "Name": "buff_name"
    }

    buff_id: int
    buff_level: int
    buff_name: str

    append_type: int
    detach_type: int

    is_stackable: bool
    is_countable: bool

    max_stack_num: int
    count: int
    interval: int
    min_interval: int

    exclude: int
    global_exclude: int
    coexist: int

    path: str
    script_file: str

    def __init__(self):
        setting_row = buff_settings[
            (buff_settings['ID'] == self.buff_id) & (buff_settings['Level'] == self.buff_level)
            ].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)


class BuffInScript(BuffInSetting):
    begin_effects: List[Effect]
    active_effects: List[Effect]
    end_effects: List[Effect]

    script: Script

    def __init__(self):
        super().__init__()
        self.begin_effects = self.get_effects('begin')
        self.active_effects = self.get_effects('active')
        self.end_effects = self.get_effects('end_time')

        self.script = Script(str(Path(self.path, self.script_file))) if self.script_file else Script()

    def get_effects(self, prefix):
        effects = []
        i = 0
        while True:
            attrib = f"{prefix}_attrib{i + 1}"
            if not hasattr(self, attrib):
                break
            attribute_type = getattr(self, attrib)
            if not attribute_type:
                break
            param_1, param_2 = getattr(self, f'{prefix}_value{i + 1}_a'), getattr(self, f'{prefix}_value{i + 1}_b')
            attribute_type = camel_to_capital(attribute_type[2:])
            effects.append(
                Effect(ATTRIBUTE_TYPE[attribute_type], param_1, param_2)
            )
            i += 1
        return effects


class BuffInPython(BuffInScript):
    index: int = 0

    source_id: int
    source_skill: Skill

    tick: int = 0
    left_active_count: int = 0
    active_frame: int = 0
    next_active_frame: int = 0
    stack_num: int = 0
    custom_value: int = 0

    sub_buffs: List["Buff"]

    def __init__(self):
        super().__init__()
        self.sub_buffs = []

    @property
    def left_frame(self):
        return self.left_active_count * self.active_frame + self.next_active_frame

    def get_active_frame(self, haste: float):
        if not self.interval:
            return 0
        if 0 < self.min_interval < self.interval:
            return max(apply_haste(self.interval, haste), self.min_interval)
        return self.interval


class Buff(BuffInPython):
    def __init__(self, source_id: int, source_level: int, buff_id: int, buff_level: int, source_skill: Skill):
        self.source_id = source_id
        self.buff_id = buff_id
        self.buff_level = buff_level
        self.source_skill = source_skill
        super().__init__()
