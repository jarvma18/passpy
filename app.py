import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QAction, QFileDialog, QMessageBox

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Manager')
        self.setGeometry(100, 100, 400, 200)
        self.initUI()

    def initUI(self):
        # Create a label
        self.label = QLabel('Welcome to Password Manager!', self)
        self.setCentralWidget(self.label)

        # Create a menu bar
        menubar = self.menuBar()

        # Add file menu
        fileMenu = menubar.addMenu('File')

        # Add actions to the file menu
        newDbAction = QAction('New Database', self)
        newDbAction.triggered.connect(self.create_new_database)
        fileMenu.addAction(newDbAction)

        openDbAction = QAction('Open Database', self)
        openDbAction.triggered.connect(self.open_existing_database)
        fileMenu.addAction(openDbAction)

        quitAction = QAction('Quit', self)
        quitAction.triggered.connect(self.quit_application)
        fileMenu.addAction(quitAction)

    def create_new_database(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Create New Database", "", "SQLite Files (*.db);;All Files (*)", options=options)
        if fileName:
            QMessageBox.information(self, 'Success', 'New database created successfully!')

    def open_existing_database(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Existing Database", "", "SQLite Files (*.db);;All Files (*)", options=options)
        if fileName:
            self.label.setText(f'Opened database: {fileName}')
            # Here you can add more functionality to interact with the opened database

    def quit_application(self):
        QApplication.quit()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MyApp()
  window.show()
  sys.exit(app.exec_())