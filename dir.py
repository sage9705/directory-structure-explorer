import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit, QLineEdit, QCheckBox, QProgressBar
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt, QSize, QThread, pyqtSignal

class Worker(QThread):
    progress_updated = pyqtSignal(int)
    structure_generated = pyqtSignal(str)

    def __init__(self, directory, exclude_list, include_subdirs):
        super().__init__()
        self.directory = directory
        self.exclude_list = exclude_list
        self.include_subdirs = include_subdirs

    def run(self):
        structure = self.get_directory_structure(self.directory, self.exclude_list, self.include_subdirs)
        self.structure_generated.emit(structure)

    def get_directory_structure(self, directory, exclude_list, include_subdirs, indent='', last=True, progress=0):
        items = os.listdir(directory)
        items = [item for item in items if item not in exclude_list]
        items = sorted(items)

        structure = indent + ('└── ' if last else '├── ') + os.path.basename(directory) + '/\n'
        indent += '    ' if last else '│   '

        total_items = len(items)
        for i, item in enumerate(items):
            item_path = os.path.join(directory, item)
            is_last = i == total_items - 1
            if os.path.isdir(item_path):
                if include_subdirs:
                    structure += self.get_directory_structure(item_path, exclude_list, include_subdirs, indent, is_last, progress + (1 / total_items) * 100)
                else:
                    structure += indent + ('└── ' if is_last else '├── ') + item + '/\n'
            else:
                structure += indent + ('└── ' if is_last else '├── ') + item + '\n'

            self.progress_updated.emit(int(progress + (1 / total_items) * 100))

        return structure

class DirectoryStructurePrinter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Directory Structure Printer")
        self.setWindowIcon(QIcon("icon.png"))

        with open("style.css", "r") as f:
            self.setStyleSheet(f.read())

        self.layout = QVBoxLayout()

        self.top_layout = QHBoxLayout()
        self.label = QLabel("Select a directory to print its structure:")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.top_layout.addWidget(self.label)
        self.top_layout.addStretch()

        self.select_button = QPushButton("Select Directory")
        self.select_button.setIcon(QIcon("folder.png"))
        self.select_button.setIconSize(QSize(24, 24))
        self.select_button.clicked.connect(self.select_directory)
        self.top_layout.addWidget(self.select_button)

        self.layout.addLayout(self.top_layout)

        self.exclude_layout = QHBoxLayout()
        self.exclude_label = QLabel("Enter subfolders to exclude (separated by comma):")
        self.exclude_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.exclude_layout.addWidget(self.exclude_label)
        self.exclude_layout.addStretch()

        self.exclude_lineedit = QLineEdit()
        self.exclude_lineedit.setPlaceholderText("Enter subfolders...")
        self.exclude_layout.addWidget(self.exclude_lineedit)

        self.layout.addLayout(self.exclude_layout)

        self.include_subdirs_checkbox = QCheckBox("Include subdirectories")
        self.include_subdirs_checkbox.setChecked(True)
        self.layout.addWidget(self.include_subdirs_checkbox)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setFont(QFont('Montserrat', 12))
        self.progress_bar.setVisible(False)  # Initially hide the progress bar

        self.output_layout = QVBoxLayout()
        self.output_label = QLabel("Directory Structure:")
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.output_layout.addWidget(self.output_label)

        self.output_textedit = QTextEdit()
        self.output_textedit.setReadOnly(True)
        self.output_layout.addWidget(self.output_textedit)

        self.layout.addWidget(self.progress_bar)
        self.layout.addLayout(self.output_layout)

        self.setLayout(self.layout)

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            exclude_list = self.exclude_lineedit.text().split(',')
            include_subdirs = self.include_subdirs_checkbox.isChecked()
            self.worker = Worker(directory, exclude_list, include_subdirs)
            self.worker.progress_updated.connect(self.update_progress_bar)
            self.worker.structure_generated.connect(self.display_structure)
            self.worker.finished.connect(self.hide_progress_bar)
            self.worker.start()
            self.show_progress_bar()

    def update_progress_bar(self, progress):
        self.progress_bar.setValue(progress)

    def display_structure(self, structure):
        self.output_textedit.setPlainText(structure)

    def show_progress_bar(self):
        self.progress_bar.setVisible(True)

    def hide_progress_bar(self):
        self.progress_bar.setVisible(False)

def main():
    app = QApplication(sys.argv)
    app.setFont(QFont('Montserrat', 16))
    window = DirectoryStructurePrinter()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
