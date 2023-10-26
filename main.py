import sys
from PyQt5.QtWidgets import QApplication,QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont
from utils.functions import on_operation_button_clicked

class MathMateGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set the main layout
        self.main_layout = QHBoxLayout(self)

        # Create a vertical layout for the input area, buttons, and result
        self.input_buttons_result_layout = QVBoxLayout()
        self.main_layout.addLayout(self.input_buttons_result_layout,5)  # 70% of the width

        # Add the input area
        self.input_area = QLineEdit(self)
        self.input_area.setFont(QFont('Arial', 16))
        self.input_buttons_result_layout.addWidget(self.input_area)

        # Add operation buttons
        self.add_operation_buttons()

        # Add result display
        self.result_display = QLabel('Result: ', self)
        self.result_display.setFont(QFont('Arial', 16))
        self.input_buttons_result_layout.addWidget(self.result_display)

        # Create description section
        self.description_text = QTextEdit(self)
        self.description_text.setFont(QFont('Arial', 16))
        self.main_layout.addWidget(self.description_text,5)  # 30% of the width
        self.description_text.setPlaceholderText("Select an operation to see its description and example.")

        # Set the window properties
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle('MathMate')
        self.show()

    def add_operation_buttons(self):
        # Container for operation buttons in a vertical layout
        operation_layout = QVBoxLayout()

        # List of operation buttons
        operations = ['+', '-', '*', '/', 'sin', 'cos', 'tan', 'sqrt', '^', '%']
        for op in operations:
            button = QPushButton(op, self)
            button.setFont(QFont('Arial', 16))
            button.clicked.connect(self.handle_button_click)
            operation_layout.addWidget(button)

        # Add the operation buttons layout to the input_buttons_result_layout
        self.input_buttons_result_layout.addLayout(operation_layout)

    def handle_button_click(self):

        button = self.sender()
        if button:
            on_operation_button_clicked(self, button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MathMateGUI()
    sys.exit(app.exec_())
