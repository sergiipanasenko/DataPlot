from PyQt5 import QtCore, QtWidgets, QtGui, uic


class MyTableWidget(QtWidgets.QTableWidget):
    def __init__(self):
        # parent initialisation
        super().__init__()
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)

    def add_data(self, data):
        row_number = len(data)
        max_column_number = max(list(map(len, data)))
        self.setRowCount(row_number)
        self.setColumnCount(max_column_number)

        for row, row_data in enumerate(data):
            col = 0
            while col < len(row_data):
                if isinstance(row_data[col], bytes) or isinstance(row_data[col], bytearray):
                    cell_data = row_data[col].decode()
                else:
                    cell_data = str(row_data[col])
                self.setItem(row, col, QtWidgets.QTableWidgetItem(cell_data))
                col += 1


class MyTabWidget(QtWidgets.QTabWidget):
    def __init__(self):
        # parent initialisation
        super().__init__()

        # default settings
        self.new_tab = None
        self.setUsesScrollButtons(True)
        self.setTabsClosable(True)

        # connections
        self.tabCloseRequested.connect(self.close_tab)

    def add_data(self, data):
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
                self.addTab(self.new_tab, keys[tab_number])
                self.new_tab.add_data(data_val)
        else:
            self.new_tab = MyTableWidget()
            self.addTab(self.new_tab, 'Data')
            self.new_tab.add_data(data)

    def close_tab(self, index):
        if self.count() > 1:
            self.removeTab(index)
            if self.count() == 1:
                self.setTabsClosable(False)