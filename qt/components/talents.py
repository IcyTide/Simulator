from qt.components import ComboWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from qt.constant import MAX_TALENTS


class TalentsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.talents_row1 = QWidget()
        row1_layout = QHBoxLayout()
        self.talents_row1.setLayout(row1_layout)
        layout.addWidget(self.talents_row1)

        self.talents_row2 = QWidget()
        row2_layout = QHBoxLayout()
        self.talents_row2.setLayout(row2_layout)
        layout.addWidget(self.talents_row2)

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
