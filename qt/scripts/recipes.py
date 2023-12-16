from qt.components.recipes import RecipesWidget

from qt.constant import MAX_RECIPE_SKILLS, MAX_RECIPES, RECIPE_GAINS


class Recipes:
    def __init__(self):
        self.recipes = [[] for _ in range(MAX_RECIPE_SKILLS)]

    def __getitem__(self, item):
        return self.recipes[item]

    def __setitem__(self, key, value):
        self.recipes[key] = value

    @property
    def gains(self):
        return [RECIPE_GAINS[recipe] for recipes in self.recipes for recipe in recipes]


def recipes_script(recipes_widget: RecipesWidget):
    recipes = Recipes()

    def recipe_update(i):
        widget = recipes_widget[i]

        def inner():
            if selected_items := widget.list_widget.selectedItems():
                while len(selected_items) > MAX_RECIPES:
                    selected_items.pop().setSelected(False)
            recipes[i] = [item.text() for item in selected_items]

        return inner

    for n, recipe_widget in enumerate(recipes_widget.values()):
        recipe_widget.list_widget.itemSelectionChanged.connect(recipe_update(n))

    return recipes
