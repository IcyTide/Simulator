from general.gains.formation import FORMATION_GAINS
from general.gains.team import TEAM_GAINS

from qt.components import RadioWithLabel, ComboWithLabel, SpinWithLabel
from qt.components.bonuses import BonusesWidget
from qt.scripts.top import School


class Bonuses(dict):
    @property
    def gains(self):
        return list(self.values())


def bonuses_script(school: School, bonuses_widget: BonusesWidget):
    bonuses = Bonuses()

    def formation_update(arg):
        widget = bonuses_widget.formation
        formation = widget.formation.combo_box.currentText()
        core_rate = widget.core_rate.spin_box.value()
        formation_rate = widget.formation_rate.spin_box.value()

        if formation == school.formation:
            widget.core_rate.show()
        else:
            core_rate = 0
            widget.core_rate.hide()

        if formation:
            bonuses['formation'] = FORMATION_GAINS[formation](formation_rate, core_rate)
        else:
            bonuses.pop("formation", None)

    bonuses_widget.formation.formation.combo_box.currentIndexChanged.connect(formation_update)
    bonuses_widget.formation.core_rate.spin_box.valueChanged.connect(formation_update)
    bonuses_widget.formation.formation_rate.spin_box.valueChanged.connect(formation_update)

    def radio_update(label):
        widget = bonuses_widget.team_gains[label]

        def inner():
            if widget.radio_button.isChecked():
                bonuses[label] = TEAM_GAINS[label]
            else:
                bonuses.pop(label, None)

        return inner

    def combine_update(label):
        widgets = bonuses_widget.team_gains[label]

        def inner(arg):
            args = []
            for widget in widgets.values():
                if isinstance(widget, ComboWithLabel):
                    args.append(widget.combo_box.currentText())
                elif isinstance(widget, SpinWithLabel):
                    args.append(widget.spin_box.value())
            if all(args):
                bonuses[label] = TEAM_GAINS[label](*args)
            else:
                bonuses.pop(label, None)

        return inner

    for bonus_label, bonus_widget in bonuses_widget.team_gains.items():
        if isinstance(bonus_widget, RadioWithLabel):
            bonus_widget.radio_button.clicked.connect(radio_update(bonus_label))
        elif isinstance(bonus_widget, dict):
            for sub_bonus_widget in bonus_widget.values():
                if isinstance(sub_bonus_widget, ComboWithLabel):
                    sub_bonus_widget.combo_box.currentIndexChanged.connect(combine_update(bonus_label))
                elif isinstance(sub_bonus_widget, SpinWithLabel):
                    sub_bonus_widget.spin_box.valueChanged.connect(combine_update(bonus_label))
                else:
                    raise TypeError
        else:
            raise TypeError

    return bonuses
