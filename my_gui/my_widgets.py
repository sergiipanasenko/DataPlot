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
        self.setRowCount(1)
        self.setColumnCount(1)
        self.setItem(0, 0, QTableWidgetItem())
        self.background = self.item(0, 0).background()

    def set_colors(self, x_color=None, y_color=None, s_color=None, data_color=None):
        if x_color is not None:
            self.x_color = x_color
        if y_color is not None:
            self.y_color = y_color
        if s_color is not None:
            self.s_color = s_color
        if data_color is not None:
            self.data_color = data_color

    def reset_colors(self):
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.item(i, j).setBackground(self.background)


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
        return values

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
        self.reset_colors()
        for index in range(4):
            for value in self.values[index]:
                i, j, _ = value
                self.item(i, j).setBackground(self.colors[index])


class OutputTableWidget(DataTableWidget):
    def __init__(self):
        # parent initialisation
        super().__init__()

        # blank output table creation
        self.setRowCount(2)
        self.setColumnCount(3)
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.setItem(i, j, QTableWidgetItem())
        self.repaint_table()

    def add_values(self, input_table, data, index, col_number=None):
        values = self.values[index]
        values.append((input_table, data))
        self.change_data(col_number)

    def extract_data(self, index):
        values = self.values[index]
        data = []
        for value in values:
            data.extend(value[1])
        return data

    def change_data(self, col_number=None):
        self.clear()
        self.setRowCount(0)
        self.setColumnCount(0)
        x_data = self.extract_data(0)
        y_data = self.extract_data(1)
        s_data = self.extract_data(2)
        data = self.extract_data(3)
        if x_data:
            if self.columnCount() < 1:
                self.setColumnCount(1)
            for i in range(1, len(x_data) + 1):
                if self.rowCount() < i + 1:
                    self.setRowCount(i + 1)
                self.setItem(i, 0,
                             QTableWidgetItem(x_data[i - 1][2]))
        if s_data:
            if self.columnCount() < 2:
                self.setColumnCount(2)
            for i in range(1, len(s_data) + 1):
                if self.rowCount() < i + 1:
                    self.setRowCount(i + 1)
                self.setItem(i, 1,
                             QTableWidgetItem(s_data[i - 1][2]))
        if y_data:
            if self.rowCount() < 1:
                self.setRowCount(1)
            for j in range(2, len(y_data) + 2):
                if self.columnCount() < j + 1:
                    self.setColumnCount(j + 1)
                self.setItem(0, j,
                             QTableWidgetItem(y_data[j - 2][2]))
        if data:
            if col_number is None:
                col_number = len(y_data)
            if self.columnCount() < col_number + 2:
                self.setColumnCount(col_number + 2)
            for index in range(len(data)):
                i = 1 + index // col_number
                j = 2 + index % col_number
                if self.rowCount() < i + 1:
                    self.setRowCount(i + 1)
                self.setItem(i, j,
                             QTableWidgetItem(data[index][2]))
        self.repaint_table()

    def repaint_table(self):
        # self.reset_colors()
        for ind_row in range(self.rowCount()):
            for ind_col in range(self.columnCount()):
                if self.item(ind_row, ind_col) is None:
                    self.setItem(ind_row, ind_col, QTableWidgetItem())
                if ind_row > 0 and ind_col == 0:
                    self.item(ind_row, ind_col).setBackground(self.x_color)
                if ind_row > 0 and ind_col == 1:
                    self.item(ind_row, ind_col).setBackground(self.s_color)
                if ind_row == 0 and ind_col > 1:
                    self.item(ind_row, ind_col).setBackground(self.y_color)
                if ind_row > 0 and ind_col > 1:
                    self.item(ind_row, ind_col).setBackground(self.data_color)


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
