from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTabWidget, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class AddDataThread(QObject):
    finished = pyqtSignal()

    def __init__(self, obj, data):
        super().__init__()
        self.obj = obj
        self.data = data

    def run(self):
        for row, row_data in enumerate(self.data):
            col = 0
            while col < len(row_data):
                if isinstance(row_data[col], bytes) or isinstance(row_data[col], bytearray):
                    cell_data = row_data[col].decode()
                else:
                    cell_data = str(row_data[col])
                self.obj.setItem(row, col, QTableWidgetItem(cell_data))
                col += 1
        self.finished.emit()


class MyTableWidget(QTableWidget):
    add_data_finished = pyqtSignal()

    def __init__(self):
        # parent initialisation
        super().__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Sunken)
        self.setFont(QFont("Times", 11, QFont.Normal))

        # self initialisation
        self.thread = None
        self.worker = None
        self.x_values = dict()
        self.y_values = dict()
        self.s_values = dict()
        self.data_values = dict()
        self.values = (self.x_values, self.y_values,
                       self.s_values, self.data_values)

    def add_data(self, data):
        row_number = len(data)
        max_column_number = max(list(map(len, data)))
        self.setRowCount(row_number)
        self.setColumnCount(max_column_number)
        self.thread = QThread()
        self.worker = AddDataThread(self, data)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(lambda: self.add_data_finished.emit())
        self.thread.start()


class MyTabWidget(QTabWidget):

    add_data_finished = pyqtSignal()

    def __init__(self):
        # parent initialisation
        super().__init__()
        self.keys_number = 0

        # default settings
        self.tables = []
        self.new_tab = None
        self.setUsesScrollButtons(True)
        self.setTabsClosable(True)

        # connections
        self.tabCloseRequested.connect(self.close_tab)

    def add_data(self, data):
        def all_keys(input_dict):
            if isinstance(input_dict, dict):
                data_keys = [*input_dict.keys(), ]
                for key, val in input_dict.items():
                    data_keys.extend(all_keys(val))
                return data_keys
            else:
                return ['data']
        self.keys_number = len(all_keys(data))
        if isinstance(data, dict):
            number_of_tabs = len(data)
            if number_of_tabs == 1:
                self.setTabsClosable(False)
            keys = tuple(data.keys())
            for tab_number in range(0, number_of_tabs):
                data_val = data[keys[tab_number]]
                if isinstance(data_val, dict):
                    self.new_tab = MyTabWidget()
                else:
                    self.new_tab = MyTableWidget()
                    self.tables.append(self.new_tab)
                self.addTab(self.new_tab, keys[tab_number])
                self.new_tab.add_data(data_val)
                self.new_tab.add_data_finished.connect(self._post_add_data)
        else:
            self.new_tab = MyTableWidget()
            self.tables.append(self.new_tab)
            self.addTab(self.new_tab, 'Data')
            self.new_tab.add_data(data)
            self.add_data_finished.connect(lambda: self.add_data_finished.emit())

    def _post_add_data(self):
        self.keys_number -= 1
        if self.keys_number == 0:
            self.add_data_finished.emit()

    def close_tab(self, index):
        if self.count() > 1:
            self.removeTab(index)
            if self.count() == 1:
                self.setTabsClosable(False)