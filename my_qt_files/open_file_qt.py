from PyQt5 import QtWidgets

from my_gui import MyTabWidget


def open_file(self):
    file_type = {}

    status = True
    while status:
        recent_directory = self.settings.value('recent_directory', type=str)
        file = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                                                     caption="Open data file",
                                                     directory=recent_directory,
                                                     filter="All files (*.*);;"
                                                            "Text files (*.dat *.txt);;"
                                                            "Excel Workbooks (*.xlsx *.xlsm);;"
                                                            "Excel Binary Workbooks (*.xlsb);;"
                                                            "Excel templates (*.xltx *.xltm);;"
                                                            "Excel Workbooks 97-2003 (*.xls)"
                                                            "HDF5 files (*.h5 *.hdf *.hdf5)",
                                                     initialFilter="All files (*.*)")


def _open_data_file(self):
    self.statusbar.showMessage('Data loading from file...')

    if file[0]:
        self.settings.setValue('recent_directory', QtCore.QFileInfo(file[0]).path())
        raw_path = r'{}'.format(file[0])
        data_file = MyDataFile(raw_path)
        try:
            data_file.read_data()
            title = raw_path
            icon = 'ui/New_Icons/text-doc.png'
            new_table = MyTableWidget()
            new_table.itemSelectionChanged.connect(self.select_cell)
            self._create_sub_window(title, icon, new_table)
            new_table.add_data(data_file.data)
            self.current_table = new_table
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


def _open_excel_file(self):
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
                icon = 'ui/New_Icons/excel.png'
                self.current_tabs = MyTabWidget()
                self.current_tabs.currentChanged.connect(self.tab_change)
                self.current_tabs.add_data(excel_file.data)
                self._create_sub_window(title, icon, self.current_tabs)
                self.current_table = self.current_tabs.currentWidget()
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


def _open_h5_file(self):
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
                icon = 'ui/New_Icons/hierarchy_diagram.png'
                new_tab_widget = MyTabWidget()
                new_tab_widget.add_data(h5_file.data)
                self._create_sub_window(title, icon, new_tab_widget)
                self.current_tabs = new_tab_widget
                while isinstance(new_tab_widget, MyTabWidget):
                    new_tab_widget.currentChanged.connect(self.tab_change)
                    new_tab_widget = new_tab_widget.new_tab
                self.current_table = new_tab_widget
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
