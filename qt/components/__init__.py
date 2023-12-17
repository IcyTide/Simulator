from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QAbstractItemView, QTableWidgetItem
from PySide6.QtWidgets import QComboBox, QRadioButton, QTextBrowser, QSpinBox, QListWidget, QTableWidget


class TableWithLabel(QWidget):
    def __init__(self, label, row_count: int = 0, column_count: int = 0, headers: list = None):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(label)
        self.table = QTableWidget()

        if row_count:
            self.table.setRowCount(row_count)
        if column_count:
            self.table.setColumnCount(column_count)
        if headers:
            self.table.setColumnCount(len(headers))
            self.table.setHorizontalHeaderLabels(headers)
        layout.addWidget(self.label)
        layout.addWidget(self.table)

    def set_content(self, content):
        self.table.setRowCount(len(content))

        for i, row in enumerate(content):
            for j, e in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(e))
        self.table.resizeColumnsToContents()


class ListWithLabel(QWidget):
    def __init__(self, label, items: list = None):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(label)
        self.list = QListWidget()
        self.list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        if items:
            self.list.addItems(items)
        layout.addWidget(self.label)
        layout.addWidget(self.list)


class ComboWithLabel(QWidget):
    def __init__(self, label, items: list = None, index=None):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(label)
        self.combo_box = QComboBox()
        if items:
            self.combo_box.addItems(items)
        if index:
            self.combo_box.setCurrentIndex(index)
        layout.addWidget(self.label)
        layout.addWidget(self.combo_box)


class RadioWithLabel(QWidget):
    def __init__(self, label):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(label)
        self.radio_button = QRadioButton()

        layout.addWidget(self.label)
        layout.addWidget(self.radio_button)


class SpinWithLabel(QWidget):
    def __init__(self, label, minimum=None, maximum=None, value=None):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(label)
        self.spin_box = QSpinBox()
        if minimum:
            self.spin_box.setMinimum(minimum)
        if maximum:
            self.spin_box.setMaximum(10e8)
        if value:
            self.spin_box.setValue(value)

        layout.addWidget(self.label)
        layout.addWidget(self.spin_box)


class TextWithLabel(QWidget):
    def __init__(self, label):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(label)
        self.text_browser = QTextBrowser()
        # self.text_browser.textChanged.connect(self.resize_height)

        layout.addWidget(self.label)
        layout.addWidget(self.text_browser)

    def resize_height(self):
        self.text_browser.setFixedHeight(self.text_browser.document().size().height())


class LabelWithLabel(QWidget):
    def __init__(self, label):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.label = QLabel(label)
        self.text = QLabel()
        # self.text_browser.textChanged.connect(self.resize_height)

        layout.addWidget(self.label)
        layout.addWidget(self.text)
