# DIMAS FEBRIYANTO
# 1IA24
# 50422430

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QColor, QPalette, QPainter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt Clock")
        self.setGeometry(100, 100, 250, 150)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)
        self.lcd.setStyleSheet(
            "QLCDNumber { background-color: black; color: green; }")
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setFixedSize(250, 100)

        self.font = QFont('Arial', 48, QFont.Bold)
        self.palette = QPalette()
        self.palette.setColor(QPalette.WindowText, QColor(0, 255, 0))

        self.layout.addWidget(self.lcd)
        self.layout.setAlignment(Qt.AlignCenter)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

    def showTime(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.lcd.display(current_time)
        self.lcd.setFont(self.font)
        self.lcd.setPalette(self.palette)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        gradient = QColor(0, 0, 0)
        gradient.setAlpha(200)
        painter.setPen(Qt.NoPen)
        painter.setBrush(gradient)
        painter.drawRect(self.rect())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
