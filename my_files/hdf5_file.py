from os.path import getmtime
import h5py as h5
from .my_file import MyFile


class MyHDF5File(MyFile):
    def __init__(self, file_name=None):
        MyFile.__init__(self, file_name)
        self.data = dict()

    def read_h5_data(self, file_name=None):
        if (self.file_name != file_name) or (self.mod_time != getmtime(file_name)):
            self._change_file_name(file_name)
            with h5.File(self.file_name, 'r') as h5_file:
                data = dict(h5_file)
                data1 = data['Metadata']
                print("Keys: %s" % h5_file.keys())