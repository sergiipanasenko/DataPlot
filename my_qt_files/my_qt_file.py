from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QFileInfo, QDir
from my_qt_files.my_files import MyDataFile

file_desc = (
    "All files (*.*)",
    "Text files (*.dat *.txt)",
    "Excel Workbooks (*.xlsx *.xlsm)",
    "Excel Binary Workbooks (*.xlsb)",
    "Excel templates (*.xltx *.xltm)",
    "Excel Workbooks 97-2003 (*.xls)",
    "HDF5 files (*.h5 *.hdf *.hdf5)"
)


class MyQtFile:
    def __init__(self, parent, recent_dir=None):
        super().__init__()
        self.recent_dir = recent_dir
        self.parent = parent

    def open_file(self):
        try_open = True
        while try_open:
            file = QFileDialog.getOpenFileName(
                parent=self.parent,
                caption="Open data file",
                directory=self.recent_dir,
                filter=';;'.join(file_desc),
                initialFilter=file_desc[0])
            if file[0]:
                self.parent.settings.setValue(
                    'recent_directory', QFileInfo(file[0]).path())
                raw_path = r'{}'.format(file[0])
                data_file = MyDataFile(raw_path)
                try:
                    data_file.read_data()
                    print(data_file.get_data())
                except Exception as e:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Data File Open Error")
                    msg.setInformativeText(
                        f"Unable to open {file[0]}. "
                        f"This file is probably not from group {file[1]}")
                    msg.setDetailedText(str(e))
                    msg.setWindowTitle("Error")
                    msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Ok)
                    msg.exec_()
                    if msg.clickedButton().text() == 'OK':
                        try_open = False
            else:
                try_open = False

    def save_file(self):
        file = QFileDialog.getSaveFileName(
            parent=self.parent,
            caption="Save data file",
            directory=QDir.currentPath(),
            filter="Text files (*.dat *.txt)",
            initialFilter="Text files (*.dat *.txt)")


# title = raw_path
# icon = 'ui/New_Icons/text-doc.png'
# new_table = MyTableWidget()
# new_table.itemSelectionChanged.connect(self.select_cell)
# self._create_sub_window(title, icon, new_table)
# new_table.add_data(data_file.data)
# self.current_table = new_table
# try:
# if file_ext in ('.xlsx', '.xlsm', '.xltx', '.xltm'):
# else:
# raise Exception(f"This file has not Excel extension ({file_ext}).")
# title = raw_path
# icon = 'ui/New_Icons/excel.png'
# self.current_tabs = MyTabWidget()
# self.current_tabs.currentChanged.connect(self.tab_change)
# self.current_tabs.add_data(excel_file.data)
# self._create_sub_window(title, icon, self.current_tabs)
# self.current_table = self.current_tabs.currentWidget()
