from qt.components import ComboWithLabel, RadioWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout


class ConsumablesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        row1 = QWidget()
        row1_layout = QHBoxLayout()
        row1.setLayout(row1_layout)
        layout.addWidget(row1)
        
        self.major_food = ComboWithLabel("Major Food")
        row1_layout.addWidget(self.major_food)
        self.minor_food = ComboWithLabel("Minor Food")
        row1_layout.addWidget(self.minor_food)
        self.major_potion = ComboWithLabel("Major Potion")
        row1_layout.addWidget(self.major_potion)
        self.minor_potion = ComboWithLabel("Minor Potion")
        row1_layout.addWidget(self.minor_potion)

        row2 = QWidget()
        row2_layout = QHBoxLayout()
        row2.setLayout(row2_layout)
        layout.addWidget(row2)

        self.weapon_enchant = ComboWithLabel("Weapon Enchant")
        row2_layout.addWidget(self.weapon_enchant)
        self.home_snack = ComboWithLabel("Home Snack")
        row2_layout.addWidget(self.home_snack)
        self.home_wine = ComboWithLabel("Home Wine")
        row2_layout.addWidget(self.home_wine)

        row3 = QWidget()
        row3_layout = QHBoxLayout()
        row3.setLayout(row3_layout)
        layout.addWidget(row3)

        self.guild_spread = RadioWithLabel("Guild Spread", "234 surplus&strain")
        row3_layout.addWidget(self.guild_spread)
        self.guild_food = RadioWithLabel("Guild Food", "517 strain")
        row3_layout.addWidget(self.guild_food)
        self.spread = ComboWithLabel("Spread")
        row3_layout.addWidget(self.spread)
        self.boiled_fish = ComboWithLabel("Boiled Fish")
        row3_layout.addWidget(self.spread)

        layout.addStretch()
