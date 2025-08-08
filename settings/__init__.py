import pandas as pd

from tools import read_tab

skill_settings, skill_settings["Path"] = read_tab("settings/skill/skills.tab"), "skill"
skill_mobile_settings, skill_mobile_settings["Path"] = read_tab("settings/skill_mobile/skills.tab"), "skill_mobile"
skill_settings = pd.concat([skill_settings, skill_mobile_settings])

buff_settings, buff_settings["Path"] = read_tab("settings/skill/buff.tab"), "skill"
buff_mobile_settings, buff_mobile_settings["Path"] = read_tab("settings/skill_mobile/buff.tab"), "skill_mobile"
buff_settings = pd.concat([buff_settings, buff_mobile_settings])

cooldown_settings = read_tab("settings/cooldownlist.tab", "settings/skill_mobile/cooldownlist.tab")
