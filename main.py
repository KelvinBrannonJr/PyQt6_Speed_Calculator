from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox

import sys


# Speed class declaration
class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance[miles]")
        self.distance_edit_box = QLineEdit()

        self.select_conversion = QComboBox()
        self.select_conversion.addItems(['Miles', 'Kilometers'])

        duration_label = QLabel("Times[hours]")
        self.duration_edit_box = QLineEdit()

        calculate_btn = QPushButton("Calculate")
        calculate_btn.clicked.connect(self.calculate_speed)

        exit_btn = QPushButton("Exit")
        exit_btn.clicked.connect(self.close_app)

        self.output_label = QLabel("")

        # Grid layout
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_edit_box, 0, 1)
        grid.addWidget(self.select_conversion, 0, 2)
        grid.addWidget(duration_label, 1, 0)
        grid.addWidget(self.duration_edit_box, 1, 1)
        grid.addWidget(calculate_btn, 2, 0)
        grid.addWidget(exit_btn, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_edit_box.text())
        time = float(self.duration_edit_box.text())
        speed = distance / time

        if self.select_conversion.currentText() == 'Miles)':
            speed = round(speed * 0.621371, 2)

        if self.select_conversion.currentText() == 'kilometers)':
            speed = round(speed, 2)

        self.output_label.setText(f"Average Speed: {speed} {self.select_conversion.currentText()}")

    def close_app(self):
        print("Closing application")
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    speed_calculator = SpeedCalculator()
    speed_calculator.show()
    sys.exit(app.exec())

