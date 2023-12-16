from qt.components import ListWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from qt.constant import MAX_RECIPE_SKILLS


class RecipesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.recipes_row1 = QWidget()
        row1_layout = QVBoxLayout()
        self.recipes_row1.setLayout(row1_layout)
        layout.addWidget(self.recipes_row1)

        self.recipes_row2 = QWidget()
        row2_layout = QVBoxLayout()
        self.recipes_row2.setLayout(row2_layout)
        layout.addWidget(self.recipes_row2)

        self.recipes = []
        for i in range(MAX_RECIPE_SKILLS // 2):
            recipe = ListWithLabel(f"recipe {i + 1}")
            self.recipes.append(recipe)
            row1_layout.addWidget(recipe)
        row1_layout.addStretch()

        for i in range(MAX_RECIPE_SKILLS // 2, MAX_RECIPE_SKILLS):
            recipe = ListWithLabel(f"recipe {i + 1}")
            self.recipes.append(recipe)
            row2_layout.addWidget(recipe)
        row2_layout.addStretch()
        
    def __getitem__(self, item) -> ListWithLabel:
        return self.recipes[item]

    def values(self) -> list[ListWithLabel]:
        return self.recipes
