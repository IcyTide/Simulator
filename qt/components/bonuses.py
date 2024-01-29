from qt.components import ComboWithLabel, SpinWithLabel, RadioWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QTabWidget
from general.gains.team import TEAM_GAINS_NAME


class FormationWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.formation = ComboWithLabel("阵法")
        layout.addWidget(self.formation)
        self.core_rate = SpinWithLabel("四重覆盖率", maximum=100)
        layout.addWidget(self.core_rate)
        self.formation_rate = SpinWithLabel("五重覆盖率", maximum=100)
        layout.addWidget(self.formation_rate)


class TeamGainsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.team_gains = {}

        tabs = QTabWidget()
        layout.addWidget(tabs)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "七秀")

        self.team_gains["袖气"] = RadioWithLabel("袖气", TEAM_GAINS_NAME["袖气"])
        tab_layout.addWidget(self.team_gains["袖气"], 0, 0)

        self.team_gains["左旋右转"] = {
            "stack": SpinWithLabel(TEAM_GAINS_NAME["左旋右转"], "层数", maximum=133)
        }
        tab_layout.addWidget(self.team_gains["左旋右转"]["stack"], 1, 0)
        self.team_gains["泠风解怀"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["泠风解怀"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["泠风解怀"]["rate"], 2, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "天策")

        self.team_gains["撼如雷"] = RadioWithLabel("撼如雷", TEAM_GAINS_NAME["撼如雷"])
        tab_layout.addWidget(self.team_gains["撼如雷"], 0, 0)

        self.team_gains["破风"] = {
            "variety": ComboWithLabel("破风", items=["", TEAM_GAINS_NAME["破风"], TEAM_GAINS_NAME["劲风"]])
        }
        tab_layout.addWidget(self.team_gains["破风"]["variety"], 1, 0)

        self.team_gains["乘龙箭"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["乘龙箭"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["乘龙箭"]["rate"], 2, 0)

        self.team_gains["号令三军"] = {
            "stack": SpinWithLabel(TEAM_GAINS_NAME["号令三军"], "层数", maximum=48)
        }
        tab_layout.addWidget(self.team_gains["号令三军"]["stack"], 3, 0)

        self.team_gains["激雷"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["激雷"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["激雷"]["rate"], 4, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "少林")

        self.team_gains["立地成佛"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["立地成佛"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["立地成佛"]["rate"], 0, 0)

        self.team_gains["舍身弘法"] = {
            "stack": SpinWithLabel(TEAM_GAINS_NAME["舍身弘法"], "层数", maximum=36),
            "rate": SpinWithLabel(TEAM_GAINS_NAME["舍身弘法"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["舍身弘法"]["stack"], 1, 0)
        tab_layout.addWidget(self.team_gains["舍身弘法"]["rate"], 1, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "万花")

        self.team_gains["秋肃"] = RadioWithLabel("秋肃", TEAM_GAINS_NAME["秋肃"])
        tab_layout.addWidget(self.team_gains["秋肃"], 0, 0)

        self.team_gains["皎素"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["皎素"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["皎素"]["rate"], 1, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "纯阳")

        self.team_gains["碎星辰"] = RadioWithLabel("碎星辰", TEAM_GAINS_NAME["碎星辰"])
        tab_layout.addWidget(self.team_gains["碎星辰"], 0, 0)

        self.team_gains["破苍穹"] = RadioWithLabel("破苍穹", TEAM_GAINS_NAME["破苍穹"])
        tab_layout.addWidget(self.team_gains["破苍穹"], 1, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "藏剑")

        self.team_gains["剑锋百锻"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["剑锋百锻"], "覆盖", maximum=int(100 / 6))
        }
        tab_layout.addWidget(self.team_gains["剑锋百锻"]["rate"], 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "五毒")

        self.team_gains["善友"] = RadioWithLabel("善友", TEAM_GAINS_NAME["善友"])
        tab_layout.addWidget(self.team_gains["善友"], 0, 0)

        self.team_gains["仙王蛊鼎"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["仙王蛊鼎"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["仙王蛊鼎"]["rate"], 1, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "明教")

        self.team_gains["戒火"] = RadioWithLabel("戒火", TEAM_GAINS_NAME["戒火"])
        tab_layout.addWidget(self.team_gains["戒火"], 0, 0)

        self.team_gains["烈日"] = RadioWithLabel("烈日", TEAM_GAINS_NAME["烈日"])
        tab_layout.addWidget(self.team_gains["烈日"], 1, 0)

        self.team_gains["朝圣言"] = {
            "variety": ComboWithLabel("朝圣言", "类型", items=["", TEAM_GAINS_NAME["朝圣言"], TEAM_GAINS_NAME["圣浴明心"]]),
            "stack": SpinWithLabel("朝圣言", "层数", maximum=24),
            "rate": SpinWithLabel("朝圣言", "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["朝圣言"]["variety"], 2, 0)
        tab_layout.addWidget(self.team_gains["朝圣言"]["stack"], 2, 1)
        tab_layout.addWidget(self.team_gains["朝圣言"]["rate"], 2, 2)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "丐帮")

        self.team_gains["酒中仙"] = RadioWithLabel("酒中仙", TEAM_GAINS_NAME["酒中仙"])
        tab_layout.addWidget(self.team_gains["酒中仙"], 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "苍云")

        self.team_gains["虚弱"] = RadioWithLabel("虚弱", TEAM_GAINS_NAME["虚弱"])
        tab_layout.addWidget(self.team_gains["虚弱"], 0, 0)

        self.team_gains["寒啸千军"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["寒啸千军"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["寒啸千军"]["rate"], 1, 0)

        self.team_gains["振奋"] = {
            "stack": SpinWithLabel(TEAM_GAINS_NAME["振奋"], "层数"),
            "rate": SpinWithLabel(TEAM_GAINS_NAME["振奋"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["振奋"]["stack"], 2, 0)
        tab_layout.addWidget(self.team_gains["振奋"]["rate"], 2, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "长歌")

        self.team_gains["庄周梦"] = {
            "stack": SpinWithLabel(TEAM_GAINS_NAME["庄周梦"], "层数", maximum=133),
            "rate": SpinWithLabel(TEAM_GAINS_NAME["庄周梦"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["庄周梦"]["stack"], 0, 0)
        tab_layout.addWidget(self.team_gains["庄周梦"]["rate"], 0, 1)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "霸刀")

        self.team_gains["疏狂"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["疏狂"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["疏狂"]["rate"], 0, 0)

        tab = QWidget()
        tab_layout = QGridLayout(tab)
        tabs.addTab(tab, "药宗")

        self.team_gains["飘黄"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["飘黄"], "覆盖", maximum=int(100 / 6))
        }
        tab_layout.addWidget(self.team_gains["飘黄"]["rate"], 0, 0)

        self.team_gains["配伍"] = {
            "rate": SpinWithLabel(TEAM_GAINS_NAME["配伍"], "覆盖", maximum=100)
        }
        tab_layout.addWidget(self.team_gains["配伍"]["rate"], 1, 0)

        layout.addStretch()

    def __getitem__(self, item):
        return self.team_gains[item]

    def items(self):
        return self.team_gains.items()


class BonusesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.tab = QTabWidget()
        layout.addWidget(self.tab)
        self.formation = FormationWidget()
        self.tab.addTab(self.formation, "阵法")
        self.team_gains = TeamGainsWidget()
        self.tab.addTab(self.team_gains, "团队增益")

        layout.addStretch()
