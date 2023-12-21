from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget

from qt.components import ComboWithLabel, SpinWithLabel, TextWithLabel, LabelWithLabel, TableWithLabel
from base.constant import SHIELD_BASE_MAP


class CombatWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        top = QWidget()
        top_layout = QHBoxLayout()
        top.setLayout(top_layout)
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
        bottom_layout = QHBoxLayout()
        bottom.setLayout(bottom_layout)
        layout.addWidget(bottom)

        tab = QTabWidget()
        bottom_layout.addWidget(tab, 7)
        result = QWidget()
        result_layout = QVBoxLayout()
        result.setLayout(result_layout)
        bottom_layout.addWidget(result, 3)

        attribute = QWidget()
        attribute_layout = QHBoxLayout()
        attribute.setLayout(attribute_layout)
        tab.addTab(attribute, "属性")

        self.init_attribute = TextWithLabel("增益前属性")
        attribute_layout.addWidget(self.init_attribute)
        self.final_attribute = TextWithLabel("增益后属性")
        attribute_layout.addWidget(self.final_attribute)

        detail = QWidget()
        detail_layout = QVBoxLayout()
        detail.setLayout(detail_layout)
        tab.addTab(detail, "战斗总结")

        self.origin_detail = TableWithLabel("伤害详情", headers=["技能", "次数", "命中/%", "会心/%", "伤害/%"])
        detail_layout.addWidget(self.origin_detail)
        self.delta_detail = TableWithLabel("残差伤害详情", headers=["技能", "次数", "命中/%", "会心/%", "伤害/%"])
        detail_layout.addWidget(self.delta_detail)
        self.delta_detail.hide()

        detail_layout.addStretch()

        sequences = QWidget()
        sequences_layout = QVBoxLayout()
        sequences.setLayout(sequences_layout)
        tab.addTab(sequences, "序列设置")

        self.prepare = TextWithLabel("预备序列")
        sequences_layout.addWidget(self.prepare)
        self.priority = TextWithLabel("优先序列")
        sequences_layout.addWidget(self.priority)
        self.loop = TextWithLabel("循环序列")
        sequences_layout.addWidget(self.loop)

        sequences_layout.addStretch()

        self.origin_dps = LabelWithLabel("DPS")
        result_layout.addWidget(self.origin_dps)
        self.delta_dps = LabelWithLabel("残差DPS")
        result_layout.addWidget(self.delta_dps)
        self.delta_dps.hide()

        self.origin_gradients = TextWithLabel("属性收益")
        result_layout.addWidget(self.origin_gradients, 7)
        self.delta_gradients = TextWithLabel("残差属性收益")
        result_layout.addWidget(self.delta_gradients, 3)
        self.delta_gradients.hide()

        result_layout.addStretch()

        layout.addStretch()



