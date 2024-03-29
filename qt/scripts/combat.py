from PySide6.QtWidgets import QMessageBox

from base.simulator import Simulator
from base.target import Target
from general.buffs import BUFFS
from general.skills import SKILLS

from qt.components.combat import CombatWidget
from qt.constant import ATTR_TYPE_TRANSLATE
from qt.scripts.top import School
from qt.scripts.equipments import Equipments
from qt.scripts.consumables import Consumables
from qt.scripts.bonuses import Bonuses
from qt.scripts.recipes import Recipes
from qt.scripts.talents import Talents
from utils.simulate import simulate_delta


def detail_content(details):
    total_damage = sum([detail['damage'] for detail in details.values()])
    content = []
    for skill, detail in details.items():
        count = round(detail['hit'] + detail['critical'], 2)
        content.append([
            skill, str(count),
            f"{detail['hit']}/{round(detail['hit'] / count * 100, 2)}%",
            f"{detail['critical']}/{round(detail['critical'] / count * 100, 2)}%",
            f"{detail['damage']}/{round(detail['damage'] / total_damage * 100, 2)}%"
        ])
    return content


def gradients_text(gradients):
    gradients_texts = [f"{ATTR_TYPE_TRANSLATE[k]}:\t{round(v[0], 2)}/{round(v[1], 4)}" for k, v in gradients.items()]
    return "\n".join(gradients_texts)


def combat_script(message_box: QMessageBox, school: School,
                  equipments: Equipments, talents: Talents, recipes: Recipes,
                  consumables: Consumables, bonuses: Bonuses,
                  combat_widget: CombatWidget):

    def simulate():
        target_level = int(combat_widget.target_level.combo_box.currentText())
        duration = combat_widget.duration.spin_box.value()
        gap = combat_widget.gap.spin_box.value()
        prepare = combat_widget.prepare.text_browser.toPlainText()
        priority = combat_widget.priority.text_browser.toPlainText()
        loop = combat_widget.loop.text_browser.toPlainText()

        attribute = school.attribute()
        for attr, value in equipments.attrs.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        for attr, value in consumables.attrs.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        setattr(attribute, "primary_weapon_attribute", equipments.primary_weapon_attrs)
        setattr(attribute, "secondary_weapon_attribute", equipments.secondary_weapon_attrs)

        combat_widget.init_attribute.set_text(school.attr_text(attribute))
        gains = sum([equipments.gains, talents.gains, recipes.gains, bonuses.gains], [])

        try:
            simulator = Simulator(attribute, SKILLS[school.kind] + school.skills, BUFFS[school.kind] + school.buffs,
                                  gains, Target(target_level), duration, prepare, priority, loop, school.initiation,
                                  gap, verbose=False)
        except SyntaxError as e:
            message_box.setWindowTitle("序列语法错误")
            message_box.setText(e.msg)
            message_box.exec()
            return

        combat_widget.final_attribute.set_text(school.attr_text(attribute))

        iteration = combat_widget.iteration.spin_box.value()
        delta = combat_widget.delta.spin_box.value()

        cost, summary, dps, details, gradients, delta_dps, delta_details, delta_gradients = simulate_delta(
            iteration, simulator, delta
        )
        message_box.setWindowTitle("模拟完成")
        message_box.setText(f"完成{iteration}次模拟消耗{cost}秒")
        message_box.exec()

        combat_widget.summary.set_content(summary)
        combat_widget.origin_dps.text.setText(str(int(dps)))
        combat_widget.origin_detail.set_content(detail_content(details))
        combat_widget.origin_gradients.text_browser.setText(gradients_text(gradients))

        combat_widget.delta_dps.text.setText(str(int(delta_dps)))
        combat_widget.delta_detail.set_content(detail_content(delta_details))
        combat_widget.delta_gradients.text_browser.setText(gradients_text(delta_gradients))

    combat_widget.button.clicked.connect(simulate)
