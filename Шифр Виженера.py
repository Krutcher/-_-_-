import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна
from itertools import cycle

class WindowApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setWindowTitle("Шифр Виженера")
        self.setupUi(self)

        self.pushButton.clicked.connect(self.b1_clicked)
        self.pushButton_2.clicked.connect(self.b2_clicked)

    def b1_clicked(self):
        key = self.textEdit_2.toPlainText().replace(' ', '').lower()
        text = self.textEdit_3.toPlainText().replace(' ', '').lower()
        self.textEdit_4.setText(encode_vijn(text, key))

    def b2_clicked(self):
        key = self.textEdit_2.toPlainText().replace(' ', '').lower()
        text = self.textEdit_4.toPlainText().replace(' ', '').lower()
        self.textEdit_3.setText(decode_vijn(text, key))

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = WindowApp()  # Создаём объект класса WindowApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение

    text = 'iwanttobelieve'
    key = 'potato'

    e = encode_vijn(text, key)
    print(e)
    print(decode_vijn(e, key))

alp = 'abcdefghijklmnopqrstuvwxyz'

def encode_vijn(text, key):
    f = lambda arg: alp[(alp.index(arg[0])+alp.index(arg[1])%26)%26]
    return ''.join(map(f, zip(text, cycle(key))))


def decode_vijn(coded_text, key):
    f = lambda arg: alp[alp.index(arg[0])-alp.index(arg[1])%26]
    return ''.join(map(f, zip(coded_text, cycle(key))))

if __name__ == '__main__':
    main()
