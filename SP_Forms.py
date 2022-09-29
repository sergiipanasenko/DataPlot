from os.path import splitext
from PyQt5 import QtCore, QtWidgets, QtGui, uic
from MyFiles import MyDataFile, MyExcelFile, MyHDF5File
from MyGUI import MyAbstractForm, MyTableWidget, MyTabWidget


class MyForm3(QtWidgets.QMainWindow, MyAbstractForm):
    def __init__(self):
        # parent initialisation
        super().__init__()

        # UI loading
        uic.loadUi('UI/MyForm3.ui', self)

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
        self.actionExcel = self.findChild(QtWidgets.QAction, "actionExcel")
        self.actionHDF5 = self.findChild(QtWidgets.QAction, "actionHDF5")
        self.actionOutput = self.findChild(QtWidgets.QAction, "actionOutput")
        self.actionSave = self.findChild(QtWidgets.QAction, "actionSave")
        self.actionExit = self.findChild(QtWidgets.QAction, "actionExit")
        self.actionFont = self.findChild(QtWidgets.QAction, "actionFont")
        self.actionTiled = self.findChild(QtWidgets.QAction, "actionTiled")
        self.actionCascaded = self.findChild(QtWidgets.QAction, "actionCascaded")
        self.actionAbout = self.findChild(QtWidgets.QAction, "actionAbout")
        self.actionRow_above = self.findChild(QtWidgets.QAction, "actionRow_above")
        self.actionRow_below = self.findChild(QtWidgets.QAction, "actionRow_below")
        self.actionColumn_left = self.findChild(QtWidgets.QAction, "actionColumn_left")
        self.actionColumn_right = self.findChild(QtWidgets.QAction, "actionColumn_right")
        self.actionRow = self.findChild(QtWidgets.QAction, "actionRow")
        self.actionColumn = self.findChild(QtWidgets.QAction, "actionColumn")

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
        self.combo_Datacolfrom = self.findChild(QtWidgets.QComboBox, "combo_Datacolfrom")
        self.combo_Datacolto = self.findChild(QtWidgets.QComboBox, "combo_Datacolto")
        self.combo_Datarowfrom = self.findChild(QtWidgets.QComboBox, "combo_Datarowfrom")
        self.combo_Datarowto = self.findChild(QtWidgets.QComboBox, "combo_Datarowto")
        self.combo_wise = self.findChild(QtWidgets.QComboBox, "combo_wise")

        self.label_totalrowvalue = self.findChild(QtWidgets.QLabel, "label_totalrowvalue")
        self.label_totalcolumnvalue = self.findChild(QtWidgets.QLabel, "label_totalcolumnvalue")
        self.label_currentrowvalue = self.findChild(QtWidgets.QLabel, "label_currentrowvalue")
        self.label_currentcolumnvalue = self.findChild(QtWidgets.QLabel, "label_currentcolumnvalue")

        self.mdiArea = self.findChild(QtWidgets.QMdiArea, "mdiArea")

        self.menuAdd = self.findChild(QtWidgets.QMenu, "menuAdd")
        self.menuRemove = self.findChild(QtWidgets.QMenu, "menuRemove")

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
        self.actionExcel.triggered.connect(self.open_excel_file)
        self.actionHDF5.triggered.connect(self.open_h5_file)
        self.actionOutput.triggered.connect(self.add_new_sub_window)
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
        new_table_widget = MyTableWidget()
        new_table_widget.itemSelectionChanged.connect(self.select_cell)
        if self.sender().objectName() == 'actionNew':
            self.statusbar.showMessage('Creating new data table...')
            title = 'Data ' + str(self.sub_window_number + 1)
            icon = 'UI/New_Icons/add-file.png'
            new_table_widget.setRowCount(1)
            new_table_widget.setColumnCount(1)
            self._create_sub_window(title, icon, new_table_widget)
        elif self.sender().objectName() == 'actionOutput':
            self.statusbar.showMessage('Creating output table...')
            title = 'Output table'
            icon = 'UI/New_Icons/output.png'
            self._create_sub_window(title, icon, new_table_widget)
            self.actionOutput.setEnabled(False)

    def open_data_file(self):
        self.statusbar.showMessage('Data loading from file...')
        status = True
        while status:
            recent_directory = self.settings.value('recent_directory', type=str)
            file = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                         caption="Open data file",
                                                         directory=recent_directory,
                                                         filter="All files (*);;Text files (*.dat *.txt)",
                                                         initialFilter="Text files (*.dat *.txt)")
            if file[0]:
                self.settings.setValue('recent_directory', QtCore.QFileInfo(file[0]).path())
                raw_path = r'{}'.format(file[0])
                data_file = MyDataFile(raw_path)
                try:
                    data_file.read_data()
                    title = raw_path
                    icon = 'UI/New_Icons/text-doc.png'
                    new_table_widget = MyTableWidget()
                    new_table_widget.itemSelectionChanged.connect(self.select_cell)
                    self._create_sub_window(title, icon, new_table_widget)
                    new_table_widget.add_data(data_file.data)
                    status = False
                except Exception as e:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("Data File Open Error")
                    msg.setInformativeText(f"Unable to open {file[0]}. This is probably not text data file")
                    msg.setDetailedText(str(e))
                    msg.setWindowTitle("Error")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Ok)
                    msg.exec_()
                    if msg.clickedButton().text() == 'OK':
                        status = False
            else:
                status = False

    def save_file(self):
        file = QtWidgets.QFileDialog.getSaveFileName(parent=self,
                                                     caption="Save data file",
                                                     directory=QtCore.QDir.currentPath(),
                                                     filter="Text files (*.dat *.txt)",
                                                     initialFilter="Text files (*.dat *.txt)")

    def open_excel_file(self):
        self.statusbar.showMessage('Excel Book loading from file...')
        status = True
        while status:
            recent_directory = self.settings.value('recent_directory', type=str)
            file = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                         caption="Open Excel file",
                                                         directory=recent_directory,
                                                         filter="All files (*.*);;"
                                                                "Excel Workbooks (*.xlsx *.xlsm);;"
                                                                "Excel Binary Workbooks (*.xlsb);;"
                                                                "Excel templates (*.xltx *.xltm);;"
                                                                "Excel Workbooks 97-2003 (*.xls)",
                                                         initialFilter="Excel Workbooks (*.xlsx *.xlsm)")
            if file[0]:
                self.settings.setValue('recent_directory', QtCore.QFileInfo(file[0]).path())
                raw_path = r'{}'.format(file[0])
                file_ext = splitext(raw_path)[1]
                excel_file = MyExcelFile(raw_path)
                try:
                    if file_ext in ('.xlsx', '.xlsm', '.xltx', '.xltm'):
                        excel_file.read_new_book()
                    elif file_ext == '.xlsb':
                        excel_file.read_binary_book()
                    elif file_ext == '.xls':
                        excel_file.read_old_book()
                    else:
                        raise Exception(f"This file has not Excel extension ({file_ext}).")
                    title = raw_path
                    icon = 'UI/New_Icons/excel.png'
                    self.current_tabs = MyTabWidget()
                    self.current_tabs.currentChanged.connect(self.tab_change)
                    self.current_tabs.add_data(excel_file.data)
                    self._create_sub_window(title, icon, self.current_tabs)
                    status = False
                except Exception as e:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("Excel File Open Error")
                    msg.setInformativeText(f"File {file[0]} is not Excel file")
                    msg.setDetailedText(str(e))
                    msg.setWindowTitle("Error")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Ok)
                    msg.exec_()
                    if msg.clickedButton().text() == 'OK':
                        status = False
            else:
                status = False

    def open_h5_file(self):
        self.statusbar.showMessage('HDF5 data loading from file...')
        status = True
        while status:
            recent_directory = self.settings.value('recent_directory', type=str)
            file = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                         caption="Open HDF5 file",
                                                         directory=recent_directory,
                                                         filter="All files (*.*);;"
                                                                "HDF5 files (*.h5 *.hdf *.hdf5)",
                                                         initialFilter="HDF5 files (*.h5 *.hdf *.hdf5)")
            if file[0]:
                self.settings.setValue('recent_directory', QtCore.QFileInfo(file[0]).path())
                raw_path = r'{}'.format(file[0])
                h5_file = MyHDF5File(raw_path)
                try:
                    h5_file.read_h5_data()
                    title = raw_path
                    icon = 'UI/New_Icons/hierarchy_diagram.png'
                    self.current_tabs = MyTabWidget()
                    self.current_tabs.currentChanged.connect(self.tab_change)
                    self.current_tabs.add_data(h5_file.data)
                    self._create_sub_window(title, icon, self.current_tabs)
                    status = False
                except Exception as e:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("HDF% File Open Error")
                    msg.setInformativeText(f"File {file[0]} is not HDF5 file")
                    msg.setDetailedText(str(e))
                    msg.setWindowTitle("Error")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Ok)
                    msg.exec_()
                    if msg.clickedButton().text() == 'OK':
                        status = False
            else:
                status = False

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
            self.current_table = self.current_tabs.findChild(QtWidgets.QTableWidget, f"table{index + 1}")
            self._change_table()

    def select_cell(self):
        self.label_currentrowvalue.setText(str(self.current_table.currentRow() + 1))
        self.label_currentcolumnvalue.setText(str(self.current_table.currentColumn() + 1))
