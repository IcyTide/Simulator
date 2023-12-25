from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget

from qt.components import ComboWithLabel, SpinWithLabel, TextWithLabel, LabelWithLabel, TableWithLabel
from base.constant import SHIELD_BASE_MAP


class CombatWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        top = QWidget()
        top_layout = QHBoxLayout(top)
        layout.addWidget(top)

        self.target_level = ComboWithLabel("目标等级", items=[str(level) for level in SHIELD_BASE_MAP])
        top_layout.addWidget(self.target_level)
        self.duration = SpinWithLabel("战斗时长", maximum=3600, value=180)
        top_layout.addWidget(self.duration)
        self.iteration = SpinWithLabel("模拟次数", value=1000)
        top_layout.addWidget(self.iteration)
        self.delta = SpinWithLabel("会心残差", maximum=1000)
        top_layout.addWidget(self.delta)

        self.button = QPushButton(text="开始模拟!")
        layout.addWidget(self.button)

        bottom = QWidget()
        bottom_layout = QHBoxLayout(bottom)
        layout.addWidget(bottom)

        tab = QTabWidget()
        bottom_layout.addWidget(tab, 2)
        result = QWidget()
        result_layout = QVBoxLayout(result)
        bottom_layout.addWidget(result, 1)

        attribute = QWidget()
        attribute_layout = QHBoxLayout(attribute)
        tab.addTab(attribute, "属性")

        self.init_attribute = TextWithLabel("增益前属性", stretch=False)
        attribute_layout.addWidget(self.init_attribute)
        self.final_attribute = TextWithLabel("增益后属性", stretch=False)
        attribute_layout.addWidget(self.final_attribute)

        detail = QWidget()
        detail_layout = QVBoxLayout()
        detail.setLayout(detail_layout)
        tab.addTab(detail, "战斗详情")

        detail_tab = QTabWidget()
        detail_layout.addWidget(detail_tab)
        self.origin_detail = TableWithLabel("伤害详情", headers=["技能", "次数", "命中/%", "会心/%", "伤害/%"])
        detail_tab.addTab(self.origin_detail, "伤害详情")
        self.delta_detail = TableWithLabel("残差伤害详情", headers=["技能", "次数", "命中/%", "会心/%", "伤害/%"])
        detail_tab.addTab(self.delta_detail, "残差伤害详情")

        detail_layout.addStretch()

        self.summary = TableWithLabel("技能统计", headers=["技能", "等级", "次数", "增益"])

        tab.addTab(self.summary, "技能总结")

        sequences = QWidget()
        sequences_layout = QVBoxLayout(sequences)
        tab.addTab(sequences, "序列设置")

        sequences_tab = QTabWidget()
        sequences_layout.addWidget(sequences_tab)
        self.prepare = TextWithLabel("预备序列", editable=True)
        sequences_tab.addTab(self.prepare, "预备序列")
        self.priority = TextWithLabel("优先序列", editable=True)
        sequences_tab.addTab(self.priority, "优先序列")
        self.loop = TextWithLabel("循环序列", editable=True)
        sequences_tab.addTab(self.loop, "循环序列")

        self.origin_dps = LabelWithLabel("每秒伤害")
        result_layout.addWidget(self.origin_dps)
        self.delta_dps = LabelWithLabel("残差每秒伤害")
        result_layout.addWidget(self.delta_dps)

        gradients_tab = QTabWidget()
        self.origin_gradients = TextWithLabel("属性收益")
        gradients_tab.addTab(self.origin_gradients, "属性收益")
        self.delta_gradients = TextWithLabel("残差属性收益")
        gradients_tab.addTab(self.delta_gradients, "残差属性收益")

        result_layout.addWidget(gradients_tab)

        result_layout.addStretch()

        layout.addStretch()



