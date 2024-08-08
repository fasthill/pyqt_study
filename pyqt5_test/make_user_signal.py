import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5.QAxContainer import *

class Worker(QObject):
    user_signal = pyqtSignal(int, int)

    def run(self, a, b):
        print("inside def run")
        for i in range(a):
            self.user_signal.emit(i, b)
        print("after emit")

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        worker= Worker()
        print("after worker")
        worker.user_signal.connect(self.user_slot)
        print("after .connect")
        worker.run(10, 20)
        print("after run")

    @pyqtSlot(int, int)
    def user_slot(self, a, b):
        print("user slot")
        print(a, b)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()