from pathlib import Path

from base import BaseSetting
from base.script import Script
from settings import skill_recipe_settings


class SkillRecipeInSetting(BaseSetting):
    recipe_id: int
    recipe_level: int

    skill_id: int
    skill_level: int
    skill_recipe_type: int

    path: str
    script_file: str

    def __init__(self):
        setting_row = skill_recipe_settings[skill_recipe_settings.RecipeID == self.recipe_id].iloc[0]
        for k, v in setting_row.items():
            setattr(self, k, v)


class SkillRecipeInScript(SkillRecipeInSetting):
    script: Script = None

    def __init__(self):
        super().__init__()
        self.script = Script(str(Path(self.path, self.script_file))) if self.script_file else Script()


class SkillRecipeInPython(SkillRecipeInScript):
    index: int = 0


class SkillRecipe(SkillRecipeInPython):
    def __init__(self, recipe_id: int, recipe_level: int):
        self.recipe_id = recipe_id
        self.recipe_level = recipe_level
        super().__init__()
