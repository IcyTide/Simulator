from qt.components import ListWithLabel
from PySide6.QtWidgets import QWidget, QGridLayout

from qt.constant import MAX_RECIPE_SKILLS


class RecipesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)

        self.recipes = []

        columns = 2
        rows = MAX_RECIPE_SKILLS // columns
        for i in range(rows):
            for j in range(columns):
                recipe = ListWithLabel(f"技能 {i * columns + j + 1}")
                self.recipes.append(recipe)
                layout.addWidget(recipe, i, j)
        
    def __getitem__(self, item) -> ListWithLabel:
        return self.recipes[item]

    def values(self) -> list[ListWithLabel]:
        return self.recipes
