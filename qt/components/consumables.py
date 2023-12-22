from general.consumables import BOILED_FISH
from qt.components import ComboWithLabel, RadioWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout


class ConsumablesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.consumables = {}

        row = QWidget()
        row_layout = QHBoxLayout(row)
        layout.addWidget(row)

        self.major_food = ComboWithLabel("辅助类食品")
        self.consumables['major_food'] = self.major_food
        row_layout.addWidget(self.major_food)
        self.minor_food = ComboWithLabel("增强类食品")
        self.consumables['minor_food'] = self.minor_food
        row_layout.addWidget(self.minor_food)
        self.major_potion = ComboWithLabel("辅助类药品")
        self.consumables['major_potion'] = self.major_potion
        row_layout.addWidget(self.major_potion)
        self.minor_potion = ComboWithLabel("增强类药品")
        self.consumables['minor_potion'] = self.minor_potion
        row_layout.addWidget(self.minor_potion)

        row = QWidget()
        row_layout = QHBoxLayout(row)
        layout.addWidget(row)

        self.weapon_enchant = ComboWithLabel("武器磨石")
        self.consumables['weapon_enchant'] = self.weapon_enchant
        row_layout.addWidget(self.weapon_enchant)
        self.home_snack = ComboWithLabel("家园食物")
        self.consumables['home_snack'] = self.home_snack
        row_layout.addWidget(self.home_snack)
        self.home_wine = ComboWithLabel("家园酒")
        self.consumables['home_wine'] = self.home_wine
        row_layout.addWidget(self.home_wine)

        row = QWidget()
        row_layout = QHBoxLayout(row)
        layout.addWidget(row)

        self.guild_spread = RadioWithLabel("同泽宴", "234破招/无双")
        self.consumables['guild_spread'] = self.guild_spread
        row_layout.addWidget(self.guild_spread)
        self.guild_food = RadioWithLabel("蒸鱼餐盘", "517无双")
        self.consumables['guild_food'] = self.guild_food
        row_layout.addWidget(self.guild_food)
        self.spread = ComboWithLabel("宴席")
        self.consumables['spread'] = self.spread
        row_layout.addWidget(self.spread)
        self.boiled_fish = ComboWithLabel("水煮鱼",  items=[""] + BOILED_FISH)
        self.consumables['boiled_fish'] = self.boiled_fish
        row_layout.addWidget(self.boiled_fish)

        layout.addStretch()

    def __getitem__(self, item) -> [ComboWithLabel, RadioWithLabel]:
        return self.consumables[item]

    def items(self):
        return self.consumables.items()
