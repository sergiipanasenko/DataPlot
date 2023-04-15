from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QFileInfo, QDir, QObject, QThread, pyqtSignal
from .my_files import MyDataFile, IData, MyFile, IFileType, DataTypeMismatchError

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
    finished = pyqtSignal(MyDataFile)
    finished_error = pyqtSignal()

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        try:
            data_file = MyDataFile(self.file_name)
            data_file.read_data()
            self.finished.emit(data_file)
        except Exception:
            self.finished_error.emit()


class MyQtFile(MyFile, IData, IFileType, QObject):
    finished = pyqtSignal()

    def __init__(self, parent, recent_dir=None):
        super().__init__()
        self.recent_dir = recent_dir
        self.parent = parent
        self.thread = None
        self.worker = None

    def finish_data_read(self, data_file=None):
        if data_file is not None:
            try_open_again = False
            self.set_data(data_file.get_data())
            self.set_file_type(data_file.get_file_type())
            self.finished.emit()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Data File Open Error")
            msg.setInformativeText(
                f"Unable to open {self.get_file_name()}. "
                f"This file is probably not data file")
            # msg.setDetailedText(str(e))
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Ok)
            msg.exec_()
            try_open_again = False if msg.clickedButton().text() == 'OK' else True
        if try_open_again:
            self.read_data()

    def read_data(self, file_name=None):
        file = QFileDialog.getOpenFileName(
                parent=self.parent,
                caption="Open data file",
                directory=self.recent_dir,
                filter=';;'.join(file_desc),
                initialFilter=file_desc[0])
        if file[0]:
            self.set_file_name(file[0])
            self.parent.settings.setValue(
                'recent_directory', QFileInfo(file[0]).path())
            self.thread = QThread()
            self.worker = DataReaderThread(self.get_file_name())
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.finish_data_read)
            self.worker.finished_error.connect(self.thread.quit)
            self.worker.finished_error.connect(self.finish_data_read)
            self.thread.start()

    def save_file(self):
        file = QFileDialog.getSaveFileName(
            parent=self.parent,
            caption="Save data file",
            directory=QDir.currentPath(),
            filter="Text files (*.dat *.txt)",
            initialFilter="Text files (*.dat *.txt)")
