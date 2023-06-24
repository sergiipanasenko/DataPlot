from PyQt5 import QtWidgets, QtGui, QtCore, uic
from my_gui import MyAbstractForm, InputTableWidget, OutputTableWidget, InputTabWidget
from my_qt_files import MyQtDataFile, MyQtFileGroup


icons = {
    'text': 'ui/New_Icons/text-doc.png',
    'excel': 'ui/New_Icons/excel.png',
    'hdf5': 'ui/New_Icons/hierarchy_diagram.png',
    'matlab': 'ui/New_Icons/mat_file.png'
}


class MyDataPlotForm(QtWidgets.QMainWindow, MyAbstractForm):
    def __init__(self):
        # parent initialisation
        super().__init__()

        # ui loading
        uic.loadUi('ui/MyForm4.ui', self)

        # new fields
        self.sub_window = None
        self.input_window_number = 0
        self.output_window_number = 0
        self.sub_window_amount = 0
        self.table_number = 0
        self.current_tabs = None
        self.current_table = None
        self.qt_files = list()
        self.sub_windows = dict()

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
        self.menuWindow = self.findChild(QtWidgets.QMenu, 'menuWindow')
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
        self.action_table = (self.menuAdd, self.menuRemove,
                             self.actionRow_above, self.actionRow_below,
                             self.actionColumn_left, self.actionColumn_right,
                             self.actionRow, self.actionColumn)

        # Buttons
        self.push_add = self.findChild(QtWidgets.QPushButton, "push_add")
        self.push_remove = self.findChild(QtWidgets.QPushButton, "push_remove")
        self.push_reset = self.findChild(QtWidgets.QPushButton, "push_reset")
        self.push_next = self.findChild(QtWidgets.QPushButton, "push_next")
        self.push_cancel = self.findChild(QtWidgets.QPushButton, "push_cancel")

        # Combos
        self.combo_wise = self.findChild(QtWidgets.QComboBox, "combo_wise")
        self.combo_Xcolfrom = self.findChild(QtWidgets.QComboBox, "combo_Xcolfrom")
        self.combo_Xcolto = self.findChild(QtWidgets.QComboBox, "combo_Xcolto")
        self.combo_Xrowfrom = self.findChild(QtWidgets.QComboBox, "combo_Xrowfrom")
        self.combo_Xrowto = self.findChild(QtWidgets.QComboBox, "combo_Xrowto")
        self.combo_Ycolfrom = self.findChild(QtWidgets.QComboBox, "combo_Ycolfrom")
        self.combo_Ycolto = self.findChild(QtWidgets.QComboBox, "combo_Ycolto")
        self.combo_Yrowfrom = self.findChild(QtWidgets.QComboBox, "combo_Yrowfrom")
        self.combo_Yrowto = self.findChild(QtWidgets.QComboBox, "combo_Yrowto")
        self.combo_Scolfrom = self.findChild(QtWidgets.QComboBox, "combo_Scolfrom")
        self.combo_Scolto = self.findChild(QtWidgets.QComboBox, "combo_Scolto")
        self.combo_Srowfrom = self.findChild(QtWidgets.QComboBox, "combo_Srowfrom")
        self.combo_Srowto = self.findChild(QtWidgets.QComboBox, "combo_Srowto")
        self.combo_Datacolfrom = self.findChild(QtWidgets.QComboBox, "combo_Datacolfrom")
        self.combo_Datacolto = self.findChild(QtWidgets.QComboBox, "combo_Datacolto")
        self.combo_Datarowfrom = self.findChild(QtWidgets.QComboBox, "combo_Datarowfrom")
        self.combo_Datarowto = self.findChild(QtWidgets.QComboBox, "combo_Datarowto")
        self.combo_wise = self.findChild(QtWidgets.QComboBox, "combo_wise")
        self.combo_rowfrom_group = (self.combo_Xrowfrom, self.combo_Yrowfrom,
                                    self.combo_Srowfrom, self.combo_Datarowfrom)
        self.combo_colfrom_group = (self.combo_Xcolfrom, self.combo_Ycolfrom,
                                    self.combo_Scolfrom, self.combo_Datacolfrom)
        self.combo_rowto_group = (self.combo_Xrowto, self.combo_Yrowto,
                                 self.combo_Srowto, self.combo_Datarowto)
        self.combo_colto_group = (self.combo_Xcolto, self.combo_Ycolto,
                                  self.combo_Scolto, self.combo_Datacolto)
        self.combo_select = {
            '0': (self.combo_Xrowfrom, self.combo_Xcolfrom,
                  self.combo_Xrowto, self.combo_Xcolto),
            '1': (self.combo_Yrowfrom, self.combo_Ycolfrom,
                  self.combo_Yrowto, self.combo_Ycolto),
            '2': (self.combo_Srowfrom, self.combo_Scolfrom,
                  self.combo_Srowto, self.combo_Scolto),
            '3': (self.combo_Datarowfrom, self.combo_Datacolfrom,
                  self.combo_Datarowto, self.combo_Datacolto)}

        # Labels
        self.label_totalrowvalue = self.findChild(QtWidgets.QLabel, "label_totalrowvalue")
        self.label_totalcolumnvalue = self.findChild(QtWidgets.QLabel, "label_totalcolumnvalue")
        self.label_currentrowvalue = self.findChild(QtWidgets.QLabel, "label_currentrowvalue")
        self.label_currentcolumnvalue = self.findChild(QtWidgets.QLabel, "label_currentcolumnvalue")
        self.label_value_group = (self.label_totalrowvalue,
                                  self.label_totalcolumnvalue,
                                  self.label_currentrowvalue,
                                  self.label_currentcolumnvalue)
        # Tab widgets
        self.tab_select = self.findChild(QtWidgets.QTabWidget, "tab_select")
        self.tab_minmax = self.findChild(QtWidgets.QTabWidget, "tab_minmax")

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

        # action group 1
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

        # action group 2
        self.layout = QtWidgets.QActionGroup(self)
        self.layout.addAction(self.actionTiled)
        self.layout.addAction(self.actionCascaded)

        # action group 3
        self.data_windows = QtWidgets.QActionGroup(self)

        # connections
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.actionNew.triggered.connect(self.add_new_sub_window)
        self.actionOpen.triggered.connect(self.open)
        self.actionOutput.triggered.connect(self.add_new_sub_window)
        # self.actionSave.triggered.connect(self.save_file)

        self.actionDefault.triggered.connect(lambda: self.set_style(''))
        self.actionAdaptic.triggered.connect(lambda: self.set_style('ui/qss/Adaptic.qss'))
        self.actionCombinear.triggered.connect(lambda: self.set_style('ui/qss/Combinear.qss'))
        self.actionDarkeum.triggered.connect(lambda: self.set_style('ui/qss/Darkeum.qss'))
        self.actionDiplaytap.triggered.connect(lambda: self.set_style('ui/qss/Diplaytap.qss'))
        self.actionEasyCode.triggered.connect(lambda: self.set_style('ui/qss/EasyCode.qss'))
        self.actionFibers.triggered.connect(lambda: self.set_style('ui/qss/Fibers.qss'))
        self.actionIrrorater.triggered.connect(lambda: self.set_style('ui/qss/Irrorater.qss'))
        self.actionPerstfic.triggered.connect(lambda: self.set_style('ui/qss/Perstfic.qss'))

        self.menuWindow.aboutToShow.connect(self.update_windows)
        self.actionTiled.triggered.connect(self.mdiArea.tileSubWindows)
        self.actionTiled.triggered.connect(lambda: self.actionTiled.setChecked(True))
        self.actionCascaded.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.actionCascaded.triggered.connect(lambda: self.actionCascaded.setChecked(True))

        self.actionRow_above.triggered.connect(lambda: self._add_row(True))
        self.actionRow_below.triggered.connect(lambda: self._add_row(False))
        self.actionColumn_left.triggered.connect(lambda: self._add_column(True))
        self.actionColumn_right.triggered.connect(lambda: self._add_column(False))
        self.actionRow.triggered.connect(self._remove_row)
        self.actionColumn.triggered.connect(self._remove_column)

        self.push_add.clicked.connect(self.change_values)
        self.push_remove.clicked.connect(self.change_values)
        self.push_reset.clicked.connect(self.change_values)
        self.push_cancel.clicked.connect(QtWidgets.qApp.quit)

        self.mdiArea.subWindowActivated.connect(self.change_sub_window)

    def open(self):
        recent_directory = self.settings.value('recent_directory', type=str)
        self.statusbar.showMessage('Input data loading from file...')
        qt_file_group = MyQtFileGroup(self)
        qt_file_group.set_file_info(recent_directory)
        for file_name in qt_file_group.get_file_names():
            qt_file = MyQtDataFile(file_name, qt_file_group.get_file_type())
            qt_file.thread_read_data()
            qt_file.finished.connect(self._post_open)
            qt_file.needed_to_retry.connect(self.open)
            self.qt_files.append(qt_file)

    def _post_open(self):
        sender = self.sender()
        title = f'Input {self.input_window_number + 1}. {sender.get_file_name()}'
        icon = icons[sender.get_file_type()]
        self.current_tabs = InputTabWidget()
        self.current_tabs.add_data(sender.get_data())
        self._connect_signals(self.current_tabs)
        self._create_sub_window(title, icon, self.current_tabs)
        self.statusbar.showMessage('')
        self.current_tabs.add_data_finished.connect(
            lambda: self.qt_files.remove(sender))

    def _connect_signals(self, current_widget):
        if isinstance(current_widget, InputTabWidget):
            current_widget.currentChanged.connect(self.tab_change)
            for index in range(current_widget.count()):
                child_widget = current_widget.widget(index)
                self._connect_signals(child_widget)
        if isinstance(current_widget, InputTableWidget):
            current_widget.cellClicked.connect(self.select_cell)

    def update_windows(self):
        menu: QtWidgets.QMenu = self.menuWindow
        menu.clear()
        menu.addActions((self.actionTiled, self.actionCascaded))
        window_list = self.mdiArea.subWindowList()
        new_action: QtWidgets.QAction
        if window_list:
            menu.addSeparator()
            for window in window_list:
                window_title = window.windowTitle()
                window_icon = window.windowIcon()
                new_action = menu.addAction(window_icon, window_title)
                new_action.setCheckable(True)
                new_action.setChecked(False)
                if window == self.mdiArea.activeSubWindow():
                    new_action.setChecked(True)
                self.data_windows.addAction(new_action)
                self.sub_windows[new_action.iconText()] = window
                new_action.triggered.connect(lambda: self.mdiArea.setActiveSubWindow(
                    self.sub_windows[self.sender().iconText()]))

    def _change_table(self):
        self._combo_label_reset()
        if self.current_table:
            col_number = self.current_table.columnCount()
            row_number = self.current_table.rowCount()
            if col_number and row_number:
                row_number_list = list(map(str, range(1, row_number + 1)))
                col_number_list = list(map(str, range(1, col_number + 1)))
                for combo_row_from in self.combo_rowfrom_group:
                    combo_row_from.addItems(row_number_list)
                    combo_row_from.setCurrentIndex(0)
                for combo_col_from in self.combo_colfrom_group:
                    combo_col_from.addItems(col_number_list)
                    combo_col_from.setCurrentIndex(0)
                for combo_row_to in self.combo_rowto_group:
                    combo_row_to.addItems(row_number_list)
                    combo_row_to.setCurrentIndex(len(row_number_list) - 1)
                for combo_col_to in self.combo_colto_group:
                    combo_col_to.addItems(col_number_list)
                    combo_col_to.setCurrentIndex(len(col_number_list) - 1)
                self.label_totalrowvalue.setText(str(self.current_table.rowCount()))
                self.label_totalcolumnvalue.setText(str(self.current_table.columnCount()))

    def _create_sub_window(self, sub_window_title, sub_window_icon, widget):
        if not self.menuAdd.isEnabled():
            for item in self.action_table:
                item.setEnabled(True)
        self.sub_window = QtWidgets.QMdiSubWindow()
        self.sub_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.sub_window.setWidget(widget)
        if self.sender().objectName() == 'actionOutput':
            self.output_window_number += 1
        if self.sender().objectName() == 'actionNew':
            self.input_window_number += 1
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
        self._paint_output_table()

    def _add_column(self, flag):
        if flag:
            self.current_table.insertColumn(self.current_table.currentColumn())
        else:
            self.current_table.insertColumn(self.current_table.currentColumn() + 1)
        self._change_table()
        self._paint_output_table()

    def _remove_row(self):
        self.current_table.removeRow(self.current_table.currentRow())
        self._paint_output_table()
        self._change_table()

    def _remove_column(self):
        self.current_table.removeColumn(self.current_table.currentColumn())
        self._paint_output_table()
        self._change_table()

    def change_values(self):
        index = self.tab_select.currentIndex()
        if isinstance(self.current_table, InputTableWidget):
            if self.sender() == self.push_reset:
                self.current_table.reset_values(index)
                return
            combos = self.combo_select[str(index)]
            start_row = int(combos[0].currentText()) - 1
            start_col = int(combos[1].currentText()) - 1
            end_row = int(combos[2].currentText())
            end_col = int(combos[3].currentText())
            limits = (start_row, start_col, end_row, end_col)
            if self.sender() == self.push_add:
                row_wise = True
                if self.combo_wise.currentText() == 'Columnwise':
                    row_wise = False
                self.current_table.add_values(limits, index, row_wise)
                return
            if self.sender() == self.push_remove:
                self.current_table.remove_values(limits, index)
                return

    def add_new_sub_window(self):
        new_table = InputTableWidget()
        title = None
        icon = None
        if self.sender().objectName() == 'actionNew':
            self.statusbar.showMessage('Creating new input data table...')
            title = f'Input {self.input_window_number + 1}'
            icon = 'ui/New_Icons/add-file.png'
            new_table.setRowCount(1)
            new_table.setColumnCount(1)
        elif self.sender().objectName() == 'actionOutput':
            self.statusbar.showMessage('Creating new output data table...')
            title = f'Output {self.output_window_number + 1}'
            icon = 'ui/New_Icons/output.png'
            new_table.setRowCount(2)
            new_table.setColumnCount(3)
        self._create_sub_window(title, icon, new_table)
        self._paint_output_table()
        self.current_table = new_table
        self._paint_output_table()
        self._change_table()
        self._connect_signals(self.current_table)

    def change_sub_window(self):
        self.sub_window = self.mdiArea.activeSubWindow()
        if self.sub_window:
            sub_window_widget = self.sub_window.widget()
            if isinstance(sub_window_widget, InputTabWidget):
                self.current_tabs = self.sub_window.widget()
                self.current_tabs.currentChanged.emit(self.current_tabs.currentIndex())
            if isinstance(sub_window_widget, InputTableWidget):
                self.current_tabs = None
                self.current_table = sub_window_widget
            self._change_table()
        else:
            for item in self.action_table:
                item.setEnabled(False)
            self._combo_label_reset()

    def _combo_label_reset(self):
        for combo in (self.combo_rowfrom_group + self.combo_colfrom_group +
                      self.combo_colto_group + self.combo_rowto_group):
            combo.clear()
        for label_value in self.label_value_group:
            label_value.setText(str(0))

    def tab_change(self, index):
        if index >= 0:
            tab_widget = self.sender()
            current_index = index
            while isinstance(tab_widget.widget(current_index), InputTabWidget):
                tab_widget = tab_widget.currentWidget()
                current_index = tab_widget.currentIndex()
            self.current_table = tab_widget.widget(current_index)
            self._change_table()
            self.select_cell()

    def select_cell(self):
        table = self.current_table
        if table:
            self.label_currentrowvalue.setText(str(table.currentRow() + 1))
            self.label_currentcolumnvalue.setText(str(table.currentColumn() + 1))

    def closeEvent(self, e):
        self.settings.setValue('Geometry', self.saveGeometry())
        self.settings.setValue('WindowState', self.saveState())
        super().closeEvent(e)

    def _paint_output_table(self):
        sub_window = self.mdiArea.activeSubWindow()
        if sub_window:
            sub_window_title = sub_window.windowTitle()
            if 'Output' in sub_window_title:
                table = self.current_table
                for ind_row in range(table.rowCount()):
                    for ind_col in range(table.columnCount()):
                        if table.item(ind_row, ind_col) is None:
                            table.setItem(ind_row, ind_col, QtWidgets.QTableWidgetItem())
                        if ind_row > 0 and ind_col == 0:
                            table.item(ind_row, ind_col).setBackground(self.XChooseColor)
                        if ind_row > 0 and ind_col == 1:
                            table.item(ind_row, ind_col).setBackground(self.SChooseColor)
                        if ind_row == 0 and ind_col > 1:
                            table.item(ind_row, ind_col).setBackground(self.YChooseColor)
                        if ind_row > 0 and ind_col > 1:
                            table.item(ind_row, ind_col).setBackground(self.DataChooseColor)

