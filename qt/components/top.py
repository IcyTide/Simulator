from PySide6.QtWidgets import QWidget, QVBoxLayout
from qt.components import ComboWithLabel
from qt.constant import SUPPORT_SCHOOL


class TopWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.school = ComboWithLabel("School", list(SUPPORT_SCHOOL), -1)

        layout.addWidget(self.school)
