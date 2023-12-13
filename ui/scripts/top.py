import gradio as gr

from ui.constant import SUPPORT_CLASS, MAX_RECIPE_SKILLS
from general.consumables import FOODS, POTIONS, WEAPON_ENCHANTS, SPREADS, SNACKS, WINES
from general.gains.formation import FORMATIONS


def top_script(equipments, detail, top_components, combat_components,
               equip_components, consumable_components, gain_components, talent_components, recipe_components):
    def update_class_name(class_name):
        if not class_name:
            return [gr.update(visible=False), None, *[None for _ in equip_components['equips']],
                    *[None for _ in consumable_components['consumables']],
                    *[None for _ in gain_components['formations']],
                    *[None for _ in talent_components['talents']],
                    *[None for _ in recipe_components['recipes']]]
        class_attr = SUPPORT_CLASS[class_name]

        equip_updates = []
        for equip in equipments:
            equipment = equipments[equip]
            choices = list(equipment[(equipment['kind'].isin([class_attr['kind'], class_attr['major']])) & (
                equipment['school'].isin(["精简", "通用", class_attr['school']]))].index)
            equip_updates.append(gr.update(choices=[""] + choices, value="", visible=True))

        consumable_updates = [
            gr.update(choices=[""] + FOODS[class_attr['major']], value=""),
            gr.update(choices=[""] + FOODS[class_attr['kind']] + FOODS["通用"], value=""),
            gr.update(choices=[""] + POTIONS[class_attr['major']], value=""),
            gr.update(choices=[""] + POTIONS[class_attr['kind']] + POTIONS["通用"], value=""),
            gr.update(choices=[""] + WEAPON_ENCHANTS[class_attr['kind']], value=""),
            gr.update(choices=[""] + SNACKS[class_attr['kind']] + SNACKS["通用"], value=""),
            gr.update(choices=[""] + WINES[class_attr['major']] + WINES["通用"], value=""),
            None,
            None,
            gr.update(choices=[""] + SPREADS[class_attr['major']] + SPREADS[class_attr['kind']], value=""),
            None
        ]
        gain_updates = [
            class_attr['formation'],
            gr.update(choices=[""] + FORMATIONS[class_attr['kind']] + FORMATIONS["通用"], value=""),
            None,
            None
        ]
        talent_updates = [
            gr.update(choices=[""] + talents, value="") for talents in class_attr['talents']
        ]
        recipe_updates = [
            gr.update(choices=recipes, label=skill, interactive=True, visible=True) for skill, recipes in
            class_attr['recipes'].items()
        ]
        for _ in range(MAX_RECIPE_SKILLS - len(recipe_updates)):
            recipe_updates.append(gr.update(visible=False))

        return (gr.update(visible=True), class_attr, *class_attr['sequences'].values(),
                *equip_updates, *consumable_updates, *gain_updates, *talent_updates, *recipe_updates)

    top_components['class_name'].input(
        update_class_name, top_components['class_name'],
        [detail, combat_components['class_attr'], *combat_components['sequences'].values(),
         *[equip_component['equip_name'] for equip_component in equip_components['equips'].values()],
         *consumable_components['consumables'].values(), *gain_components['formations'].values(),
         *talent_components['talents'], *recipe_components['recipes']])
