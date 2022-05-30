from PyQt5 import QtCore, QtWidgets, QtGui, uic


class MyAbstractForm(QtCore.QObject):
    def __init__(self):
        super().__init__()

        # settings
        self.settings_file = 'settings.ini'
        self.settings = QtCore.QSettings(self.settings_file, QtCore.QSettings.IniFormat)

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


class MyTableSubWindow(QtWidgets.QWidget, MyAbstractForm):
    def __init__(self):
        # parent initialisation
        super().__init__()

        # UI loading
        uic.loadUi('UI/MyTableWidget.ui', self)

        # explicit definition of the class attributes

        # new fields
        self.table = None


class MyTabSubWindow(QtWidgets.QWidget, MyAbstractForm):
    def __init__(self):

        # parent initialisation
        QtWidgets.QWidget.__init__(self)

        # UI loading
        uic.loadUi('UI/MyTabWidget.ui', self)

        # explicit definition of the class attributes


class MyForm3(QtWidgets.QMainWindow, MyAbstractForm):
    def __init__(self):
        # parent initialisation
        super().__init__()

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
        self.actionNew = self.findChild(QtWidgets.QAction, "actionNew")
        self.actionOpen = self.findChild(QtWidgets.QAction, "actionOpen")
        self.actionSave = self.findChild(QtWidgets.QAction, "actionSave")
        self.actionExit = self.findChild(QtWidgets.QAction, "actionExit")
        self.actionFont = self.findChild(QtWidgets.QAction, "actionFont")
        self.actionTiled = self.findChild(QtWidgets.QAction, "actionTiled")
        self.actionCascaded = self.findChild(QtWidgets.QAction, "actionCascaded")
        self.actionAbout = self.findChild(QtWidgets.QAction, "actionAbout")

        self.push_add = self.findChild(QtWidgets.QPushButton, "push_add")
        self.push_remove = self.findChild(QtWidgets.QPushButton, "push_remove")
        self.push_reset = self.findChild(QtWidgets.QPushButton, "push_reset")
        self.push_next = self.findChild(QtWidgets.QPushButton, "push_next")
        self.push_cancel = self.findChild(QtWidgets.QPushButton, "push_cancel")

        self.combo_Xcolfrom = self.findChild(QtWidgets.QComboBox, "combo_Xcolfrom")
        self.combo_Xcolto = self.findChild(QtWidgets.QComboBox, "combo_Xcolto")
        self.combo_Xrowfrom = self.findChild(QtWidgets.QComboBox, "combo_Xrowfrom")
        self.combo_Xrowto = self.findChild(QtWidgets.QComboBox, "combo_Xrowto")
        self.combo_Ycolfrom = self.findChild(QtWidgets.QComboBox, "combo_Ycolfrom")
        self.combo_Ycolto = self.findChild(QtWidgets.QComboBox, "combo_Ycolto")
        self.combo_Yrowfrom = self.findChild(QtWidgets.QComboBox, "combo_Yrowfrom")
        self.combo_Yrowto = self.findChild(QtWidgets.QComboBox, "combo_Yrowto")
        self.combo_Ncolfrom = self.findChild(QtWidgets.QComboBox, "combo_Ncolfrom")
        self.combo_Ncolto = self.findChild(QtWidgets.QComboBox, "combo_Ncolto")
        self.combo_Nrowfrom = self.findChild(QtWidgets.QComboBox, "combo_Nrowfrom")
        self.combo_Nrowto = self.findChild(QtWidgets.QComboBox, "combo_Nrowto")
        self.combo_Datacolfrom = self.findChild(QtWidgets.QComboBox, "combo_Xcolfrom")
        self.combo_Datacolto = self.findChild(QtWidgets.QComboBox, "combo_Xcolto")
        self.combo_Datarowfrom = self.findChild(QtWidgets.QComboBox, "combo_Xrowfrom")
        self.combo_Datarowto = self.findChild(QtWidgets.QComboBox, "combo_Xrowto")
        self.combo_wise = self.findChild(QtWidgets.QComboBox, "combo_wise")

        self.mdiArea = self.findChild(QtWidgets.QMdiArea, "mdiArea")

        # settings
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
        self.actionNew.triggered.connect(self.create_new_file)
        self.actionOpen.triggered.connect(self.open_data_file)
        self.actionSave.triggered.connect(self.save_file)
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
        self.sub_window = QtWidgets.QMdiSubWindow()
        self.sub_window_number = 0
        self.LoadbProgress = QtWidgets.QProgressBar()
        self.LabelX = QtWidgets.QLabel()
        self.LabelY = QtWidgets.QLabel()
        self.LabelData = QtWidgets.QLabel()
        self.current_table = QtWidgets.QTableWidget()

    def create_new_file(self):
        self.statusbar.showMessage('Creating new data file...')
        new_sub_window = MyTableSubWindow()
        self.sub_window = new_sub_window
        self.sub_window_number += 1
        self.sub_window.setObjectName('sub-window ' + str(self.sub_window_number))
        self.sub_window.setWindowTitle('Data ' + str(self.sub_window_number))
        self.sub_window.setWindowIcon(QtGui.QIcon("UI/New_Icons/add-file.png"))
        self.current_table = self.sub_window.table
        self.mdiArea.addSubWindow(self.sub_window)
        self.sub_window.show()

    def open_data_file(self):
        pass

    def save_file(self):
        pass

    def sub_window_change(self):
        self.subWindow = self.mdiArea.activeSubWindow()
#        self.currentTable = self.subWindow.widget().table
