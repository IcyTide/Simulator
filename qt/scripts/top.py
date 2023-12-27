from PySide6.QtWidgets import QTabWidget

from qt.components.equipments import EquipmentsWidget
from qt.components.talents import TalentsWidget
from qt.components.recipes import RecipesWidget
from qt.components.consumables import ConsumablesWidget
from qt.components.bonuses import BonusesWidget
from qt.components.combat import CombatWidget
from qt.components.top import TopWidget

from general.consumables import FOODS, POTIONS, WEAPON_ENCHANTS, SPREADS, SNACKS, WINES
from general.gains.formation import FORMATIONS
from qt.constant import SUPPORT_SCHOOL, MAX_RECIPES, MAX_STONE_LEVEL


class School:
    kind: str = ""
    major: str = ""
    school: str = ""
    talents: list = None
    recipes: dict = None
    attribute: type = None,
    formation: str = ""
    skills: list = None,
    buffs: list = None,
    initiation = None,
    prepare: str = "",
    priority: str = "",
    loop: str = "",
    display_attrs: dict = None

    def attr_text(self, attribute):
        texts = []
        for attr, name in self.display_attrs.items():
            value = getattr(attribute, attr)
            if isinstance(value, int):
                texts.append(f"{name}:\t{value}")
            else:
                texts.append(f"{name}:\t{round(value * 100, 2)}%")
        return "\n".join(texts)


def top_script(top_widget: TopWidget, tab_widget: QTabWidget,
               equipments_widget: EquipmentsWidget, talents_widget: TalentsWidget, recipes_widget: RecipesWidget,
               consumables_widget: ConsumablesWidget, bonuses_widget: BonusesWidget,
               combat_widget: CombatWidget):
    school = School()

    def school_update(index):
        school_name = top_widget.school.combo_box.itemText(index)
        for key, value in SUPPORT_SCHOOL[school_name].items():
            setattr(school, key, value)

        for equipment_widget in equipments_widget.values():
            choices = [""]
            for name, detail in equipment_widget.equipment_json.items():
                if detail['kind'] not in (school.kind, school.major):
                    continue
                if detail['school'] not in ("精简", "通用", school.school):
                    continue
                choices.append(name)

            equipment_widget.equipment.set_items(choices)

            if equipment_widget.stones_json:
                equipment_widget.stone_level.combo_box.setCurrentIndex(MAX_STONE_LEVEL)

        for i, talent_widget in enumerate(talents_widget.values()):
            talent_widget.set_items(school.talents[i])

        for recipe_widget in recipes_widget.values():
            recipe_widget.list.clear()
            recipe_widget.hide()

        for i, (skill, recipes) in enumerate(school.recipes.items()):
            recipes_widget[i].set_label(skill)
            recipes_widget[i].set_items(recipes)
            for n in range(MAX_RECIPES):
                recipes_widget[i].list.item(n).setSelected(True)
            recipes_widget[i].show()

        consumables_widget.major_food.set_items([""] + FOODS[school.major])
        consumables_widget.minor_food.set_items([""] + FOODS[school.kind] + FOODS[""])
        consumables_widget.major_potion.set_items([""] + POTIONS[school.major])
        consumables_widget.minor_potion.set_items([""] + POTIONS[school.kind] + POTIONS[""])
        consumables_widget.weapon_enchant.set_items([""] + WEAPON_ENCHANTS[school.kind])
        consumables_widget.home_snack.set_items([""] + SNACKS[school.kind] + SNACKS[""])
        consumables_widget.home_wine.set_items([""] + WINES[school.major] + WINES[""])
        consumables_widget.spread.set_items([""] + SPREADS[school.major] + SPREADS[school.kind])

        bonuses_widget.formation.formation.set_items([""] + FORMATIONS[school.kind] + FORMATIONS[""])
        combat_widget.prepare.set_text(school.prepare)
        combat_widget.priority.set_text(school.priority)
        combat_widget.loop.set_text(school.loop)
        if index >= 0:
            tab_widget.show()

    top_widget.school.combo_box.currentIndexChanged.connect(school_update)

    return school
