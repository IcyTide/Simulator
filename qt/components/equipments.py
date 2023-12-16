import json
import os

from qt.constant import POSITION_MAP, STONES_POSITIONS, EQUIPMENTS_DIR, ENCHANTS_DIR, STONES_DIR, MAX_STONE_ATTR
from qt.constant import EMBED_POSITIONS, MAX_STRENGTH_LEVEL, MAX_EMBED_LEVEL, MAX_STONE_LEVEL, SPECIAL_ENCHANT_POSITIONS
from qt.components import ComboWithLabel, RadioWithLabel, TextWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTabWidget


class EquipmentWidget(QWidget):
    def __init__(self, label):
        super().__init__()
        self.position = POSITION_MAP[label]
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.input_widget = QWidget()
        input_layout = QVBoxLayout()
        self.input_widget.setLayout(input_layout)
        layout.addWidget(self.input_widget, 6)
        self.output_widget = QWidget()
        output_layout = QVBoxLayout()
        self.output_widget.setLayout(output_layout)
        layout.addWidget(self.output_widget, 4)

        self.equipment_json = json.load(open(os.path.join(EQUIPMENTS_DIR, self.position), encoding="utf-8"))
        self.enchant_json = json.load(open(os.path.join(ENCHANTS_DIR, self.position), encoding="utf-8"))
        self.equipment = ComboWithLabel("Equipment")

        self.detail_widget = QWidget()
        detail_layout = QVBoxLayout()
        self.detail_widget.setLayout(detail_layout)
        input_layout.addWidget(self.equipment)
        input_layout.addWidget(self.detail_widget)
        input_layout.addStretch()

        self.enchant_widget = QWidget()
        enchant_layout = QHBoxLayout()
        self.enchant_widget.setLayout(enchant_layout)
        if not self.enchant_json:
            self.enchant = None
        else:
            self.enchant = ComboWithLabel("Enchant")
            self.enchant.combo_box.addItems([""] + list(self.enchant_json))
            enchant_layout.addWidget(self.enchant)

        if self.position not in SPECIAL_ENCHANT_POSITIONS:
            self.special_enchant = None
        else:
            self.special_enchant = RadioWithLabel("Special Enchant")
            enchant_layout.addWidget(self.special_enchant)
        detail_layout.addWidget(self.enchant_widget)

        self.strength_widget = QWidget()
        strength_layout = QVBoxLayout()
        self.strength_widget.setLayout(strength_layout)
        self.strength_level = ComboWithLabel("Strength Level")
        self.strength_level.combo_box.setCurrentIndex(MAX_STRENGTH_LEVEL)
        strength_layout.addWidget(self.strength_level)
        detail_layout.addWidget(self.strength_widget)

        self.embed_widget = QWidget()
        embed_layout = QHBoxLayout()
        self.embed_widget.setLayout(embed_layout)
        self.embed_levels = []
        for i in range(EMBED_POSITIONS[self.position]):
            embed_level = ComboWithLabel(f"Embed Level-{i + 1}", [str(i) for i in range(MAX_EMBED_LEVEL + 1)])
            embed_level.combo_box.setCurrentIndex(MAX_EMBED_LEVEL)
            self.embed_levels.append(embed_level)
            embed_layout.addWidget(embed_level)
        detail_layout.addWidget(self.embed_widget)

        self.stone_level_widget = QWidget()
        stone_level_layout = QVBoxLayout()
        self.stone_level_widget.setLayout(stone_level_layout)
        self.stone_widget = QWidget()
        stone_layout = QHBoxLayout()
        self.stone_widget.setLayout(stone_layout)
        if self.position not in STONES_POSITIONS:
            self.stones_json = None
            self.stone_level = None
            self.stone_attrs = None
        else:
            self.stones_json = json.load(open(STONES_DIR, encoding="utf-8"))

            self.stone_level = ComboWithLabel("Stone Level", [str(i) for i in range(MAX_STONE_LEVEL + 1)])
            self.stone_attrs = []
            stone_level_layout.addWidget(self.stone_level)
            for i in range(MAX_STONE_ATTR):
                stone_attr = ComboWithLabel(f"Stone Attr-{i + 1}")
                self.stone_attrs.append(stone_attr)
                stone_layout.addWidget(stone_attr)

        detail_layout.addWidget(self.stone_level_widget)
        detail_layout.addWidget(self.stone_widget)

        detail_layout.addStretch()

        self.base_attr = TextWithLabel("Base Attr")
        output_layout.addWidget(self.base_attr)
        self.magic_attr = TextWithLabel("Magic Attr")
        output_layout.addWidget(self.magic_attr)
        self.embed_attr = TextWithLabel("Embed Attr")
        output_layout.addWidget(self.embed_attr)
        output_layout.addStretch()


class EquipmentsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.tab = QTabWidget()
        self.equipments = {}
        for label in POSITION_MAP:
            self.equipments[label] = EquipmentWidget(label)
            self.tab.addTab(self.equipments[label], label)

        layout.addWidget(self.tab)

    def __getitem__(self, item) -> EquipmentWidget:
        return self.equipments[item]

    def items(self):
        return self.equipments.items()

    def values(self):
        return self.equipments.values()
