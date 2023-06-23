from PyQt5 import QtWidgets
from SP_Forms import MyDataPlotForm


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyDataPlotForm()
    MainWindow.show()
    sys.exit(app.exec_())
