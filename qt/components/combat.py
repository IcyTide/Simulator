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
        tab.addTab(attribute, "Attribute")

        self.init_attribute = TextWithLabel("Init Attribute")
        attribute_layout.addWidget(self.init_attribute)
        self.final_attribute = TextWithLabel("Final Attribute")
        attribute_layout.addWidget(self.final_attribute)

        detail = QWidget()
        detail_layout = QVBoxLayout()
        detail.setLayout(detail_layout)
        tab.addTab(detail, "Detail")

        self.origin_detail = TableWithLabel("Origin Detail", headers=["skill", "count", "hit", "critical", "damage"])
        detail_layout.addWidget(self.origin_detail)
        self.delta_detail = TableWithLabel("Delta Detail", headers=["skill", "count", "hit", "critical", "damage"])
        detail_layout.addWidget(self.delta_detail)
        self.delta_detail.hide()

        detail_layout.addStretch()

        sequences = QWidget()
        sequences_layout = QVBoxLayout()
        sequences.setLayout(sequences_layout)
        tab.addTab(sequences, "Sequences")

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
        result_layout.addWidget(self.origin_gradients, 7)
        self.delta_gradients = TextWithLabel("Delta Gradients")
        result_layout.addWidget(self.delta_gradients, 3)
        self.delta_gradients.hide()

        result_layout.addStretch()

        layout.addStretch()



