import sys
from PyQt5.QtWidgets import QTabWidget, QTextBrowser, QApplication, QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont, QIcon
from utils.functions import on_operation_button_clicked, handle_equals_button_click
from PyQt5.QtCore import Qt
import json

class MathMateGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.load_tutorial_info()

        self.init_ui()

    def init_ui(self):
        # Set the main layout
        self.main_layout = QHBoxLayout(self)

        # Add tab widget
        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs, 5)  # 70% of the width

        # Create tab for operations
        self.operations_tab = QWidget()
        self.tabs.addTab(self.operations_tab, "Operations")
        self.operations_layout = QVBoxLayout(self.operations_tab)

        # Create tab for functions
        self.functions_tab = QWidget()
        self.tabs.addTab(self.functions_tab, "Functions")
        self.functions_layout = QVBoxLayout(self.functions_tab)

        # Add the input area to operations tab
        self.input_area = QLineEdit(self)
        self.input_area.setFont(QFont('Arial', 16))
        self.input_area.setFixedHeight(40)  # Set the height as per your preference
        self.input_area.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # Align text to right and center
        self.operations_layout.addWidget(self.input_area)

        # Add operation buttons to the operations tab
        self.add_operation_buttons()

        # Add result display to operations tab
        self.result_display = QLabel('Result: ', self)
        self.result_display.setFont(QFont('Arial', 16))
        self.result_display.setStyleSheet("QLabel { color : teal; border: 1px solid black; padding: 5px; }")
        self.result_display.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.operations_layout.addWidget(self.result_display)

        # Create description section
        # Create description section
        self.description_text = QTextBrowser(self)  # Changed from QLabel to QTextBrowser
        self.description_text.setFont(QFont('Arial', 16))
        self.description_text.setOpenExternalLinks(True)  # Allow opening links in the description
        self.main_layout.addWidget(self.description_text, 4)  # Changed from 5 to 2 to reduce size

        self.description_text.setOpenExternalLinks(True)  # Allow opening links in the description
        self.description_text.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Set the window properties
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle('MathMate: A Comprehensive Mathematical Utility')
        self.setWindowIcon(QIcon('logo.png'))  # Set the window icon
        self.show()

    def add_operation_buttons(self):
        # Container for operation buttons in a vertical layout
        operation_layout = QHBoxLayout()

        # List of operation buttons
        operations = ['+', '-', '*', '/', 'sin', 'cos', 'tan', 'sqrt', '^', '%']
        for op in operations:
            button = QPushButton(op, self)
            button.setFont(QFont('Arial', 16))
            button.clicked.connect(self.handle_button_click)
            operation_layout.addWidget(button)

        # Add the equal button
        equals_button = QPushButton('=', self)
        equals_button.setFont(QFont('Arial', 16))
        equals_button.setStyleSheet("background-color: grey")
        equals_button.clicked.connect(self.handle_equal_click)
        operation_layout.addWidget(equals_button)

        self.operations_layout.addLayout(operation_layout)  # Corrected to add to operations_layout

    def handle_button_click(self):
        button = self.sender()
        if button:
            button_text = button.text()
            operation_name = self.get_operation_name(button_text)
            if operation_name in self.tutorial_info:
                info = self.tutorial_info[operation_name]

                # Specify the path to your images folder
                image_folder_path = "images"

                # Construct the path to the image file
                image_path = f"{image_folder_path}/{operation_name}.png"

                # Set the content of the description text box with image and text
                self.description_text.setText(f"""
                    <div style="text-align:center;">
                        <img src="{image_path}" width="300" height="300" style="margin-bottom:10px;" />
                    </div>
                    <div>
                        <p>{info['symbol']} {info['explanation']}</p>
                    </div>
                """)

            else:
                self.description_text.setPlainText("No additional information available.")

            current_text = self.input_area.text()
            new_text = current_text + button_text
            self.input_area.setText(new_text)
            on_operation_button_clicked(self, button)

    def handle_equal_click(self):
        button = self.sender()
        if button:
            handle_equals_button_click(self, button)

    def load_tutorial_info(self):
        with open('tuto.json', 'r') as f:
            self.tutorial_info = json.load(f)

    def get_operation_name(self, button_text):
        operation_mapping = {
            '+': 'addition',
            '-': 'subtraction',
            '*': 'multiplication',
            '/': 'division',
            '^': 'power',
            'sqrt': 'square_root',
            '%': 'modulo',
            'sin': 'sine',
            'cos': 'cosine',
            'tan': 'tangent'
        }
        return operation_mapping.get(button_text, '')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MathMateGUI()
    sys.exit(app.exec_())
