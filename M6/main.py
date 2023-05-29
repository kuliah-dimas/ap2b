import sys
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(300, 300, 300, 300)

        self.text_box = QLineEdit(self)
        self.text_box.setReadOnly(True)
        self.text_box.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.text_box.setFont(QtGui.QFont("Arial", 12))

        vbox = QVBoxLayout()
        vbox.addWidget(self.text_box)

        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "<-"],
        ]

        for row in self.buttons:
            hbox = QHBoxLayout()
            for label in row:
                button = QPushButton(label, self)
                button.clicked.connect(self.buttonClicked)
                hbox.addWidget(button)
            vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;
                border: 1px solid #CCCCCC;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
            QPushButton:pressed {
                background-color: #3E8E41;
            }
            QLineEdit {
                background-color: #000000;
                border: 1px solid #CCCCCC;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
            """
        )

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == "=":
            try:
                result = str(eval(self.text_box.text()))
                self.text_box.setText(result)
            except:
                self.text_box.setText("Error")
        elif key == "C":
            self.text_box.clear()
        elif key == "<-":
            text = self.text_box.text()[:-1]
            self.text_box.setText(text)
        else:
            self.text_box.setText(self.text_box.text() + key)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
