from PyQt5 import QtCore, QtWidgets, QtGui, uic

class TableWidget(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
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
        QtWidgets.QMainWindow.__init__(self)

        self.settings_file = 'settings.ini'
        self.settings = QtCore.QSettings(self.settings_file, QtCore.QSettings.IniFormat)
        self.XChooseColor = QtGui.QColor(119, 223, 139)
        self.DataChooseColor = QtGui.QColor(247, 247, 101)
        self.LoadProgress = QtWidgets.QProgressBar()

        # load
        uic.loadUi('MyForm2.ui', self)
        self.set_style(self.settings.value('theme_checked', type=str))
        self.statusBar().showMessage('Ready')

        # settings
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2 - 30
        self.move(x, y)

        self.YChooseColor = QtGui.QColor(119, 203, 224)
        self.NChooseColor = QtGui.QColor(234, 134, 222)
        # self.stylesheet = "::section{background-color: rgb(200,200,200); color: rgb(220,0,0); \
        #                   font-family: 'Times New Roman'; font-size: 12pt}"

        # new fields
        self.LabelX = QtWidgets.QLabel()
        self.LabelY = QtWidgets.QLabel()
        self.LabelData = QtWidgets.QLabel()
        self.subWindow = QtWidgets.QMdiSubWindow()
        self.currentTable = QtWidgets.QTableWidget()

        # action_groups
        self.themes = QtWidgets.QActionGroup(self)
        self.themes.addAction(self.actionWindows)
        self.themes.addAction(self.actionAdaptic)
        self.themes.addAction(self.actionCombinear)
        self.themes.addAction(self.actionDarkeum)
        self.themes.addAction(self.actionDiplaytap)
        self.themes.addAction(self.actionEasyCode)
        self.themes.addAction(self.actionFibers)
        self.themes.addAction(self.actionIntegrid)
        self.themes.addAction(self.actionIrrorater)
        self.themes.addAction(self.actionPerstfic)

        # connections
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.actionOpen.triggered.connect(self.FileOpen)
        self.actionSave.triggered.connect(self.FileSave)
        self.actionWindows.triggered.connect(lambda: self.set_style(''))
        self.actionAdaptic.triggered.connect(lambda: self.set_style('qss/Adaptic.qss'))
        self.actionCombinear.triggered.connect(lambda: self.set_style('qss/Combinear.qss'))
        self.actionDarkeum.triggered.connect(lambda: self.set_style('qss/Darkeum.qss'))
        self.actionDiplaytap.triggered.connect(lambda: self.set_style('qss/Diplaytap.qss'))
        self.actionEasyCode.triggered.connect(lambda: self.set_style('qss/EasyCode.qss'))
        self.actionFibers.triggered.connect(lambda: self.set_style('qss/Fibers.qss'))
        self.actionIrrorater.triggered.connect(lambda: self.set_style('qss/Irrorater.qss'))
        self.actionPerstfic.triggered.connect(lambda: self.set_style('qss/Perstfic.qss'))
        self.push_cancel.clicked.connect(QtWidgets.qApp.quit)
        self.combo_Xrowcol.currentIndexChanged.connect(self.XRowColChange)
        self.combo_Yrowcol.currentIndexChanged.connect(self.YRowColChange)
        self.check_Xvalue.stateChanged.connect(self.XChangeState)
        self.check_Yvalue.stateChanged.connect(self.YChangeState)
        self.combo_Xnumber.currentIndexChanged.connect(self.XChangeState)
        self.combo_Ynumber.currentIndexChanged.connect(self.YChangeState)
        self.combo_Xbegin.currentIndexChanged.connect(self.XChangeState)
        self.combo_Xend.currentIndexChanged.connect(self.XChangeState)
        self.combo_Ybegin.currentIndexChanged.connect(self.YChangeState)
        self.combo_Yend.currentIndexChanged.connect(self.YChangeState)
        self.check_Datavalue.stateChanged.connect(self.DataChangeState)
        self.combo_Datarowbegin.currentIndexChanged.connect(self.DataChangeState)
        self.combo_Datarowend.currentIndexChanged.connect(self.DataChangeState)
        self.combo_Datacolbegin.currentIndexChanged.connect(self.DataChangeState)
        self.combo_Datacolend.currentIndexChanged.connect(self.DataChangeState)
        self.mdiArea.subWindowActivated.connect(self.SubWindowChange)

    def set_style(self, qss_file_name):
        # settings = QtCore.QSettings(self.settings_file, QtCore.QSettings.IniFormat)
        qss = ""
        try:
            with open(qss_file_name, 'r') as qss_file:
                with qss_file:
                    qss = qss_file.read()
        except:
            pass
        QtWidgets.qApp.setStyleSheet(qss)
        self.settings.setValue("theme_checked", qss_file_name)
        self.settings.sync()

    def FileOpen(self):
        self.ListRowNumber = []
        self.ListColNumber = []
        self.XRange = []
        self.YRange = []
        self.DataRange = []
        # self.table_Data.setRowCount(0)
        # self.table_Data.setColumnCount(0)
        ##        self.combo_Nnumber.clear()
        ##        self.combo_Nbegin.clear()
        ##        self.combo_Nend.clear()
        self.combo_Datarowbegin.clear()
        self.combo_Datarowend.clear()
        self.combo_Datacolbegin.clear()
        self.combo_Datacolend.clear()
        self.statusbar.showMessage('Data loading from file...')
        self.LoadProgress = QtWidgets.QProgressBar()
        self.LoadProgress.setValue(0)
        file = QtWidgets.QFileDialog.getOpenFileName(parent=MainWindow,
                                                     caption="Open data file",
                                                     directory=QtCore.QDir.currentPath(),
                                                     filter="All files (*);;Text files (*.dat *.txt)",
                                                     initialFilter="Text files (*.dat *.txt)")
        if file[0]:
            raw_path = r'{}'.format(file[0])
            f = open(raw_path, 'rt')
            LineNumber = 0
            for _ in f:
                LineNumber += 1
            f.seek(0)
            RowNumber = 0
            ColNumber = 0
            self.LoadProgress.setRange(0, LineNumber)
            self.statusbar.addPermanentWidget(self.LoadProgress)
            tableWidget = TableWidget()
            self.subWindow = tableWidget
            self.subWindow.setObjectName('subwindow ' + str(self.SubWindowNumber))
            self.currentTable = self.subWindow.table
            # self.currentTable.horizontalHeader().setStyleSheet(self.stylesheet)
            # self.currentTable.verticalHeader().setStyleSheet(self.stylesheet)
            self.currentTable.setRowCount(0)
            self.currentTable.setColumnCount(0)
            self.subWindow.setWindowTitle(raw_path)
            self.subWindow.setWindowIcon(QtGui.QIcon('Icons\Text.png'))
            self.mdiArea.addSubWindow(self.subWindow)
            self.subWindow.show()
            self.SubWindowNumber += 1
            for line in f:
                row = line.split()

                self.currentTable.setRowCount(self.currentTable.rowCount() + 1)
                if self.currentTable.columnCount() < len(row):
                    self.currentTable.setColumnCount(len(row))
                    ColNumber = len(row)
                for i in range(len(row)):
                    self.currentTable.setItem(RowNumber, i,
                                              QtWidgets.QTableWidgetItem(row[i]))
                RowNumber += 1
                self.LoadProgress.setValue(RowNumber)
            f.close()
            self.statusbar.showMessage('Initialization of values...')
            self.LoadProgress.setValue(0)
            self.label_totalrowvalue.setText(str(RowNumber))
            self.label_totalcolumnvalue.setText(str(ColNumber))
            self.ListColNumber = list(range(1, ColNumber + 1))
            self.ListColNumber = list(map(str, self.ListColNumber))
            self.ListRowNumber = list(range(1, RowNumber + 1))
            self.ListRowNumber = list(map(str, self.ListRowNumber))
            self.XRowColChange()
            self.LoadProgress.setValue(RowNumber // 4)
            self.YRowColChange()
            self.LoadProgress.setValue(RowNumber // 2)
            # self.combo_Datarowbegin.addItems(5)
            self.combo_Datarowbegin.addItems(self.ListRowNumber)
            self.combo_Datarowend.addItems(self.ListRowNumber)
            self.combo_Datarowend.setCurrentIndex(len(self.ListRowNumber) - 1)
            self.combo_Datacolbegin.addItems(self.ListColNumber)
            self.combo_Datacolend.addItems(self.ListColNumber)
            self.combo_Datacolend.setCurrentIndex(len(self.ListColNumber) - 1)
            self.LoadProgress.setValue(3 * RowNumber // 4)
            self.XChangeState()
            self.YChangeState()
            self.LoadProgress.setValue(RowNumber)
            self.DataChangeState()
            self.statusbar.clearMessage()
            self.statusbar.removeWidget(self.LoadProgress)
            self.LabelX.setText('X:')
            self.statusbar.addWidget(self.LabelX, 1)
            self.LabelY.setText('Y:')
            self.statusbar.addWidget(self.LabelY, 1)
            self.LabelData.setText('Data:')
            self.statusbar.addWidget(self.LabelData, 1)

    def FileSave(self):
        file = QtWidgets.QFileDialog.getSaveFileName(parent=MainWindow,
                                                     caption="Save data file",
                                                     directory=QtCore.QDir.currentPath(),
                                                     filter="All files (*);;Text files (*.dat *.txt)",
                                                     initialFilter="Text files (*.dat *.txt)")

    def TableRepaint(self):
        BackgroundColor = QtGui.QColor('white')
        if self.ListRowNumber:
            for j in self.ListRowNumber:
                for i in self.ListColNumber:
                    jj = int(j) - 1
                    ii = int(i) - 1
                    if self.currentTable.item(jj, ii):
                        self.currentTable.item(jj, ii).setBackground(BackgroundColor)
        if self.check_Datavalue.isChecked():
            self.DataSelect()
        if self.check_Xvalue.isChecked():
            self.XSelect()
        if self.check_Yvalue.isChecked():
            self.YSelect()
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
            if self.combo_Xrowcol.currentIndex():
                self.XRange[3] = False
            else:
                self.XRange[3] = True
        else:
            self.XRange.append(self.combo_Xnumber.currentIndex())
            self.XRange.append(self.combo_Xbegin.currentIndex())
            self.XRange.append(self.combo_Xend.currentIndex())
            if self.combo_Xrowcol.currentIndex():
                self.XRange.append(False)
            else:
                self.XRange.append(True)

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
            if self.combo_Yrowcol.currentIndex():
                self.YRange.append(False)
            else:
                self.YRange.append(True)

    def XRowColChange(self):
        self.XRange = []
        self.combo_Xnumber.clear()
        self.combo_Xbegin.clear()
        self.combo_Xend.clear()
        if self.combo_Xrowcol.currentIndex():
            self.label_Xrowcol.setText('Columns from')
            self.combo_Xnumber.addItems(self.ListRowNumber)
            self.combo_Xbegin.addItems(self.ListColNumber)
            self.combo_Xend.addItems(self.ListColNumber)
            self.combo_Xend.setCurrentIndex(len(self.ListColNumber) - 1)
        else:
            self.label_Xrowcol.setText('Rows from')
            self.combo_Xnumber.addItems(self.ListColNumber)
            self.combo_Xbegin.addItems(self.ListRowNumber)
            self.combo_Xend.addItems(self.ListRowNumber)
            self.combo_Xend.setCurrentIndex(len(self.ListRowNumber) - 1)
        self.XRangeInit()

    def YRowColChange(self):
        self.YRange = []
        self.combo_Ynumber.clear()
        self.combo_Ybegin.clear()
        self.combo_Yend.clear()
        if self.combo_Yrowcol.currentIndex():
            self.label_Yrowcol.setText('Rows from')
            self.combo_Ynumber.addItems(self.ListColNumber)
            self.combo_Ybegin.addItems(self.ListRowNumber)
            self.combo_Yend.addItems(self.ListRowNumber)
            self.combo_Yend.setCurrentIndex(len(self.ListRowNumber) - 1)
        else:
            self.label_Yrowcol.setText('Columns from')
            self.combo_Ynumber.addItems(self.ListRowNumber)
            self.combo_Ybegin.addItems(self.ListColNumber)
            self.combo_Yend.addItems(self.ListColNumber)
            self.combo_Yend.setCurrentIndex(len(self.ListColNumber) - 1)
        self.YRangeInit()

    def XChangeState(self):
        if self.currentTable.rowCount():
            if self.check_Xvalue.isChecked():
                self.XRangeInit()
            else:
                self.XRange = []
            self.TableRepaint()

    def YChangeState(self):
        if self.currentTable.rowCount():
            if self.check_Yvalue.isChecked():
                self.YRangeInit()
            else:
                self.YRange = []
            self.TableRepaint()

    def DataChangeState(self):
        if self.currentTable.rowCount():
            if self.check_Datavalue.isChecked():
                self.DataRangeInit()
            else:
                self.DataRange = []
            self.TableRepaint()

    def DataRangeInit(self):
        RowBegin = self.combo_Datarowbegin.currentIndex()
        RowEnd = self.combo_Datarowend.currentIndex()
        ColBegin = self.combo_Datacolbegin.currentIndex()
        ColEnd = self.combo_Datacolend.currentIndex()
        if len(self.DataRange):
            self.DataRange[0] = [RowBegin, ColBegin]
            self.DataRange[1] = [RowEnd, ColEnd]
        else:
            self.DataRange.append([RowBegin, ColBegin])
            self.DataRange.append([RowEnd, ColEnd])

    def DataSelect(self):
        if len(self.DataRange):
            RowBegin = self.DataRange[0][0]
            RowEnd = self.DataRange[1][0]
            ColBegin = self.DataRange[0][1]
            ColEnd = self.DataRange[1][1]
            if RowEnd < RowBegin:
                stepRow = -1
                beginRow = RowBegin
                endRow = RowEnd - 1
            else:
                stepRow = 1
                beginRow = RowBegin
                endRow = RowEnd + 1
            if ColEnd < ColBegin:
                stepCol = -1
                beginCol = ColBegin
                endCol = ColEnd - 1
            else:
                stepCol = 1
                beginCol = ColBegin
                endCol = ColEnd + 1
            if self.check_Datavalue.isChecked():
                for j in range(beginRow, endRow, stepRow):
                    for i in range(beginCol, endCol, stepCol):
                        if self.currentTable.item(j, i):
                            self.currentTable.item(j, i).setBackground(self.DataChooseColor)

    def SubWindowChange(self):
        self.subWindow = self.mdiArea.activeSubWindow()
        self.currentTable = self.subWindow.widget().table


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ProgramWindow()
    MainWindow.show()
    sys.exit(app.exec_())
