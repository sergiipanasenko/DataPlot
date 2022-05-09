from PyQt5 import QtCore, QtWidgets, QtGui, uic


class TableWidget(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.table = None
        self.WidgetInit()

    def WidgetInit(self):
        uic.loadUi('MyTableWidget.ui', self)


class TabWidget(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.WidgetInit()

    def WidgetInit(self):
        uic.loadUi('MyTabWidget.ui', self)


class ProgramWindow(QtWidgets.QMainWindow):
    SubWindowNumber = 0

    def __init__(self):

        # parent initialisation
        QtWidgets.QMainWindow.__init__(self)

        # form loading
        uic.loadUi('MyForm3.ui', self)

        # explicit definition of the class attributes
        self.statusbar = self.findChild(QtWidgets.QStatusBar, "statusbar")

        self.actionDefault = self.findChild(QtWidgets.QAction, "actionDefault")
        self.actionAdaptic = self.findChild(QtWidgets.QAction, "actionAdaptic")
        self.actionCombinear = self.findChild(QtWidgets.QAction, "actionCombinear")
        self.actionDarkeum = self.findChild(QtWidgets.QAction, "actionDarkeum")
        self.actionDiplaytap = self.findChild(QtWidgets.QAction, "actionDiplaytap")
        self.actionEasyCode = self.findChild(QtWidgets.QAction, "actionEasyCode")
        self.actionFibers = self.findChild(QtWidgets.QAction, "actionFibers")
        self.actionIrrorater = self.findChild(QtWidgets.QAction, "actionIrrorater")
        self.actionPerstfic = self.findChild(QtWidgets.QAction, "actionPerstfic")
        self.actionExit = self.findChild(QtWidgets.QAction, "actionExit")
        self.actionOpen = self.findChild(QtWidgets.QAction, "actionOpen")
        self.actionSave = self.findChild(QtWidgets.QAction, "actionSave")

        self.push_cancel = self.findChild(QtWidgets.QPushButton, "push_cancel")

        # self.combo_Xrowcol = self.findChild(QtWidgets.QComboBox, "combo_Xrowcol")
        # self.combo_Yrowcol = self.findChild(QtWidgets.QComboBox, "combo_Yrowcol")
        self.combo_Xnumber = self.findChild(QtWidgets.QComboBox, "combo_Xnumber")
        self.combo_Ynumber = self.findChild(QtWidgets.QComboBox, "combo_Ynumber")
        self.combo_Xbegin = self.findChild(QtWidgets.QComboBox, "combo_Xbegin")
        self.combo_Xend = self.findChild(QtWidgets.QComboBox, "combo_Xend")
        self.combo_Ybegin = self.findChild(QtWidgets.QComboBox, "combo_Ybegin")
        self.combo_Yend = self.findChild(QtWidgets.QComboBox, "combo_Yend")
        self.combo_Datarowbegin = self.findChild(QtWidgets.QComboBox, "combo_Datarowbegin")
        self.combo_Datarowend = self.findChild(QtWidgets.QComboBox, "combo_Datarowend")
        self.combo_Datacolbegin = self.findChild(QtWidgets.QComboBox, "combo_Datacolbegin")
        self.combo_Datacolend = self.findChild(QtWidgets.QComboBox, "combo_Datacolend")

        # self.check_Xvalue = self.findChild(QtWidgets.QCheckBox, "check_Xvalue")
        # self.check_Yvalue = self.findChild(QtWidgets.QCheckBox, "check_Yvalue")
        # self.check_Datavalue = self.findChild(QtWidgets.QCheckBox, "check_Datavalue")

        self.mdiArea = self.findChild(QtWidgets.QMdiArea, "mdiArea")

        self.label_totalrowvalue = self.findChild(QtWidgets.QLabel, "label_totalrowvalue")
        self.label_totalcolumnvalue = self.findChild(QtWidgets.QLabel, "label_totalcolumnvalue")
        self.label_Xrowcol = self.findChild(QtWidgets.QLabel, "label_Xrowcol")
        self.label_Yrowcol = self.findChild(QtWidgets.QLabel, "label_Yrowcol")

        # settings
        self.settings_file = 'settings.ini'
        self.settings = QtCore.QSettings(self.settings_file, QtCore.QSettings.IniFormat)
        self.set_style(self.settings.value('theme_checked', type=str))
        current_action = self.settings.value('theme_action_checked', type=str)
        self.findChild(QtWidgets.QAction, current_action).setChecked(True)
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2 - 30
        self.move(x, y)
        self.statusbar.showMessage('Ready')
        self.XRange = None
        self.YRange = None
        self.DataRange = None
        self.ListColNumber = None
        self.ListRowNumber = None
        self.XChooseColor = QtGui.QColor('green')
        self.YChooseColor = QtGui.QColor('blue')
        self.DataChooseColor = QtGui.QColor('yellow')

        # new fields
        self.LoadProgress = QtWidgets.QProgressBar()
        self.LabelX = QtWidgets.QLabel()
        self.LabelY = QtWidgets.QLabel()
        self.LabelData = QtWidgets.QLabel()
        self.subWindow = QtWidgets.QMdiSubWindow()
        self.currentTable = QtWidgets.QTableWidget()

        # action_groups
        self.themes = QtWidgets.QActionGroup(self)
        self.themes.addAction(self.actionDefault)
        self.themes.addAction(self.actionAdaptic)
        self.themes.addAction(self.actionCombinear)
        self.themes.addAction(self.actionDarkeum)
        self.themes.addAction(self.actionDiplaytap)
        self.themes.addAction(self.actionEasyCode)
        self.themes.addAction(self.actionFibers)
        self.themes.addAction(self.actionIrrorater)
        self.themes.addAction(self.actionPerstfic)

        # connections
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.actionOpen.triggered.connect(self.FileOpen)
        self.actionSave.triggered.connect(self.FileSave)
        self.actionDefault.triggered.connect(lambda: self.set_style(''))
        self.actionAdaptic.triggered.connect(lambda: self.set_style('qss/Adaptic.qss'))
        self.actionCombinear.triggered.connect(lambda: self.set_style('qss/Combinear.qss'))
        self.actionDarkeum.triggered.connect(lambda: self.set_style('qss/Darkeum.qss'))
        self.actionDiplaytap.triggered.connect(lambda: self.set_style('qss/Diplaytap.qss'))
        self.actionEasyCode.triggered.connect(lambda: self.set_style('qss/EasyCode.qss'))
        self.actionFibers.triggered.connect(lambda: self.set_style('qss/Fibers.qss'))
        self.actionIrrorater.triggered.connect(lambda: self.set_style('qss/Irrorater.qss'))
        self.actionPerstfic.triggered.connect(lambda: self.set_style('qss/Perstfic.qss'))

        self.push_cancel.clicked.connect(QtWidgets.qApp.quit)

        # self.combo_Xrowcol.currentIndexChanged.connect(self.XRowColChange)
        # self.combo_Yrowcol.currentIndexChanged.connect(self.YRowColChange)
#        self.combo_Xnumber.currentIndexChanged.connect(self.XChangeState)
#         self.combo_Ynumber.currentIndexChanged.connect(self.YChangeState)
#         self.combo_Xbegin.currentIndexChanged.connect(self.XChangeState)
#         self.combo_Xend.currentIndexChanged.connect(self.XChangeState)
#         self.combo_Ybegin.currentIndexChanged.connect(self.YChangeState)
#         self.combo_Yend.currentIndexChanged.connect(self.YChangeState)
#         self.combo_Datarowbegin.currentIndexChanged.connect(self.DataChangeState)
#         self.combo_Datarowend.currentIndexChanged.connect(self.DataChangeState)
#         self.combo_Datacolbegin.currentIndexChanged.connect(self.DataChangeState)
#         self.combo_Datacolend.currentIndexChanged.connect(self.DataChangeState)

        # self.check_Xvalue.stateChanged.connect(self.XChangeState)
        # self.check_Yvalue.stateChanged.connect(self.YChangeState)
        # self.check_Datavalue.stateChanged.connect(self.DataChangeState)
        # self.combo_Datarowbegin.currentIndexChanged.connect(self.DataChangeState)
        # self.combo_Datarowend.currentIndexChanged.connect(self.DataChangeState)
        # self.combo_Datacolbegin.currentIndexChanged.connect(self.DataChangeState)
        # self.combo_Datacolend.currentIndexChanged.connect(self.DataChangeState)
        self.mdiArea.subWindowActivated.connect(self.SubWindowChange)

    def set_style(self, qss_file_name):
        if self.sender():
            self.settings.setValue("theme_action_checked", self.sender().objectName())
        try:
            with open(qss_file_name, 'r') as qss_file:
                with qss_file:
                    qss = qss_file.read()
        except (FileNotFoundError, OSError, IOError):
            qss = ""
        QtWidgets.qApp.setStyleSheet(qss)
        self.settings.setValue("theme_checked", qss_file_name)
        self.settings.sync()

    def FileOpen(self):
        self.ListRowNumber = []
        self.ListColNumber = []
        self.XRange = []
        self.YRange = []
        self.DataRange = []
        self.combo_Datarowbegin.clear()
        self.combo_Datarowend.clear()
        self.combo_Datacolbegin.clear()
        self.combo_Datacolend.clear()
        self.statusbar.showMessage('Data loading from file...')
        self.LoadProgress = QtWidgets.QProgressBar()
        self.LoadProgress.setValue(0)
        recent_directory = self.settings.value('recent_directory', type=str)
        file = QtWidgets.QFileDialog.getOpenFileName(parent=MainWindow,
                                                     caption="Open data file",
                                                     directory=recent_directory,
                                                     filter="All files (*);;Text files (*.dat *.txt)",
                                                     initialFilter="Text files (*.dat *.txt)")
        if file[0]:
            self.settings.setValue('recent_directory', QtCore.QFileInfo(file[0]).path())
            raw_path = r'{}'.format(file[0])
            f = open(raw_path, 'rt')
            line_number = 0
            for _ in f:
                line_number += 1
            f.seek(0)
            row_number = 0
            col_number = 0
            self.LoadProgress.setRange(0, line_number)
            self.statusbar.addPermanentWidget(self.LoadProgress)
            table_widget = TableWidget()
            self.subWindow = table_widget
            self.subWindow.setObjectName('subwindow ' + str(self.SubWindowNumber))
            self.currentTable = self.subWindow.table
            self.currentTable.setRowCount(0)
            self.currentTable.setColumnCount(0)
            self.subWindow.setWindowTitle(raw_path)
            self.subWindow.setWindowIcon(QtGui.QIcon("Icons/Text.png"))
            self.mdiArea.addSubWindow(self.subWindow)
            self.subWindow.show()
            self.SubWindowNumber += 1
            for line in f:
                row = line.split()

                self.currentTable.setRowCount(self.currentTable.rowCount() + 1)
                if self.currentTable.columnCount() < len(row):
                    self.currentTable.setColumnCount(len(row))
                    col_number = len(row)
                for i in range(len(row)):
                    self.currentTable.setItem(row_number, i,
                                              QtWidgets.QTableWidgetItem(row[i]))
                row_number += 1
                self.LoadProgress.setValue(row_number)
            f.close()
            self.statusbar.showMessage('Initialization of values...')
            self.LoadProgress.setValue(0)
            self.label_totalrowvalue.setText(str(row_number))
            self.label_totalcolumnvalue.setText(str(col_number))
            self.ListColNumber = list(range(1, col_number + 1))
            self.ListColNumber = list(map(str, self.ListColNumber))
            self.ListRowNumber = list(range(1, row_number + 1))
            self.ListRowNumber = list(map(str, self.ListRowNumber))
            self.XRowColChange()
            self.LoadProgress.setValue(row_number // 4)
            self.YRowColChange()
            self.LoadProgress.setValue(row_number // 2)
            # self.combo_Datarowbegin.addItems(5)
            self.combo_Datarowbegin.addItems(self.ListRowNumber)
            self.combo_Datarowend.addItems(self.ListRowNumber)
            self.combo_Datarowend.setCurrentIndex(len(self.ListRowNumber) - 1)
            self.combo_Datacolbegin.addItems(self.ListColNumber)
            self.combo_Datacolend.addItems(self.ListColNumber)
            self.combo_Datacolend.setCurrentIndex(len(self.ListColNumber) - 1)
            self.LoadProgress.setValue(3 * row_number // 4)
            self.XChangeState()
            self.YChangeState()
            self.LoadProgress.setValue(row_number)
            self.DataChangeState()
            self.statusbar.clearMessage()
            self.statusbar.removeWidget(self.LoadProgress)
            self.LabelX.setText('X:')
            self.statusbar.addWidget(self.LabelX, 1)
            self.LabelY.setText('Y:')
            self.statusbar.addWidget(self.LabelY, 1)
            self.LabelData.setText('Data:')
            self.statusbar.addWidget(self.LabelData, 1)

    @staticmethod
    def FileSave():
        file = QtWidgets.QFileDialog.getSaveFileName(parent=MainWindow,
                                                     caption="Save data file",
                                                     directory=QtCore.QDir.currentPath(),
                                                     filter="All files (*);;Text files (*.dat *.txt)",
                                                     initialFilter="Text files (*.dat *.txt)")

    def TableRepaint(self):
        background_color = QtGui.QColor('white')
        if self.ListRowNumber:
            for j in self.ListRowNumber:
                for i in self.ListColNumber:
                    jj = int(j) - 1
                    ii = int(i) - 1
                    if self.currentTable.item(jj, ii):
                        self.currentTable.item(jj, ii).setBackground(background_color)
        # if self.check_Datavalue.isChecked():
        #     self.DataSelect()
        # if self.check_Xvalue.isChecked():
        #     self.XSelect()
        # if self.check_Yvalue.isChecked():
        #     self.YSelect()
        self.unsetCursor()

    def XSelect(self):
        if len(self.XRange):
            if self.XRange[2] < self.XRange[1]:
                step = -1
                begin = self.XRange[1]
                end = self.XRange[2] - 1
            else:
                step = 1
                begin = self.XRange[1]
                end = self.XRange[2] + 1
            if self.XRange[3]:
                for i in range(begin, end, step):
                    if self.currentTable.item(i, self.XRange[0]):
                        self.currentTable.item(i, self.XRange[0]).setBackground(self.XChooseColor)
            else:
                for i in range(begin, end, step):
                    if self.currentTable.item(self.XRange[0], i):
                        self.currentTable.item(self.XRange[0], i).setBackground(self.XChooseColor)

    def YSelect(self):
        if len(self.YRange):
            if self.YRange[2] < self.YRange[1]:
                step = -1
                begin = self.YRange[1]
                end = self.YRange[2] - 1
            else:
                step = 1
                begin = self.YRange[1]
                end = self.YRange[2] + 1
            if self.YRange[3]:
                for i in range(begin, end, step):
                    if self.currentTable.item(self.YRange[0], self.YRange[0]):
                        self.currentTable.item(self.YRange[0], i).setBackground(self.YChooseColor)
            else:
                for i in range(begin, end, step):
                    if self.currentTable.item(i, self.YRange[0]):
                        self.currentTable.item(i, self.YRange[0]).setBackground(self.YChooseColor)

    def XRangeInit(self):
        if len(self.XRange):
            self.XRange[0] = self.combo_Xnumber.currentIndex()
            self.XRange[1] = self.combo_Xbegin.currentIndex()
            self.XRange[2] = self.combo_Xend.currentIndex()
            # if self.combo_Xrowcol.currentIndex():
            #     self.XRange[3] = False
            # else:
            #     self.XRange[3] = True
        else:
            self.XRange.append(self.combo_Xnumber.currentIndex())
            self.XRange.append(self.combo_Xbegin.currentIndex())
            self.XRange.append(self.combo_Xend.currentIndex())
            # if self.combo_Xrowcol.currentIndex():
            #     self.XRange.append(False)
            # else:
            #     self.XRange.append(True)

    def YRangeInit(self):
        if len(self.YRange):
            self.YRange[0] = self.combo_Ynumber.currentIndex()
            self.YRange[1] = self.combo_Ybegin.currentIndex()
            self.YRange[2] = self.combo_Yend.currentIndex()
            if self.combo_Yrowcol.currentIndex():
                self.YRange[3] = False
            else:
                self.YRange[3] = True
        else:
            self.YRange.append(self.combo_Ynumber.currentIndex())
            self.YRange.append(self.combo_Ybegin.currentIndex())
            self.YRange.append(self.combo_Yend.currentIndex())
            # if self.combo_Yrowcol.currentIndex():
            #     self.YRange.append(False)
            # else:
            #     self.YRange.append(True)

    def XRowColChange(self):
        self.XRange = []
        self.combo_Xnumber.clear()
        self.combo_Xbegin.clear()
        self.combo_Xend.clear()
        # if self.combo_Xrowcol.currentIndex():
        #     self.label_Xrowcol.setText('Columns from')
        #     self.combo_Xnumber.addItems(self.ListRowNumber)
        #     self.combo_Xbegin.addItems(self.ListColNumber)
        #     self.combo_Xend.addItems(self.ListColNumber)
        #     self.combo_Xend.setCurrentIndex(len(self.ListColNumber) - 1)
        # else:
        #     self.label_Xrowcol.setText('Rows from')
        #     self.combo_Xnumber.addItems(self.ListColNumber)
        #     self.combo_Xbegin.addItems(self.ListRowNumber)
        #     self.combo_Xend.addItems(self.ListRowNumber)
        #     self.combo_Xend.setCurrentIndex(len(self.ListRowNumber) - 1)
        self.XRangeInit()

    def YRowColChange(self):
        self.YRange = []
        self.combo_Ynumber.clear()
        self.combo_Ybegin.clear()
        self.combo_Yend.clear()
        # if self.combo_Yrowcol.currentIndex():
        #     self.label_Yrowcol.setText('Rows from')
        #     self.combo_Ynumber.addItems(self.ListColNumber)
        #     self.combo_Ybegin.addItems(self.ListRowNumber)
        #     self.combo_Yend.addItems(self.ListRowNumber)
        #     self.combo_Yend.setCurrentIndex(len(self.ListRowNumber) - 1)
        # else:
        #     self.label_Yrowcol.setText('Columns from')
        #     self.combo_Ynumber.addItems(self.ListRowNumber)
        #     self.combo_Ybegin.addItems(self.ListColNumber)
        #     self.combo_Yend.addItems(self.ListColNumber)
        #     self.combo_Yend.setCurrentIndex(len(self.ListColNumber) - 1)
        self.YRangeInit()

    # def XChangeState(self):
    #     if self.currentTable.rowCount():
    #         if self.check_Xvalue.isChecked():
    #             self.XRangeInit()
    #         else:
    #             self.XRange = []
    #         self.TableRepaint()

    # def YChangeState(self):
    #     if self.currentTable.rowCount():
    #         if self.check_Yvalue.isChecked():
    #             self.YRangeInit()
    #         else:
    #             self.YRange = []
    #         self.TableRepaint()
    #
    # def DataChangeState(self):
    #     if self.currentTable.rowCount():
    #         if self.check_Datavalue.isChecked():
    #             self.DataRangeInit()
    #         else:
    #             self.DataRange = []
    #         self.TableRepaint()

    def DataRangeInit(self):
        row_begin = self.combo_Datarowbegin.currentIndex()
        row_end = self.combo_Datarowend.currentIndex()
        col_begin = self.combo_Datacolbegin.currentIndex()
        col_end = self.combo_Datacolend.currentIndex()
        if len(self.DataRange):
            self.DataRange[0] = [row_begin, col_begin]
            self.DataRange[1] = [row_end, col_end]
        else:
            self.DataRange.append([row_begin, col_begin])
            self.DataRange.append([row_end, col_end])

    def DataSelect(self):
        if len(self.DataRange):
            row_begin = self.DataRange[0][0]
            row_end = self.DataRange[1][0]
            col_begin = self.DataRange[0][1]
            col_end = self.DataRange[1][1]
            if row_end < row_begin:
                step_row = -1
                begin_row = row_begin
                end_row = row_end - 1
            else:
                step_row = 1
                begin_row = row_begin
                end_row = row_end + 1
            if col_end < col_begin:
                step_col = -1
                begin_col = col_begin
                end_col = col_end - 1
            else:
                step_col = 1
                begin_col = col_begin
                end_col = col_end + 1
            # if self.check_Datavalue.isChecked():
            #     for j in range(begin_row, end_row, step_row):
            #         for i in range(begin_col, end_col, step_col):
            #             if self.currentTable.item(j, i):
            #                 self.currentTable.item(j, i).setBackground(self.DataChooseColor)

    def SubWindowChange(self):
        self.subWindow = self.mdiArea.activeSubWindow()
        self.currentTable = self.subWindow.widget().table


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ProgramWindow()
    MainWindow.show()
    sys.exit(app.exec_())
