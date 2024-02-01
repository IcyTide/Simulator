from collections import defaultdict

from general.gains.equipment import EQUIP_GAINS_NAME
from qt.components.equipments import EquipmentsWidget
from qt.constant import POSITION_MAP, STONES_POSITIONS, EMBED_POSITIONS, ATTR_TYPE_TRANSLATE, EQUIP_GAINS, \
    ATTR_TYPE_TRANSLATE_REVERSE
from qt.constant import STRENGTH_COF, EMBED_COF, MAX_STRENGTH_LEVEL, MAX_EMBED_LEVEL


class Enchant:
    def __init__(self):
        self.name = ""
        self.attr = {}

    def clear(self):
        self.name = ""
        self.attr = {}


class Stone:
    def __init__(self):
        self.name = ""
        self.level = 0
        self.attr = {}

    def clear(self):
        self.name = ""
        self.attr = {}


class Equipment:
    def __init__(self, label):
        self.label = label
        self.position = POSITION_MAP[label]
        self.name = ""
        self.base = {}
        self.magic = {}
        self.embed = {}
        self.gains = []
        self.special_enchant = []
        self.set_id = ""
        self.set_data = {}

        self.strength_level = MAX_STRENGTH_LEVEL
        self.embed_levels = [MAX_EMBED_LEVEL for _ in range(EMBED_POSITIONS[self.position])]

        self.enchant = Enchant()
        if self.position in STONES_POSITIONS:
            self.stone = Stone()
        else:
            self.stone = None

    def clear(self):
        self.name = ""
        self.base = {}
        self.magic = {}
        self.embed = {}
        self.gains = []
        self.special_enchant = []
        self.set_id = ""
        self.set_data = {}

    @property
    def base_attr(self):
        return self.base

    @property
    def magic_attr(self):
        return self.magic

    @property
    def strength_attr(self):
        if self.strength_level:
            return {k: round(STRENGTH_COF(self.strength_level) * v) for k, v in self.magic.items()}
        else:
            return {}

    @property
    def embed_attr(self):
        return {
            k: int(EMBED_COF(self.embed_levels[i]) * v)
            for i, (k, v) in enumerate(self.embed.items()) if self.embed_levels[i]
        }

    @property
    def base_attr_text(self):
        return "\n".join([f"{ATTR_TYPE_TRANSLATE[k]}:\t{v}" for k, v in self.base_attr.items()])

    @property
    def magic_attr_text(self):
        if strength_attr := self.strength_attr:
            return "\n".join([
                f"{ATTR_TYPE_TRANSLATE[k]}:\t{v}(+{strength_attr[k]})" for k, v in self.magic_attr.items()
            ])
        else:
            return "\n".join([f"{ATTR_TYPE_TRANSLATE[k]}:\t{v}" for k, v in self.magic_attr.items()])

    @property
    def embed_attr_text(self):
        return "\n".join([f"{ATTR_TYPE_TRANSLATE[k]}:\t{v}" for k, v in self.embed_attr.items()])


class Equipments:
    def __init__(self):
        self.equipments = {label: Equipment(label) for label in POSITION_MAP}

    def __getitem__(self, item) -> Equipment:
        return self.equipments[item]

    @property
    def primary_weapon_attrs(self):
        equipment = self.equipments['近战武器']
        if not equipment.name:
            return {}
        
        primary_weapon_attrs = defaultdict(int)
        for attr, value in equipment.base_attr.items():
            primary_weapon_attrs[attr] += value
        for attr, value in equipment.magic_attr.items():
            primary_weapon_attrs[attr] += value
        for attr, value in equipment.strength_attr.items():
            primary_weapon_attrs[attr] += value
        for attr, value in equipment.embed_attr.items():
            primary_weapon_attrs[attr] += value
        for attr, value in equipment.enchant.attr.items():
            primary_weapon_attrs[attr] += value
        for attr, value in equipment.stone.attr.items():
            primary_weapon_attrs[attr] += value
        return primary_weapon_attrs
    
    @property
    def secondary_weapon_attrs(self):
        equipment = self.equipments['额外武器']
        if not equipment.name:
            return {}

        secondary_weapon_attrs = defaultdict(int)
        for attr, value in equipment.base_attr.items():
            secondary_weapon_attrs[attr] += value
        for attr, value in equipment.magic_attr.items():
            secondary_weapon_attrs[attr] += value
        for attr, value in equipment.strength_attr.items():
            secondary_weapon_attrs[attr] += value
        for attr, value in equipment.embed_attr.items():
            secondary_weapon_attrs[attr] += value
        for attr, value in equipment.enchant.attr.items():
            secondary_weapon_attrs[attr] += value
        for attr, value in equipment.stone.attr.items():
            secondary_weapon_attrs[attr] += value
        return secondary_weapon_attrs
    
    @property
    def attrs(self):
        final_attrs = defaultdict(int)
        set_count = {}
        set_effect = {}
        for equipment in self.equipments.values():
            if not equipment.name or equipment.position == "secondary_weapon":
                continue
            for attr, value in equipment.base_attr.items():
                final_attrs[attr] += value
            for attr, value in equipment.magic_attr.items():
                final_attrs[attr] += value
            for attr, value in equipment.strength_attr.items():
                final_attrs[attr] += value
            for attr, value in equipment.embed_attr.items():
                final_attrs[attr] += value
            for attr, value in equipment.enchant.attr.items():
                final_attrs[attr] += value
            if equipment.stone:
                for attr, value in equipment.stone.attr.items():
                    final_attrs[attr] += value

            if equipment.set_id not in set_count:
                set_count[equipment.set_id] = 0
                set_effect[equipment.set_id] = equipment.set_data
            set_count[equipment.set_id] += 1

        for set_id, set_data in set_effect.items():
            for count, effects in set_data.items():
                if int(count) > set_count[set_id]:
                    break
                for effect in effects:
                    if "gain" not in effect:
                        for attr, value in effect.items():
                            final_attrs[attr] += value

        return final_attrs

    @property
    def gains(self):
        final_gains = []
        set_count = {}
        set_effect = {}
        for equipment in self.equipments.values():
            if not equipment.name:
                continue
            final_gains += [gain for gain in equipment.gains + equipment.special_enchant]
            if equipment.set_id not in set_count:
                set_count[equipment.set_id] = 0
                set_effect[equipment.set_id] = equipment.set_data
            set_count[equipment.set_id] += 1

        for set_id, set_data in set_effect.items():
            for count, effects in set_data.items():
                if int(count) > set_count[set_id]:
                    break
                for effect in effects:
                    if gain := effect.get("gain"):
                        final_gains.append(gain)

        return [EQUIP_GAINS[gain] for gain in set(final_gains)]


def equipments_script(equipments_widget: EquipmentsWidget):
    equipments = Equipments()

    def equipment_update(label):
        widget = equipments_widget[label]
        equipment = equipments[label]

        def inner(index):
            equipment_name = widget.equipment.combo_box.currentText()

            if not equipment_name:
                equipment.clear()
                widget.detail_widget.hide()
                widget.output_widget.hide()
                return

            equipment_detail = widget.equipment_json[equipment_name]
            equipment.name = equipment_name
            equipment.base = equipment_detail['base']
            equipment.magic = equipment_detail['magic']
            equipment.gains = equipment_detail['gains']
            equipment.set_id = equipment_detail['set_id']
            equipment.set_data = equipment_detail['set_data']

            if equipment.base:
                widget.base_attr.set_text(equipment.base_attr_text)
                widget.base_attr.show()
            else:
                widget.base_attr.hide()

            max_strength = equipment_detail['max_strength']
            if widget.strength_level == 1:
                pass

            strength_level = max_strength

            widget.strength_level.set_items([str(i) for i in range(max_strength + 1)])
            widget.strength_level.combo_box.setCurrentIndex(strength_level)

            embed = equipment_detail['embed']
            equipment.embed = embed
            if embed:
                for i, (attr, value) in enumerate(embed.items()):
                    widget.embed_levels[i].set_label(f"镶嵌等级-{ATTR_TYPE_TRANSLATE[attr]}")
                widget.embed_attr.set_text(equipment.embed_attr_text)
                widget.embed_attr.show()
            else:
                widget.embed_attr.hide()

            if special_enchant := equipment_detail["special_enchant"]:
                widget.special_enchant.set_text(EQUIP_GAINS_NAME[special_enchant])

            widget.detail_widget.show()
            widget.output_widget.show()

        return inner

    def enchant_update(label):
        widget = equipments_widget.equipments[label]
        equipment = equipments[label]

        def inner(index):
            enchant_name = widget.enchant.combo_box.currentText()
            if enchant_name:
                enchant_detail = widget.enchant_json[enchant_name]
                equipment.enchant.name = enchant_name
                equipment.enchant.attr = enchant_detail['attr']
            else:
                equipment.enchant.clear()

        return inner

    def special_enchant_update(label):
        widget = equipments_widget.equipments[label]
        equipment = equipments[label]

        def inner(index):
            equipment_detail = widget.equipment_json[widget.equipment.combo_box.currentText()]
            special_enchant = equipment_detail['special_enchant']
            if widget.special_enchant and widget.special_enchant.radio_button.isChecked():
                equipment.special_enchant = [special_enchant]
            else:
                equipment.special_enchant = []

        return inner

    def strength_level_update(label):
        widget = equipments_widget.equipments[label]
        equipment = equipments[label]

        def inner(index):
            equipment.strength_level = index
            if magic_attr_text := equipment.magic_attr_text:
                widget.magic_attr.text_browser.setText(magic_attr_text)
                widget.magic_attr.show()
            else:
                widget.magic_attr.hide()

        return inner

    def embed_level_update(i, label):
        widget = equipments_widget.equipments[label]
        equipment = equipments[label]

        def inner(index):
            equipment.embed_levels[i] = index
            if embed_attr_text := equipment.embed_attr_text:
                widget.embed_attr.text_browser.setText(embed_attr_text)
                widget.embed_attr.show()
            else:
                widget.embed_attr.hide()

        return inner

    def stone_update(label):
        widget = equipments_widget.equipments[label]
        equipment = equipments[label]

        def inner(index):
            level = widget.stone_level.combo_box.currentText()

            current = widget.stones_json
            for i in range(len(widget.stone_attrs)):
                attr = ATTR_TYPE_TRANSLATE_REVERSE.get(widget.stone_attrs[i].combo_box.currentText())
                if attr in current:
                    current = current[attr]
                else:
                    widget.stone_attrs[i].combo_box.blockSignals(True)
                    widget.stone_attrs[i].combo_box.clear()
                    widget.stone_attrs[i].combo_box.addItems([""] + [ATTR_TYPE_TRANSLATE[k] for k in current])
                    widget.stone_attrs[i].combo_box.blockSignals(False)

            if level in current:
                equipment.stone.attr = current[level]['attr']
                equipment.stone.level = level

        return inner

    for equipment_label, equipment_widget in equipments_widget.items():

        equipment_widget.equipment.combo_box.currentIndexChanged.connect(equipment_update(equipment_label))
        if equipment_widget.special_enchant:
            equipment_widget.special_enchant.radio_button.clicked.connect(special_enchant_update(equipment_label))
        if equipment_widget.enchant:
            equipment_widget.enchant.combo_box.currentIndexChanged.connect(enchant_update(equipment_label))
        equipment_widget.strength_level.combo_box.currentIndexChanged.connect(strength_level_update(equipment_label))
        for n, embed_widget in enumerate(equipment_widget.embed_levels):
            embed_widget.combo_box.currentIndexChanged.connect(embed_level_update(n, equipment_label))
        if equipment_widget.stones_json:
            equipment_widget.stone_level.combo_box.currentIndexChanged.connect(stone_update(equipment_label))
            for stone_attr in equipment_widget.stone_attrs:
                stone_attr.combo_box.currentIndexChanged.connect(stone_update(equipment_label))

    return equipments
