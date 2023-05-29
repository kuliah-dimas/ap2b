import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt
import requests
import webbrowser
from flask import Flask
from flask_restful import Api, Resource


class FileUploaderWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('File Uploader')
        self.setGeometry(100, 100, 300, 150)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)

        self.file_label = QLabel('No file selected', self)
        layout.addWidget(self.file_label)

        select_button = QPushButton('Select File', self)
        select_button.clicked.connect(self.select_file)
        layout.addWidget(select_button)

        upload_button = QPushButton('Upload', self)
        upload_button.clicked.connect(self.upload_file)
        layout.addWidget(upload_button)

        open_web_button = QPushButton('Open File in Web', self)
        open_web_button.clicked.connect(self.open_web_file)
        layout.addWidget(open_web_button)

        self.uploaded_file_path = None

        self.setStyleSheet('''
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 14px;
            }
            QPushButton {
                font-size: 14px;
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #367d39;
            }
        ''')

    def select_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('PDF files (*.pdf)')
        if file_dialog.exec_():
            self.uploaded_file_path = file_dialog.selectedFiles()[0]
            self.file_label.setText(self.uploaded_file_path)

    def upload_file(self):
        if self.uploaded_file_path:
            try:
                files = {'file': open(self.uploaded_file_path, 'rb')}
                response = requests.post(
                    'http://127.0.0.1:5000/upload', files=files)
                if response.status_code == 200:
                    QMessageBox.information(
                        self, 'Success', 'File uploaded successfully')
                    self.file_label.setText('No file selected')
                else:
                    QMessageBox.critical(
                        self, 'Error', 'Failed to upload file')
            except requests.exceptions.RequestException:
                QMessageBox.critical(
                    self, 'Error', 'Failed to connect to the server')
        else:
            QMessageBox.warning(
                self, 'Warning', 'Please select a file to upload')

    def open_web_file(self):
        if self.uploaded_file_path:
            file_name = self.uploaded_file_path.split('/')[-1]
            web_url = f"http://127.0.0.1:5000/uploads/{file_name}"
            webbrowser.open(web_url)
        else:
            QMessageBox.warning(self, 'Warning', 'Please upload a file first')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileUploaderWindow()
    window.show()
    sys.exit(app.exec())
