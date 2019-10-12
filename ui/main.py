import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PySide2.QtGui import QPixmap


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Form")
        self.identifier = QLineEdit('Your login')
        self.pwd = QLineEdit("Put you password")
        self.pwd.setEchoMode(QLineEdit.Password)
        self.button = QPushButton("show Greetings")
        image = QPixmap("toto.jpg")
        label = QLabel(self)
        label.setPixmap(image)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.identifier)
        layout.addWidget(self.pwd)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)


    def greetings(self):
        print("Hello {}".format(self.identifier.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
