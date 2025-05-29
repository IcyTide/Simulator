from base import BaseSetting
from settings import skill_recipe_settings as settings


class SkillRecipeInSetting(BaseSetting):
    index: int

    recipe_id: int
    recipe_level: int
    skill_recipe_type: int
    skill_id: int

    damage_add_percent: int

    script_file: str

    def __init__(self):
        setting_row = settings[
            (settings['RecipeID'] == self.recipe_id) & (settings['RecipeLevel'] == self.recipe_level)
        ].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)

class SkillRecipeInScript(SkillRecipeInSetting):
    pass


class SkillWithMethod(SkillRecipeInScript):
    pass


class SkillRecipe(SkillWithMethod):
    def __init__(self, recipe_id, recipe_level):
        self.recipe_id = recipe_id
        self.recipe_level = recipe_level
        super().__init__()
