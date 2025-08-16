import pandas as pd

from tools import read_tab

skill_settings = read_tab("settings/skill/skills.tab")
skill_mobile_settings = read_tab("settings/skill_mobile/skills.tab")
skill_settings["Path"], skill_mobile_settings["Path"] = "skill", "skill_mobile"
skill_settings = pd.concat([skill_settings, skill_mobile_settings])

buff_settings, buff_settings["Path"] = read_tab("settings/skill/buff.tab"), "skill"
buff_mobile_settings, buff_mobile_settings["Path"] = read_tab("settings/skill_mobile/buff.tab"), "skill_mobile"
buff_settings = pd.concat([buff_settings, buff_mobile_settings])

cooldown_settings = read_tab("settings/cooldownlist.tab", "settings/skill_mobile/cooldownlist.tab")

skill_recipe_settings = read_tab("settings/skill/recipeskill.tab")
skill_mobile_recipe_settings = read_tab("settings/skill_mobile/recipeskill.tab")
skill_recipe_settings["Path"], skill_mobile_recipe_settings["Path"] = "skill", "skill_mobile"
skill_recipe_settings = pd.concat([skill_recipe_settings, skill_mobile_recipe_settings])

skill_event_settings = read_tab("settings/skill/skillevent.tab", "settings/skill_mobile/skillevent.tab")

skill_move_settings = read_tab("settings/skillmove.tab", "settings/skill_mobile/skillmove.tab")