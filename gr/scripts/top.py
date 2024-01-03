import gradio as gr

from gr.constant import SUPPORT_SCHOOL, MAX_RECIPE_SKILLS
from general.consumables import FOODS, POTIONS, WEAPON_ENCHANTS, SPREADS, SNACKS, WINES
from general.gains.formation import FORMATIONS


def top_script(equipments, detail, top_components, combat_components,
               equip_components, consumable_components, gain_components, talent_components, recipe_components):
    def update_school_name(school_name):
        if not school_name:
            return [gr.update(visible=False), None, *[None for _ in equip_components['equips']],
                    *[None for _ in consumable_components['consumables']],
                    *[None for _ in gain_components['formations']],
                    *[None for _ in talent_components['talents']],
                    *[None for _ in recipe_components['recipes']]]
        school_attr = SUPPORT_SCHOOL[school_name]

        equip_updates = []
        for equip in equipments:
            equipment = equipments[equip]
            choices = list(equipment[(equipment['kind'].isin([school_attr['kind'], school_attr['major']])) & (
                equipment['school'].isin(["精简", "通用", school_attr['school']]))].index)
            equip_updates.append(gr.update(choices=[""] + choices, value="", visible=True))

        consumable_updates = [
            gr.update(choices=[""] + FOODS[school_attr['major']], value=""),
            gr.update(choices=[""] + FOODS[school_attr['kind']] + FOODS[""], value=""),
            gr.update(choices=[""] + POTIONS[school_attr['major']], value=""),
            gr.update(choices=[""] + POTIONS[school_attr['kind']] + POTIONS[""], value=""),
            gr.update(choices=[""] + WEAPON_ENCHANTS[school_attr['kind']], value=""),
            gr.update(choices=[""] + SNACKS[school_attr['kind']] + SNACKS[""], value=""),
            gr.update(choices=[""] + WINES[school_attr['major']] + WINES[""], value=""),
            None,
            None,
            gr.update(choices=[""] + SPREADS[school_attr['major']] + SPREADS[school_attr['kind']], value=""),
            None
        ]
        gain_updates = [
            school_attr['formation'],
            gr.update(choices=[""] + FORMATIONS[school_attr['kind']] + FORMATIONS[""], value=""),
            None,
            None
        ]
        talent_updates = [
            gr.update(choices=[""] + talents, value="") for talents in school_attr['talents']
        ]
        recipe_updates = [
            gr.update(choices=recipes, label=skill, interactive=True, visible=True) for skill, recipes in
            school_attr['recipes'].items()
        ]
        for _ in range(MAX_RECIPE_SKILLS - len(recipe_updates)):
            recipe_updates.append(gr.update(visible=False))

        return (gr.update(visible=True), school_attr, *school_attr['sequences'].values(),
                *equip_updates, *consumable_updates, *gain_updates, *talent_updates, *recipe_updates)

    top_components['school_name'].input(
        update_school_name, top_components['school_name'],
        [detail, combat_components['school_attr'], *combat_components['sequences'].values(),
         *[equip_component['equip_name'] for equip_component in equip_components['equips'].values()],
         *consumable_components['consumables'].values(), *gain_components['formations'].values(),
         *talent_components['talents'], *recipe_components['recipes']])
