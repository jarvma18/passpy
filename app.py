import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MyApp(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('Hello PyQt')
    self.setGeometry(100, 100, 200, 80)
    label = QLabel('Hello, world!', self)
    self.setCentralWidget(label)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MyApp()
  window.show()
  sys.exit(app.exec_())