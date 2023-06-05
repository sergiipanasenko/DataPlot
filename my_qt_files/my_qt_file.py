from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QFileInfo, QDir, QObject, QThread, pyqtSignal
from .my_files import MyDataFile

file_desc = (
    "All files (*.*)",
    "Text files (*.dat *.txt)",
    "Excel Workbooks (*.xlsx *.xlsm)",
    "Excel Binary Workbooks (*.xlsb)",
    "Excel templates (*.xltx *.xltm)",
    "Excel Workbooks 97-2003 (*.xls)",
    "HDF5 files (*.h5 *.hdf *.hdf5)"
)


class DataReaderThread(QObject):
    finished = pyqtSignal()
    finished_error = pyqtSignal(str)

    def __init__(self, file, file_name, file_type):
        super().__init__()
        self.file = file
        self.file_name = file_name
        self.file_type = file_type

    def run(self):
        try:
            self.file.read_data(self.file_name, self.file_type)
            self.finished.emit()
        except Exception as e:
            self.finished_error.emit(str(e))


class MyQtFileGroup:
    def __init__(self, parent):
        self.parent = parent
        self.__file_names = []
        self.__file_filter = file_desc[0]
        self.data_files = []

    def set_file_info(self, recent_dir = None):
        files = QFileDialog.getOpenFileNames(
            parent=self.parent,
            caption="Open data files",
            directory=recent_dir,
            filter=';;'.join(file_desc),
            initialFilter=self.__file_filter,
            options=QFileDialog.DontUseNativeDialog)
        if files[0]:
            self.__file_names = files[0]
            self.__file_filter = files[1]
            self.parent.settings.setValue(
                'recent_directory', QFileInfo(self.get_file_names()[0]).path())

    def get_file_names(self):
        return self.__file_names

    def get_file_filter(self):
        return self.__file_filter

    def get_file_type(self):
        if self.__file_filter in file_desc[:2]:
            return 'text'
        if self.__file_filter in file_desc[2:6]:
            return 'excel'
        if self.__file_filter == file_desc[6]:
            return 'hdf5'

    def read_data_files(self):
        pass


class MyQtDataFile(MyDataFile, QObject):
    finished = pyqtSignal()
    needed_to_retry = pyqtSignal()

    def __init__(self, file_name=None, data_file_type=None):
        super().__init__(file_name, data_file_type)
        self.thread = None
        self.worker = None

    def thread_read_data(self, file_name=None, data_file_type=None):
        self.thread = QThread()
        self.worker = DataReaderThread(self, file_name, data_file_type)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self._success_data_read)
        self.worker.finished_error.connect(self.thread.quit)
        self.worker.finished_error.connect(self._error_data_read)
        self.thread.start()

    def _success_data_read(self):
        self.finished.emit()

    def _error_data_read(self, err_message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Data File Open Error")
        msg.setInformativeText(
            f"Unable to open {self.get_file_name()}. "
            f"This file is probably not {self.get_file_type()} file")
        msg.setDetailedText(err_message)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Ok)
        msg.exec_()
        try_open_again = False if msg.clickedButton().text() == 'OK' else True
        if try_open_again:
            self.needed_to_retry.emit()



    # def save_file(self):
    #     file = QFileDialog.getSaveFileName(
    #         parent=self.parent,
    #         caption="Save data file",
    #         directory=QDir.currentPath(),
    #         filter="Text files (*.dat *.txt)",
    #         initialFilter="Text files (*.dat *.txt)")
