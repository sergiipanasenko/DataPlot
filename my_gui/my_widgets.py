from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTabWidget, QFrame
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class InputDataThread(QObject):
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
        if self.obj.rowCount() > 0 and self.obj.columnCount() > 0:
            self.obj.background = self.obj.item(0, 0).background()
        self.finished.emit()


class DataTableWidget(QTableWidget):
    add_data_finished = pyqtSignal()

    def __init__(self):
        # parent initialisation
        super().__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Sunken)
        self.setFont(QFont("Times", 11, QFont.Normal))

        # self initialisation
        self.background = None
        self.x_values = []
        self.y_values = []
        self.s_values = []
        self.data_values = []
        self.values = (self.x_values, self.y_values,
                       self.s_values, self.data_values)
        self.x_color = QColor(112, 194, 126)
        self.y_color = QColor(112, 168, 194)
        self.s_color = QColor(194, 112, 141)
        self.data_color = QColor(194, 194, 112)
        self.colors = (self.x_color, self.y_color,
                       self.s_color, self.data_color)

    def set_colors(self, x_color=None, y_color=None, s_color=None, data_color=None):
        if x_color is not None:
            self.x_color = x_color
        if y_color is not None:
            self.y_color = y_color
        if s_color is not None:
            self.s_color = s_color
        if data_color is not None:
            self.data_color = data_color


class InputTableWidget(DataTableWidget):
    def __init__(self):
        # parent initialisation
        super().__init__()

        # self initialisation
        self.thread = None
        self.worker = None

    def add_data(self, data):
        row_number = len(data)
        max_column_number = max(list(map(len, data)))
        self.setRowCount(row_number)
        self.setColumnCount(max_column_number)
        self.thread = QThread()
        self.worker = InputDataThread(self, data)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(lambda: self.add_data_finished.emit())
        self.thread.start()

    def add_values(self, limits: tuple, index: int, row_wise=True):
        start_row, start_col, end_row, end_col = limits
        values = []
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                values.append((i, j, self.item(i, j).text()))
        if not row_wise:
            values.sort(key=lambda x: (x[1], x[0]))
        self.values[index].extend(values)
        self.repaint_table()

    def remove_values(self, limits: tuple, index: int):
        start_row, start_col, end_row, end_col = limits
        values = self.values[index]
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                if len(values) == 0:
                    return
                for value in values:
                    *row_col, data = value
                    if row_col == [i, j]:
                        item = *row_col, data
                        values.remove(item)
                        break
        self.repaint_table()

    def reset_values(self, index):
        self.values[index].clear()
        self.repaint_table()

    def repaint_table(self):
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.item(i, j).setBackground(self.background)
        for index in range(4):
            for value in self.values[index]:
                i, j, _ = value
                self.item(i, j).setBackground(self.colors[index])


class OutputTableWidget(DataTableWidget):
    def __init__(self):
        # parent initialisation
        super().__init__()

    def add_data(self):
        pass


class InputTabWidget(QTabWidget):
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
                    self.new_tab = InputTabWidget()
                else:
                    self.new_tab = InputTableWidget()
                    self.tables.append(self.new_tab)
                self.addTab(self.new_tab, keys[tab_number])
                self.new_tab.add_data(data_val)
                self.new_tab.add_data_finished.connect(self._post_add_data)
        else:
            self.new_tab = InputTableWidget()
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
