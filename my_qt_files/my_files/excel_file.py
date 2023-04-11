from openpyxl import load_workbook
from xlrd import open_workbook as open_old_workbook
from pyxlsb import open_workbook as open_binary_workbook
from .my_file import MyFile, IData


class MyNewExcelFile(MyFile, IData):
    def __init__(self, file_name=None):
        super().__init__(file_name)

    def read_data(self, file_name=None):
        if self.check_file_name(file_name) is not None:
            with load_workbook(file_name) as wb:
                data = dict()
                for sheet in wb:
                    data[sheet.title] = []
                    for row in range(1, sheet.max_row + 1):
                        current_row = []
                        for col in range(1, sheet.max_column + 1):
                            cell_value = sheet.cell(row, col).value
                            if cell_value is not None:
                                current_row.append(str(cell_value))
                            else:
                                current_row.append('')
                        data[sheet.title].append(current_row)
            self.set_data(data)


class MyOldExcelFile(MyFile, IData):
    def __init__(self, file_name=None):
        super().__init__(file_name)

    def read_data(self, file_name=None):
        if self.check_file_name(file_name) is not None:
            data = dict()
            with open_old_workbook(file_name) as wb:
                for sheet in wb:
                    data[sheet.name] = []
                    for row in range(sheet.nrows):
                        current_row = []
                        for col in range(sheet.ncols):
                            cell_value = sheet.cell_value(row, col)
                            if cell_value is not None:
                                current_row.append(str(cell_value))
                            else:
                                current_row.append('')
                        data[sheet.name].append(current_row)
            self.set_data(data)


class MyBinaryExcelFile(MyFile, IData):
    def __init__(self, file_name=None):
        super().__init__(file_name)

    def read_data(self, file_name=None):
        if self.check_file_name(file_name) is not None:
            data = dict()
            with open_binary_workbook(file_name) as wb:
                for sheet_name in wb.sheets:
                    with wb.get_sheet(sheet_name) as sheet:
                        data[sheet_name] = []
                        for row in sheet.rows():
                            current_row = []
                            for cell in row:
                                if cell.v is not None:
                                    current_row.append(str(cell.v))
                                else:
                                    current_row.append('')
                            data[sheet_name].append(current_row)
            self.set_data(data)


class MyExcelFile(MyFile, IData):
    excel_file_matching = {
        'xlsx': MyNewExcelFile,
        'xls':  MyOldExcelFile,
        'xlsb': MyBinaryExcelFile
    }

    def __init__(self, file_name=None, file_type='xlsx'):
        super().__init__(file_name)
        self.file_type = file_type

    def read_data(self, file_name=None):
        if self.check_file_name(file_name) is not None:
            self.excel_file_matching[self.file_type](file_name).read_data()
