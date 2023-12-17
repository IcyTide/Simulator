from PySide6.QtWidgets import QTabWidget

from base.attribute import Attribute
from qt.components.equipments import EquipmentsWidget
from qt.components.talents import TalentsWidget
from qt.components.recipes import RecipesWidget
from qt.components.combat import CombatWidget
from qt.components.top import TopWidget
from qt.constant import SUPPORT_SCHOOL


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

            equipment_widget.equipment.combo_box.clear()
            equipment_widget.equipment.combo_box.addItems(choices)
        for i, talent_widget in enumerate(talents_widget.values()):
            talent_widget.combo_box.clear()
            talent_widget.combo_box.addItems(school.talents[i])

        for recipe_widget in recipes_widget.values():
            recipe_widget.list.clear()
            recipe_widget.hide()

        for i, (skill, recipes) in enumerate(school.recipes.items()):
            recipes_widget[i].label.setText(skill)
            recipes_widget[i].list.addItems(recipes)
            recipes_widget[i].show()

        combat_widget.prepare.text_browser.setText(school.prepare)
        combat_widget.priority.text_browser.setText(school.priority)
        combat_widget.loop.text_browser.setText(school.loop)
        if index >= 0:
            tab_widget.show()

    top_widget.school.combo_box.currentIndexChanged.connect(school_update)

    return school
