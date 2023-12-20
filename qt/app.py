import os
import sys

from PySide6 import QtWidgets

from qt.components.top import TopWidget
from qt.scripts.top import top_script
from qt.components.equipments import EquipmentsWidget
from qt.scripts.equipments import equipments_script
from qt.components.consumables import ConsumablesWidget
from qt.components.talents import TalentsWidget
from qt.scripts.talents import talents_script
from qt.components.recipes import RecipesWidget
from qt.scripts.recipes import recipes_script
from qt.components.combat import CombatWidget
from qt.scripts.combat import combat_script

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simulator")
        self.setWindowIcon(QIcon("qt/assets/icon.ico"))
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.resize(960, 640)
        self.layout = QVBoxLayout(self.central_widget)

        self.top_widget = TopWidget()
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.top_widget)
        self.layout.addWidget(self.tab_widget)
        self.layout.addStretch()

        self.equipments_widget = EquipmentsWidget()
        self.tab_widget.addTab(self.equipments_widget, "Equipments")
        self.talents_widget = TalentsWidget()
        self.tab_widget.addTab(self.talents_widget, "Talents")
        self.recipes_widget = RecipesWidget()
        self.tab_widget.addTab(self.recipes_widget, "Recipes")
        self.consumables_widget = ConsumablesWidget()
        self.tab_widget.addTab(self.consumables_widget, "Consumables")
        self.combat_widget = CombatWidget()
        self.tab_widget.addTab(self.combat_widget, "Combat")

        school = top_script(self.top_widget, self.tab_widget,
                            self.equipments_widget, self.talents_widget, self.recipes_widget,
                            self.consumables_widget,
                            self.combat_widget)
        equipments = equipments_script(self.equipments_widget)
        talents = talents_script(self.talents_widget)
        recipes = recipes_script(self.recipes_widget)
        combat_script(school, equipments, talents, recipes, self.combat_widget)

        self.tab_widget.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
