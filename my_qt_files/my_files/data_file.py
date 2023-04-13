from . import MyTextDataFile, MyExcelFile, MyHDF5File
from .my_file import MyFile, IData, IFileType


data_file_matching = {
    'text': (MyTextDataFile, ('txt', 'dat')),
    'excel': (MyExcelFile, ('xlsx', 'xlsm', 'xltx', 'xltm', 'xlsb', 'xls')),
    'hdf5': (MyHDF5File, ('h5', 'hdf', 'hdf5'))
}


class MyDataFile(MyFile, IData, IFileType):
    def __init__(self, file_name=None, data_file_type=None):
        super().__init__(file_name)
        self.set_type_dict(data_file_matching)
        if data_file_type is not None:
            self.check_file_type(data_file_type)
        self.set_file_type(data_file_type)

    def read_data(self, file_name=None, data_file_type=None):
        file_name = self.check_file_name(file_name)
        if data_file_type is None:
            file_ext = file_name.split('.')[-1]
            if file_ext in self.get_type_dict()['excel'][1]:
                data_file_type = 'excel'
            elif file_ext in self.get_type_dict()['hdf5'][1]:
                data_file_type = 'hdf5'
            else:
                data_file_type = 'text'
        else:
            self.check_file_type(data_file_type)
        data_file = self.get_type_dict()[data_file_type][0](file_name)
        data_file.read_data()
        self.set_data(data_file.get_data())
