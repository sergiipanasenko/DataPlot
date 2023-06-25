from PyQt5 import QtWidgets, QtGui, QtCore, uic
from my_gui import AbstractForm, InputTableWidget, OutputTableWidget, InputTabWidget
from my_qt_files import MyQtDataFile, MyQtFileGroup


icons = {
    'text': 'ui/New_Icons/text-doc.png',
    'excel': 'ui/New_Icons/excel.png',
    'hdf5': 'ui/New_Icons/hierarchy_diagram.png',
    'matlab': 'ui/New_Icons/mat_file.png'
}


class DataPlotForm(QtWidgets.QMainWindow, AbstractForm):
    def __init__(self):
        # parent initialisation
        super().__init__()

        # ui loading
        uic.loadUi('ui/MyForm5.ui', self)

        # new fields
        self.sub_window = None
        self.input_window_number = 0
        self.output_window_number = 0
        self.sub_window_amount = 0
        self.table_number = 0
        self.current_tabs = None
        self.input_table = None
        self.output_table = None
        self.qt_files = list()
        self.sub_windows = dict()

        # explicit definition of the class attributes
        self.statusbar = self.findChild(QtWidgets.QStatusBar, "statusbar")

        # Settings/Themes
        self.action_default = self.findChild(QtWidgets.QAction, "action_Default")
        self.action_adaptic = self.findChild(QtWidgets.QAction, "action_Adaptic")
        self.action_combinear = self.findChild(QtWidgets.QAction, "action_Combinear")
        self.action_darkeum = self.findChild(QtWidgets.QAction, "action_Darkeum")
        self.action_diplaytap = self.findChild(QtWidgets.QAction, "action_Diplaytap")
        self.action_easycode = self.findChild(QtWidgets.QAction, "action_EasyCode")
        self.action_fibers = self.findChild(QtWidgets.QAction, "action_Fibers")
        self.action_irrorater = self.findChild(QtWidgets.QAction, "action_Irrorater")
        self.action_perstfic = self.findChild(QtWidgets.QAction, "action_Perstfic")

        # File
        self.action_new = self.findChild(QtWidgets.QAction, "action_New")
        self.action_open = self.findChild(QtWidgets.QAction, "action_Open")
        self.action_output = self.findChild(QtWidgets.QAction, "action_Output")
        self.action_save = self.findChild(QtWidgets.QAction, "action_Save")
        self.action_exit = self.findChild(QtWidgets.QAction, "action_Exit")

        # Settings/Font
        self.action_font = self.findChild(QtWidgets.QAction, "action_Font")

        # Window
        self.menu_window = self.findChild(QtWidgets.QMenu, 'menu_Window')
        self.action_tiled = self.findChild(QtWidgets.QAction, "action_Tiled")
        self.action_cascaded = self.findChild(QtWidgets.QAction, "action_Cascaded")

        # Help
        self.action_about = self.findChild(QtWidgets.QAction, "action_About")

        # Table
        self.menu_add = self.findChild(QtWidgets.QMenu, "menu_Add")
        self.menu_remove = self.findChild(QtWidgets.QMenu, "menu_Remove")
        self.action_row_above = self.findChild(QtWidgets.QAction, "action_RowAbove")
        self.action_row_below = self.findChild(QtWidgets.QAction, "action_RowBelow")
        self.action_column_left = self.findChild(QtWidgets.QAction, "action_ColumnLeft")
        self.action_column_right = self.findChild(QtWidgets.QAction, "action_ColumnRight")
        self.action_row = self.findChild(QtWidgets.QAction, "action_Row")
        self.action_column = self.findChild(QtWidgets.QAction, "action_Column")
        self.action_table = (self.menu_add, self.menu_remove,
                             self.action_row_above, self.action_row_below,
                             self.action_column_left, self.action_column_right,
                             self.action_row, self.action_column)

        # Buttons
        self.push_add = self.findChild(QtWidgets.QPushButton, "push_Add")
        self.push_remove = self.findChild(QtWidgets.QPushButton, "push_Remove")
        self.push_reset = self.findChild(QtWidgets.QPushButton, "push_Reset")
        self.push_next = self.findChild(QtWidgets.QPushButton, "push_Next")
        self.push_cancel = self.findChild(QtWidgets.QPushButton, "push_Cancel")

        # Combos
        self.combo_output = self.findChild(QtWidgets.QComboBox, "combo_Output")
        self.combo_values = self.findChild(QtWidgets.QComboBox, "combo_Values")
        self.combo_wise = self.findChild(QtWidgets.QComboBox, "combo_Wise")
        self.combo_col_from = self.findChild(QtWidgets.QComboBox, "combo_ColFrom")
        self.combo_col_to = self.findChild(QtWidgets.QComboBox, "combo_ColTo")
        self.combo_row_from = self.findChild(QtWidgets.QComboBox, "combo_RowFrom")
        self.combo_row_to = self.findChild(QtWidgets.QComboBox, "combo_RowTo")
        self.combo_select = (self.combo_row_from, self.combo_col_from,
                             self.combo_row_to, self.combo_col_to)

        # Labels
        self.label_total_row_value = self.findChild(QtWidgets.QLabel, "label_TotalRowValue")
        self.label_total_column_value = self.findChild(QtWidgets.QLabel, "label_TotalColumnValue")
        self.label_value_group = (self.label_total_row_value,
                                  self.label_total_column_value)

        # Checkboxes
        self.check_data = self.findChild(QtWidgets.QCheckBox, "check_Data")

        # Line Edits
        self.line_min = self.findChild(QtWidgets.QLineEdit, "line_Min")
        self.line_max = self.findChild(QtWidgets.QLineEdit, "line_Max")
        self.line_step = self.findChild(QtWidgets.QLineEdit, "line_Step")
        self.line_step = self.findChild(QtWidgets.QLineEdit, "line_Step")
        self.line_data_cols = self.findChild(QtWidgets.QLineEdit, "line_DataCols")

        # MDI area
        self.mdi_area = self.findChild(QtWidgets.QMdiArea, "mdiArea")

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
        self.themes.addAction(self.action_default)
        self.themes.addAction(self.action_adaptic)
        self.themes.addAction(self.action_combinear)
        self.themes.addAction(self.action_darkeum)
        self.themes.addAction(self.action_diplaytap)
        self.themes.addAction(self.action_easycode)
        self.themes.addAction(self.action_fibers)
        self.themes.addAction(self.action_irrorater)
        self.themes.addAction(self.action_perstfic)

        # action group 2
        self.layout = QtWidgets.QActionGroup(self)
        self.layout.addAction(self.action_tiled)
        self.layout.addAction(self.action_cascaded)

        # action group 3
        self.data_windows = QtWidgets.QActionGroup(self)

        # connections
        self.action_exit.triggered.connect(QtWidgets.qApp.quit)
        self.action_new.triggered.connect(self.add_new_sub_window)
        self.action_open.triggered.connect(self.open)
        self.action_output.triggered.connect(self.add_new_sub_window)
        self.action_save.triggered.connect(self.save_file)

        self.action_default.triggered.connect(lambda: self.set_style(''))
        self.action_adaptic.triggered.connect(lambda: self.set_style('ui/qss/Adaptic.qss'))
        self.action_combinear.triggered.connect(lambda: self.set_style('ui/qss/Combinear.qss'))
        self.action_darkeum.triggered.connect(lambda: self.set_style('ui/qss/Darkeum.qss'))
        self.action_diplaytap.triggered.connect(lambda: self.set_style('ui/qss/Diplaytap.qss'))
        self.action_easycode.triggered.connect(lambda: self.set_style('ui/qss/EasyCode.qss'))
        self.action_fibers.triggered.connect(lambda: self.set_style('ui/qss/Fibers.qss'))
        self.action_irrorater.triggered.connect(lambda: self.set_style('ui/qss/Irrorater.qss'))
        self.action_perstfic.triggered.connect(lambda: self.set_style('ui/qss/Perstfic.qss'))

        self.menu_window.aboutToShow.connect(self.update_windows)
        self.action_tiled.triggered.connect(self.mdi_area.tileSubWindows)
        self.action_tiled.triggered.connect(lambda: self.action_tiled.setChecked(True))
        self.action_cascaded.triggered.connect(self.mdi_area.cascadeSubWindows)
        self.action_cascaded.triggered.connect(lambda: self.action_cascaded.setChecked(True))

        self.action_row_above.triggered.connect(lambda: self._add_row(True))
        self.action_row_below.triggered.connect(lambda: self._add_row(False))
        self.action_column_left.triggered.connect(lambda: self._add_column(True))
        self.action_column_right.triggered.connect(lambda: self._add_column(False))
        self.action_row.triggered.connect(self._remove_row)
        self.action_column.triggered.connect(self._remove_column)

        self.push_add.clicked.connect(self.change_values)
        self.push_remove.clicked.connect(self.change_values)
        self.push_reset.clicked.connect(self.change_values)
        self.push_cancel.clicked.connect(QtWidgets.qApp.quit)

        self.mdi_area.subWindowActivated.connect(self.change_sub_window)

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

    def save_file(self):
        pass

    def _connect_signals(self, current_widget):
        if isinstance(current_widget, InputTabWidget):
            current_widget.currentChanged.connect(self.tab_change)
            for index in range(current_widget.count()):
                child_widget = current_widget.widget(index)
                self._connect_signals(child_widget)

    def update_windows(self):
        menu: QtWidgets.QMenu = self.menu_window
        menu.clear()
        menu.addActions((self.action_tiled, self.action_cascaded))
        window_list = self.mdi_area.subWindowList()
        new_action: QtWidgets.QAction
        if window_list:
            menu.addSeparator()
            for window in window_list:
                window_title = window.windowTitle()
                window_icon = window.windowIcon()
                new_action = menu.addAction(window_icon, window_title)
                new_action.setCheckable(True)
                new_action.setChecked(False)
                if window == self.mdi_area.activeSubWindow():
                    new_action.setChecked(True)
                self.data_windows.addAction(new_action)
                self.sub_windows[new_action.iconText()] = window
                new_action.triggered.connect(lambda: self.mdi_area.setActiveSubWindow(
                    self.sub_windows[self.sender().iconText()]))

    def _change_table(self):
        self._combo_label_reset()
        if self.input_table:
            col_number = self.input_table.columnCount()
            row_number = self.input_table.rowCount()
            if col_number and row_number:
                row_number_list = list(map(str, range(1, row_number + 1)))
                col_number_list = list(map(str, range(1, col_number + 1)))
                self.combo_row_from.addItems(row_number_list)
                self.combo_row_from.setCurrentIndex(0)
                self.combo_col_from.addItems(col_number_list)
                self.combo_col_from.setCurrentIndex(0)
                self.combo_row_to.addItems(row_number_list)
                self.combo_row_to.setCurrentIndex(len(row_number_list) - 1)
                self.combo_col_to.addItems(col_number_list)
                self.combo_col_to.setCurrentIndex(len(col_number_list) - 1)
                self.label_total_row_value.setText(str(self.input_table.rowCount()))
                self.label_total_column_value.setText(str(self.input_table.columnCount()))

    def _create_sub_window(self, sub_window_title, sub_window_icon, widget):
        if not self.menu_add.isEnabled():
            for item in self.action_table:
                item.setEnabled(True)
        self.sub_window = QtWidgets.QMdiSubWindow()
        self.sub_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.sub_window.setWidget(widget)
        if self.sender().objectName() == 'action_Output':
            self.output_window_number += 1
            self.combo_output.addItem(f'Output {self.output_window_number + 1}')
        else:
            self.input_window_number += 1
        self.sub_window_amount += 1
        self.table_number += 1
        self.sub_window.setWindowTitle(sub_window_title)
        self.sub_window.setWindowIcon(QtGui.QIcon(sub_window_icon))
        self.mdi_area.addSubWindow(self.sub_window)
        self.sub_window.show()

    def _add_row(self, flag):
        if flag:
            self.input_table.insertRow(self.input_table.currentRow())
        else:
            self.input_table.insertRow(self.input_table.currentRow() + 1)
        self._change_table()

    def _add_column(self, flag):
        if flag:
            self.input_table.insertColumn(self.input_table.currentColumn())
        else:
            self.input_table.insertColumn(self.input_table.currentColumn() + 1)
        self._change_table()

    def _remove_row(self):
        self.input_table.removeRow(self.input_table.currentRow())
        self._change_table()

    def _remove_column(self):
        self.input_table.removeColumn(self.input_table.currentColumn())
        self._change_table()

    def change_values(self):
        index = self.combo_values.currentIndex()
        if isinstance(self.input_table, InputTableWidget):
            if self.sender() == self.push_reset:
                self.input_table.reset_values(index)
            else:
                start_row = int(self.combo_row_from.currentText()) - 1
                start_col = int(self.combo_col_from.currentText()) - 1
                end_row = int(self.combo_row_to.currentText())
                end_col = int(self.combo_col_to.currentText())
                limits = (start_row, start_col, end_row, end_col)
                if self.sender() == self.push_add:
                    row_wise = True
                    if self.combo_wise.currentText() == 'Columnwise':
                        row_wise = False
                    values = self.input_table.add_values(limits, index, row_wise)
                    if self.output_table is None:
                        self.action_output.triggered.emit()
                    col_number = None
                    if index == 3 and not self.check_data.isChecked():
                        col_number = int(self.line_data_cols.text())
                    self.output_table.add_values(self.input_table, values,
                                                 index, col_number)
                elif self.sender() == self.push_remove:
                    self.input_table.remove_values(limits, index)

    def add_new_sub_window(self):
        if self.sender().objectName() == 'action_New':
            new_table = InputTableWidget()
            self.statusbar.showMessage('Creating new input data table...')
            title = f'Input {self.input_window_number + 1}'
            icon = 'ui/New_Icons/add-file.png'
            new_table.setRowCount(1)
            new_table.setColumnCount(1)
            self.input_table = new_table
            self.input_table.repaint_table()
            self._create_sub_window(title, icon, self.input_table)
        elif self.sender().objectName() == 'action_Output':
            new_table = OutputTableWidget()
            self.statusbar.showMessage('Creating new output data table...')
            title = f'Output {self.output_window_number + 1}'
            icon = 'ui/New_Icons/output.png'
            self.output_table = new_table
            self.output_table.repaint_table()
            self._create_sub_window(title, icon, self.output_table)
        self._change_table()

    def change_sub_window(self):
        self.sub_window = self.mdi_area.activeSubWindow()
        if self.sub_window:
            sub_window_widget = self.sub_window.widget()
            if isinstance(sub_window_widget, InputTabWidget):
                self.current_tabs = self.sub_window.widget()
                self.current_tabs.currentChanged.emit(self.current_tabs.currentIndex())
            if isinstance(sub_window_widget, InputTableWidget):
                self.current_tabs = None
                self.input_table = sub_window_widget
            self._change_table()
        else:
            for item in self.action_table:
                item.setEnabled(False)
            self._combo_label_reset()

    def _combo_label_reset(self):
        for combo in (self.combo_select):
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
            self.input_table = tab_widget.widget(current_index)
            self._change_table()

    def closeEvent(self, e):
        self.settings.setValue('Geometry', self.saveGeometry())
        self.settings.setValue('WindowState', self.saveState())
        super().closeEvent(e)
