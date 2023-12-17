from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget

from qt.components import ComboWithLabel, SpinWithLabel, TextWithLabel, LabelWithLabel, TableWithLabel
from base.constant import SHIELD_BASE_MAP


class CombatWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.top = QWidget()
        top_layout = QHBoxLayout()
        self.top.setLayout(top_layout)
        layout.addWidget(self.top)

        self.target_level = ComboWithLabel("Target Level", [str(level) for level in SHIELD_BASE_MAP])
        top_layout.addWidget(self.target_level)
        self.duration = SpinWithLabel("Duration", minimum=1, maximum=3600, value=180)
        top_layout.addWidget(self.duration)
        self.iteration = SpinWithLabel("Iteration", minimum=1, maximum=1000000, value=1000)
        top_layout.addWidget(self.iteration)
        self.delta = SpinWithLabel("Delta Critical", maximum=10000)
        top_layout.addWidget(self.delta)

        self.button = QPushButton(text="Start Simulation!")
        layout.addWidget(self.button)

        self.bottom = QWidget()
        bottom_layout = QHBoxLayout()
        self.bottom.setLayout(bottom_layout)
        layout.addWidget(self.bottom)

        self.tab = QTabWidget()
        bottom_layout.addWidget(self.tab, 7)
        self.result = QWidget()
        result_layout = QVBoxLayout()
        self.result.setLayout(result_layout)
        bottom_layout.addWidget(self.result, 3)

        self.attribute = QWidget()
        attribute_layout = QHBoxLayout()
        self.attribute.setLayout(attribute_layout)
        self.tab.addTab(self.attribute, "Attribute")

        self.init_attribute = TextWithLabel("Init Attribute")
        attribute_layout.addWidget(self.init_attribute)
        self.final_attribute = TextWithLabel("Final Attribute")
        attribute_layout.addWidget(self.final_attribute)

        self.detail = QWidget()
        detail_layout = QVBoxLayout()
        self.detail.setLayout(detail_layout)
        self.tab.addTab(self.detail, "Detail")

        self.origin_detail = TableWithLabel("Origin Detail", headers=["skill", "count", "hit", "critical", "damage"])
        detail_layout.addWidget(self.origin_detail)
        self.delta_detail = TableWithLabel("Delta Detail", headers=["skill", "count", "hit", "critical", "damage"])
        detail_layout.addWidget(self.delta_detail)
        self.delta_detail.hide()

        detail_layout.addStretch()

        self.sequences = QWidget()
        sequences_layout = QVBoxLayout()
        self.sequences.setLayout(sequences_layout)
        self.tab.addTab(self.sequences, "Sequences")

        self.prepare = TextWithLabel("Prepare Sequences")
        sequences_layout.addWidget(self.prepare)
        self.priority = TextWithLabel("Priority Sequences")
        sequences_layout.addWidget(self.priority)
        self.loop = TextWithLabel("Loop Sequences")
        sequences_layout.addWidget(self.loop)

        sequences_layout.addStretch()

        self.origin_dps = LabelWithLabel("Origin DPS")
        result_layout.addWidget(self.origin_dps)
        self.delta_dps = LabelWithLabel("Delta DPS")
        result_layout.addWidget(self.delta_dps)
        self.delta_dps.hide()
        self.origin_gradients = TextWithLabel("Origin Gradients")
        result_layout.addWidget(self.origin_gradients)
        self.delta_gradients = TextWithLabel("Delta Gradients")
        result_layout.addWidget(self.delta_gradients)
        self.delta_gradients.hide()

        result_layout.addStretch()

        layout.addStretch()



