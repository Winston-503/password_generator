import sys
import string
import random
from PyQt5 import QtWidgets
from password_generator_form import Ui_MainWindow

class PasswordGenerator(QtWidgets.QMainWindow):
    def __init__(self):
        # Call parent constructor
        super(PasswordGenerator, self).__init__()
        self.password_generator_form = Ui_MainWindow()
        self.password_generator_form.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        # Event for click on button
        self.password_generator_form.pushButton.clicked.connect(self.generate)

    def generate(self):
        # Function of generating passwords
        use_numbers = self.password_generator_form.cb_use_numbers.isChecked()
        use_letters = self.password_generator_form.cb_use_letters.isChecked()
        use_punctuation = self.password_generator_form.cb_use_punctuation.isChecked()
        length_str = self.password_generator_form.le_length.text()
        count_str = self.password_generator_form.le_count.text()
        
        # Checking for input errors
        if (use_numbers or use_letters or use_punctuation) == False:
            self.password_generator_form.te_result.\
                setText("Не был выбран ни один из CheckBox")
            return
        if (not(length_str.isdigit()) or not(count_str.isdigit())):
            self.password_generator_form.te_result.\
                setText("Неверный ввод длины пароля или количества паролей - введены не числа")
            return
        length = int(length_str)
        count = int(count_str)
        if (length <= 0 or length > 100 or count <= 0 or count > 100):
            self.password_generator_form.te_result.\
                setText("Неверный ввод длины пароля или количества паролей - введены неверные числа")
            return
        
        password_characters = string.digits*use_numbers + \
            string.ascii_letters*use_letters + string.punctuation*use_punctuation
        passwords = ""
        for i in range(count):
            password = ''.join(random.choice(password_characters) for i in range(length))
            passwords += password + "\n"
        self.password_generator_form.te_result.setText(passwords)

app = QtWidgets.QApplication([])
application = PasswordGenerator()
application.show()
# Application operating cycle
sys.exit(app.exec())