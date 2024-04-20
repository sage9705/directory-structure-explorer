import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit, QLineEdit

class DirectoryStructurePrinter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Directory Structure Printer")

        self.layout = QVBoxLayout()

        self.label = QLabel("Select a directory to print its structure:")
        self.layout.addWidget(self.label)

        self.select_button = QPushButton("Select Directory")
        self.select_button.clicked.connect(self.select_directory)
        self.layout.addWidget(self.select_button)

        self.exclude_label = QLabel("Enter subfolders to exclude (separated by comma):")
        self.layout.addWidget(self.exclude_label)

        self.exclude_lineedit = QLineEdit()
        self.layout.addWidget(self.exclude_lineedit)

        self.output_textedit = QTextEdit()
        self.output_textedit.setReadOnly(True)
        self.layout.addWidget(self.output_textedit)

        self.setLayout(self.layout)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            exclude_list = self.exclude_lineedit.text().split(',')
            self.print_directory_structure(directory, exclude_list)

    def print_directory_structure(self, directory, exclude_list):
        structure = self.get_directory_structure(directory, exclude_list)
        self.output_textedit.setPlainText(structure)

    def get_directory_structure(self, directory, exclude_list, indent=''):
        structure = indent + os.path.basename(directory) + '/\n'
        indent += '    '
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                if item not in exclude_list:
                    structure += self.get_directory_structure(item_path, exclude_list, indent)
            else:
                structure += indent + '├── ' + item + '\n'
        return structure

def main():
    app = QApplication(sys.argv)
    window = DirectoryStructurePrinter()
    window.resize(600, 400)  # Set initial size
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
