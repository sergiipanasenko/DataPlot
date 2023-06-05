from scipy.io import loadmat, savemat
from .base_file import MyFile, IData


class MyMatFile(MyFile, IData):
    def __init__(self, file_name=None):
        super().__init__(file_name)

    def read_data(self, file_name=None):
        file_name = self.check_file_name(file_name)
        mat_data = loadmat(file_name)

