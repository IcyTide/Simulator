from qt.components import ComboWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from qt.constant import MAX_TALENTS


class TalentsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        row1 = QWidget()
        row1_layout = QHBoxLayout()
        row1.setLayout(row1_layout)
        layout.addWidget(row1)

        row2 = QWidget()
        row2_layout = QHBoxLayout()
        row2.setLayout(row2_layout)
        layout.addWidget(row2)

        layout.addStretch()

        self.talents = []
        for i in range(MAX_TALENTS // 2):
            talent = ComboWithLabel(f"Talent {i + 1}")
            self.talents.append(talent)
            row1_layout.addWidget(talent)
        for i in range(MAX_TALENTS // 2, MAX_TALENTS):
            talent = ComboWithLabel(f"Talent {i + 1}")
            self.talents.append(talent)
            row2_layout.addWidget(talent)

    def __getitem__(self, item) -> ComboWithLabel:
        return self.talents[item]

    def values(self):
        return self.talents
