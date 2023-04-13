from os.path import splitext
from PyQt5 import QtCore, QtWidgets, QtGui, uic
from my_gui import MyAbstractForm, MyTableWidget, MyTabWidget


class MyForm3(QtWidgets.QMainWindow, MyAbstractForm):
    def __init__(self):
        # parent initialisation
        super().__init__()

        # ui loading
        uic.loadUi('ui/MyForm4.ui', self)

        # new fields
        self.sub_window = None
        self.sub_window_number = 0
        self.sub_window_amount = 0
        self.table_number = 0
        self.current_tabs = None
        self.current_table = None
        self.x_values = dict()
        self.y_values = dict()
        self.data_values = dict()

        # explicit definition of the class attributes
        self.statusbar = self.findChild(QtWidgets.QStatusBar, "statusbar")

        # Settings/Themes
        self.actionDefault = self.findChild(QtWidgets.QAction, "actionDefault")
        self.actionAdaptic = self.findChild(QtWidgets.QAction, "actionAdaptic")
        self.actionCombinear = self.findChild(QtWidgets.QAction, "actionCombinear")
        self.actionDarkeum = self.findChild(QtWidgets.QAction, "actionDarkeum")
        self.actionDiplaytap = self.findChild(QtWidgets.QAction, "actionDiplaytap")
        self.actionEasyCode = self.findChild(QtWidgets.QAction, "actionEasyCode")
        self.actionFibers = self.findChild(QtWidgets.QAction, "actionFibers")
        self.actionIrrorater = self.findChild(QtWidgets.QAction, "actionIrrorater")
        self.actionPerstfic = self.findChild(QtWidgets.QAction, "actionPerstfic")

        # File
        self.actionNew = self.findChild(QtWidgets.QAction, "actionNew")
        self.actionOpen = self.findChild(QtWidgets.QAction, "actionOpen")
        self.actionOutput = self.findChild(QtWidgets.QAction, "actionOutput")
        self.actionSave = self.findChild(QtWidgets.QAction, "actionSave")
        self.actionExit = self.findChild(QtWidgets.QAction, "actionExit")

        # Settings/Font
        self.actionFont = self.findChild(QtWidgets.QAction, "actionFont")

        # Window
        self.actionTiled = self.findChild(QtWidgets.QAction, "actionTiled")
        self.actionCascaded = self.findChild(QtWidgets.QAction, "actionCascaded")

        # Help
        self.actionAbout = self.findChild(QtWidgets.QAction, "actionAbout")

        # Table
        self.menuAdd = self.findChild(QtWidgets.QMenu, "menuAdd")
        self.menuRemove = self.findChild(QtWidgets.QMenu, "menuRemove")
        self.actionRow_above = self.findChild(QtWidgets.QAction, "actionRow_above")
        self.actionRow_below = self.findChild(QtWidgets.QAction, "actionRow_below")
        self.actionColumn_left = self.findChild(QtWidgets.QAction, "actionColumn_left")
        self.actionColumn_right = self.findChild(QtWidgets.QAction, "actionColumn_right")
        self.actionRow = self.findChild(QtWidgets.QAction, "actionRow")
        self.actionColumn = self.findChild(QtWidgets.QAction, "actionColumn")

        # Buttons
        self.push_add = self.findChild(QtWidgets.QPushButton, "push_add")
        self.push_remove = self.findChild(QtWidgets.QPushButton, "push_remove")
        self.push_reset = self.findChild(QtWidgets.QPushButton, "push_reset")
        self.push_next = self.findChild(QtWidgets.QPushButton, "push_next")
        self.push_cancel = self.findChild(QtWidgets.QPushButton, "push_cancel")

        # Combos
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
        self.combo_Datacolfrom = self.findChild(QtWidgets.QComboBox, "combo_Datacolfrom")
        self.combo_Datacolto = self.findChild(QtWidgets.QComboBox, "combo_Datacolto")
        self.combo_Datarowfrom = self.findChild(QtWidgets.QComboBox, "combo_Datarowfrom")
        self.combo_Datarowto = self.findChild(QtWidgets.QComboBox, "combo_Datarowto")
        self.combo_wise = self.findChild(QtWidgets.QComboBox, "combo_wise")

        # Labels
        self.label_totalrowvalue = self.findChild(QtWidgets.QLabel, "label_totalrowvalue")
        self.label_totalcolumnvalue = self.findChild(QtWidgets.QLabel, "label_totalcolumnvalue")
        self.label_currentrowvalue = self.findChild(QtWidgets.QLabel, "label_currentrowvalue")
        self.label_currentcolumnvalue = self.findChild(QtWidgets.QLabel, "label_currentcolumnvalue")

        # MDI area
        self.mdiArea = self.findChild(QtWidgets.QMdiArea, "mdiArea")

        # settings
        geometry = self.settings.value('Geometry')
        if geometry:
            self.restoreGeometry(geometry)

        state = self.settings.value('WindowState')
        if state:
            self.restoreState(state)

        self.set_style(self.settings.value('theme_checked', type=str))
        current_action = self.settings.value('theme_action_checked', type=str)
        self.findChild(QtWidgets.QAction, current_action).setChecked(True)
        self.statusbar.showMessage('Ready')
        self.XChooseColor = QtGui.QColor('green')
        self.YChooseColor = QtGui.QColor('blue')
        self.DataChooseColor = QtGui.QColor('yellow')

        # action_group1
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

        # action_group2
        self.layout = QtWidgets.QActionGroup(self)
        self.layout.addAction(self.actionTiled)
        self.layout.addAction(self.actionCascaded)

        # connections
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.actionNew.triggered.connect(self.add_new_sub_window)
        self.actionOpen.triggered.connect(self.open_data_file)
        self.actionOutput.triggered.connect(self.add_new_sub_window)
        self.actionSave.triggered.connect(self.save_file)

        self.actionDefault.triggered.connect(lambda: self.set_style(''))
        self.actionAdaptic.triggered.connect(lambda: self.set_style('ui/qss/Adaptic.qss'))
        self.actionCombinear.triggered.connect(lambda: self.set_style('ui/qss/Combinear.qss'))
        self.actionDarkeum.triggered.connect(lambda: self.set_style('ui/qss/Darkeum.qss'))
        self.actionDiplaytap.triggered.connect(lambda: self.set_style('ui/qss/Diplaytap.qss'))
        self.actionEasyCode.triggered.connect(lambda: self.set_style('ui/qss/EasyCode.qss'))
        self.actionFibers.triggered.connect(lambda: self.set_style('ui/qss/Fibers.qss'))
        self.actionIrrorater.triggered.connect(lambda: self.set_style('ui/qss/Irrorater.qss'))
        self.actionPerstfic.triggered.connect(lambda: self.set_style('ui/qss/Perstfic.qss'))

        self.actionTiled.triggered.connect(self.mdiArea.tileSubWindows)
        self.actionCascaded.triggered.connect(self.mdiArea.cascadeSubWindows)

        self.actionRow_above.triggered.connect(lambda: self._add_row(True))
        self.actionRow_below.triggered.connect(lambda: self._add_row(False))
        self.actionColumn_left.triggered.connect(lambda: self._add_column(True))
        self.actionColumn_right.triggered.connect(lambda: self._add_column(False))
        self.actionRow.triggered.connect(self._remove_row)
        self.actionColumn.triggered.connect(self._remove_column)
        self.push_cancel.clicked.connect(QtWidgets.qApp.quit)

        self.mdiArea.subWindowActivated.connect(self.sub_window_change)

    def open(self):
        recent_directory = self.settings.value('recent_directory', type=str)
        self.statusbar.showMessage('Data loading from file...')

    def _change_table(self):
        if self.current_table:
            self.combo_Xrowfrom.clear()
            self.combo_Xrowto.clear()
            self.combo_Xcolfrom.clear()
            self.combo_Xcolto.clear()
            self.combo_Yrowfrom.clear()
            self.combo_Yrowto.clear()
            self.combo_Ycolfrom.clear()
            self.combo_Ycolto.clear()
            self.combo_Datarowfrom.clear()
            self.combo_Datarowto.clear()
            self.combo_Datacolfrom.clear()
            self.combo_Datacolto.clear()
            if self.current_table.columnCount() and self.current_table.rowCount():
                row_number_list = list(map(str, range(1, self.current_table.rowCount() + 1)))
                col_number_list = list(map(str, range(1, self.current_table.columnCount() + 1)))
                self.combo_Xrowfrom.addItems(row_number_list)
                self.combo_Xrowfrom.setCurrentIndex(0)
                self.combo_Xrowto.addItems(row_number_list)
                self.combo_Xrowto.setCurrentIndex(len(row_number_list) - 1)
                self.combo_Xcolfrom.addItems(col_number_list)
                self.combo_Xcolfrom.setCurrentIndex(0)
                self.combo_Xcolto.addItems(col_number_list)
                self.combo_Xcolto.setCurrentIndex(len(col_number_list) - 1)
                self.combo_Yrowfrom.addItems(row_number_list)
                self.combo_Yrowfrom.setCurrentIndex(0)
                self.combo_Yrowto.addItems(row_number_list)
                self.combo_Yrowto.setCurrentIndex(len(row_number_list) - 1)
                self.combo_Ycolfrom.addItems(col_number_list)
                self.combo_Ycolfrom.setCurrentIndex(0)
                self.combo_Ycolto.addItems(col_number_list)
                self.combo_Ycolto.setCurrentIndex(len(col_number_list) - 1)
                self.combo_Datarowfrom.addItems(row_number_list)
                self.combo_Datarowfrom.setCurrentIndex(0)
                self.combo_Datarowto.addItems(row_number_list)
                self.combo_Datarowto.setCurrentIndex(len(row_number_list) - 1)
                self.combo_Datacolfrom.addItems(col_number_list)
                self.combo_Datacolfrom.setCurrentIndex(0)
                self.combo_Datacolto.addItems(col_number_list)
                self.combo_Datacolto.setCurrentIndex(len(col_number_list) - 1)
            self.label_totalrowvalue.setText(str(self.current_table.rowCount()))
            self.label_totalcolumnvalue.setText(str(self.current_table.columnCount()))
            self.select_cell()

    def _create_sub_window(self, sub_window_title, sub_window_icon, widget):
        if not self.menuAdd.isEnabled():
            self.menuAdd.setEnabled(True)
            self.actionRow_above.setEnabled(True)
            self.actionRow_below.setEnabled(True)
            self.actionColumn_left.setEnabled(True)
            self.actionColumn_right.setEnabled(True)
            self.menuRemove.setEnabled(True)
            self.actionRow.setEnabled(True)
            self.actionColumn.setEnabled(True)
        self.sub_window = QtWidgets.QMdiSubWindow()
        self.sub_window.setWidget(widget)
        self.sub_window_number += 1
        self.sub_window_amount += 1
        self.table_number += 1
        self.sub_window.setWindowTitle(sub_window_title)
        self.sub_window.setWindowIcon(QtGui.QIcon(sub_window_icon))
        self.mdiArea.addSubWindow(self.sub_window)
        self.sub_window.show()

    def _add_row(self, flag):
        if flag:
            self.current_table.insertRow(self.current_table.currentRow())
        else:
            self.current_table.insertRow(self.current_table.currentRow() + 1)
        self._change_table()

    def _add_column(self, flag):
        if flag:
            self.current_table.insertColumn(self.current_table.currentColumn())
        else:
            self.current_table.insertColumn(self.current_table.currentColumn() + 1)
        self._change_table()

    def _remove_row(self):
        self.current_table.removeRow(self.current_table.currentRow())
        self._change_table()

    def _remove_column(self):
        self.current_table.removeColumn(self.current_table.currentColumn())
        self._change_table()

    def _select_data(self, limits: dict, color: QtGui.QColor):
        pass

    def _add_data(self, target: dict, data: dict):
        pass

    def add_new_sub_window(self):
        new_table = MyTableWidget()
        new_table.itemSelectionChanged.connect(self.select_cell)
        if self.sender().objectName() == 'actionNew':
            self.statusbar.showMessage('Creating new data table...')
            title = 'Data ' + str(self.sub_window_number + 1)
            icon = 'ui/New_Icons/add-file.png'
            new_table.setRowCount(1)
            new_table.setColumnCount(1)
            self._create_sub_window(title, icon, new_table)
        elif self.sender().objectName() == 'actionOutput':
            self.statusbar.showMessage('Creating output table...')
            title = 'Output table'
            icon = 'ui/New_Icons/output.png'
            self._create_sub_window(title, icon, new_table)
            self.actionOutput.setEnabled(False)
        self.current_table = new_table


    def sub_window_change(self):
        self.sub_window = self.mdiArea.activeSubWindow()
        if self.sub_window:
            tabs = self.sub_window.findChild(QtWidgets.QTabWidget, 'tabs')
            if tabs:
                self.current_tabs = tabs
                self.current_tabs.setCurrentIndex(0)
                self.current_table = self.sub_window.widget().findChild(QtWidgets.QTableWidget, 'table1')
            else:
                self.current_table = self.sub_window.widget().findChild(QtWidgets.QTableWidget, 'table')
            self._change_table()

    def tab_change(self, index):
        if index >= 0:
            tab_widget = self.current_tabs
            while isinstance(tab_widget.currentWidget(), MyTabWidget):
                tab_widget = tab_widget.currentWidget()
            self._change_table()
            self.current_table = tab_widget.currentWidget()

    def select_cell(self):
        self.label_currentrowvalue.setText(str(self.current_table.currentRow() + 1))
        self.label_currentcolumnvalue.setText(str(self.current_table.currentColumn() + 1))

    def closeEvent(self, e):
        self.settings.setValue('Geometry', self.saveGeometry())
        self.settings.setValue('WindowState', self.saveState())
        super().closeEvent(e)
