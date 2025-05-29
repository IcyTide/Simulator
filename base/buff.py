from base import BaseSetting
from base.attribute import Attribute
from base.constant import BINARY_SCALE
from base.script import AttributeEffect
from base.skill import Skill
from enums.script import ATTRIBUTE_EFFECT_MODE, ATTRIBUTE_TYPE
from settings import buff_settings as settings
from tools.regex import camel_to_capital


class BuffInSetting(BaseSetting):
    _aliases = {
        "Name": "buff_name",
    }

    buff_id: int
    buff_level: int

    is_stackable: bool
    is_countable: bool

    max_stack_num: int
    count: int
    interval: int
    min_interval: int
    max_interval: int
    exclude: int

    script_file: str


    def __init__(self):
        setting_row = settings[
            (settings['ID'] == self.buff_id) & (settings['Level'] == self.buff_level)
        ].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)

        self.begin_attributes = self.get_attributes(15, 'begin')
        self.active_attributes = self.get_attributes(2, 'active')
        self.end_attributes = self.get_attributes(2, 'end_time')

    def get_attributes(self, max_attr_nums, prefix):
        attributes = []
        for i in range(max_attr_nums):
            attr_type = getattr(self, f'{prefix}_attrib{i + 1}')
            if not attr_type:
                break
            param_1, param_2 = getattr(self, f'{prefix}_value{i + 1}_a'), getattr(self, f'{prefix}_value{i + 1}_b')
            attr_type = camel_to_capital(attr_type[2:])
            attr_type = getattr(ATTRIBUTE_TYPE, attr_type)
            attributes.append(
                AttributeEffect(ATTRIBUTE_EFFECT_MODE.EFFECT_TO_DEST_NOT_ROLLBACK, attr_type, param_1, param_2)
            )
        return attributes


class BuffInScript(BuffInSetting):
    attribute: Attribute
    source_skill: Skill

    index: int = 0

    tick: int = 0
    left_active_count: int = 0
    next_active_frame: int = 0
    stack_num: int = 0
    custom_value: int = 0

    @property
    def active_frame(self):
        active_frame = int(self.interval * BINARY_SCALE / (BINARY_SCALE + self.attribute.haste))
        active_frame = min(active_frame, self.max_interval)
        active_frame = max(active_frame, self.min_interval)
        return active_frame


class BuffWithMethod(BuffInScript):
    def begin(self):
        pass

    def end(self):
        pass

    def call_damage(self):
        pass


class Buff(BuffWithMethod):
    source_id: int
    source_level: int

    def __init__(self, source_id, source_level, buff_id, buff_level):
        self.source_id = source_id
        self.source_level = source_level
        self.buff_id = buff_id
        self.buff_level = buff_level
        super().__init__()
