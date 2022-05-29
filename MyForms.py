from PyQt5 import QtCore, QtWidgets, QtGui, uic


class TableSubWindow(QtWidgets.QWidget):
    def __init__(self):
        # parent initialisation
        QtWidgets.QWidget.__init__(self)

        # UI loading
        uic.loadUi('UI/MyTableWidget.ui', self)

        # explicit definition of the class attributes

        # new fields
        self.table = None


class TabSubWindow(QtWidgets.QWidget):
    def __init__(self):

        # parent initialisation
        QtWidgets.QWidget.__init__(self)

        # UI loading
        uic.loadUi('UI/MyTabWidget.ui', self)

        # explicit definition of the class attributes


class MyForm3(QtWidgets.QMainWindow):
    def __init__(self):

        # parent initialisation
        QtWidgets.QMainWindow.__init__(self)

        # UI loading
        uic.loadUi('UI/MyForm3.ui', self)

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
        self.XChooseColor = QtGui.QColor('green')
        self.YChooseColor = QtGui.QColor('blue')
        self.DataChooseColor = QtGui.QColor('yellow')

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
        self.actionAdaptic.triggered.connect(lambda: self.set_style('UI/qss/Adaptic.qss'))
        self.actionCombinear.triggered.connect(lambda: self.set_style('UI/qss/Combinear.qss'))
        self.actionDarkeum.triggered.connect(lambda: self.set_style('UI/qss/Darkeum.qss'))
        self.actionDiplaytap.triggered.connect(lambda: self.set_style('UI/qss/Diplaytap.qss'))
        self.actionEasyCode.triggered.connect(lambda: self.set_style('UI/qss/EasyCode.qss'))
        self.actionFibers.triggered.connect(lambda: self.set_style('UI/qss/Fibers.qss'))
        self.actionIrrorater.triggered.connect(lambda: self.set_style('UI/qss/Irrorater.qss'))
        self.actionPerstfic.triggered.connect(lambda: self.set_style('UI/qss/Perstfic.qss'))

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
        self.mdiArea.subWindowActivated.connect(self.sub_window_change)

        # new fields
        self.subWindow = QtWidgets.QMdiSubWindow()
        self.LoadProgress = QtWidgets.QProgressBar()
        self.LabelX = QtWidgets.QLabel()
        self.LabelY = QtWidgets.QLabel()
        self.LabelData = QtWidgets.QLabel()
        self.subWindow = QtWidgets.QMdiSubWindow()
        self.currentTable = QtWidgets.QTableWidget()

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

    def sub_window_change(self):
        self.subWindow = self.mdiArea.activeSubWindow()
#        self.currentTable = self.subWindow.widget().table


