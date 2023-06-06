from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox

import sys


# Speed class declaration
class SpeedCalculator(QWidget):
    def __init__(self):
        # Overwrite parent class QWidget __init__() method
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Distance label and box
        distance_label = QLabel("Distance[miles]")
        self.distance_edit_box = QLineEdit()

        # Select measurement ComboBox
        self.select_conversion = QComboBox()
        self.select_conversion.addItems(['Miles', 'Kilometers'])

        # Time in hours
        duration_label = QLabel("Times[hours]")
        self.duration_edit_box = QLineEdit()

        # Calculate btn
        calculate_btn = QPushButton("Calculate")
        calculate_btn.clicked.connect(self.calculate_speed)

        # Exit btn
        exit_btn = QPushButton("Exit")
        exit_btn.clicked.connect(self.close_app)

        # Output label
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

        # Instantiate layout as grid object
        self.setLayout(grid)

    # Calculate speed
    def calculate_speed(self):
        distance = float(self.distance_edit_box.text())
        time = float(self.duration_edit_box.text())
        speed = distance / time

        # Conversion for MPH
        if self.select_conversion.currentText() == 'Miles)':
            speed = round(speed * 0.621371, 2)

        # Conversion for KMH
        if self.select_conversion.currentText() == 'kilometers)':
            speed = round(speed, 2)

        # Output result to label
        self.output_label.setText(f"Average Speed: {speed} {self.select_conversion.currentText()}")

    # Close App method for 'EXIT' button
    def close_app(self):
        print("Closing application")
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    speed_calculator = SpeedCalculator()
    speed_calculator.show()
    sys.exit(app.exec())

