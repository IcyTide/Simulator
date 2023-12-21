from qt.components import ListWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from qt.constant import MAX_RECIPE_SKILLS


class RecipesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        column1 = QWidget()
        column1_layout = QVBoxLayout()
        column1.setLayout(column1_layout)
        layout.addWidget(column1)

        column2 = QWidget()
        column2_layout = QVBoxLayout()
        column2.setLayout(column2_layout)
        layout.addWidget(column2)

        self.recipes = []
        for i in range(MAX_RECIPE_SKILLS // 2):
            recipe = ListWithLabel(f"技能 {i + 1}")
            self.recipes.append(recipe)
            column1_layout.addWidget(recipe)
        column1_layout.addStretch()

        for i in range(MAX_RECIPE_SKILLS // 2, MAX_RECIPE_SKILLS):
            recipe = ListWithLabel(f"技能 {i + 1}")
            self.recipes.append(recipe)
            column2_layout.addWidget(recipe)
        column2_layout.addStretch()
        
    def __getitem__(self, item) -> ListWithLabel:
        return self.recipes[item]

    def values(self) -> list[ListWithLabel]:
        return self.recipes
