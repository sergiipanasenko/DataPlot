from os.path import getmtime
import h5py as h5
from .my_file import MyFile


class MyHDF5File(MyFile):
    def __init__(self, file_name=None):
        MyFile.__init__(self, file_name)
        self.data = dict()

    @staticmethod
    def parse_h5_data(data):
        if isinstance(data, h5.Dataset):
            output = []
            if data.dtype.fields.keys():
                output.append(list(data.dtype.fields.keys()))
            for row in data:
                output.append(list(row))
            return output
        elif isinstance(data, h5.File) or isinstance(data, h5.Group):
            output = dict()
            data = dict(data)
            for key in data.keys():
                output[key] = MyHDF5File.parse_h5_data(data[key])
            return output

    def read_h5_data(self, file_name=None):
        if (self.file_name != file_name) or (self.mod_time != getmtime(file_name)):
            self._change_file_name(file_name)
            with h5.File(self.file_name, 'r') as h5_file:
                self.data = self.parse_h5_data(h5_file)