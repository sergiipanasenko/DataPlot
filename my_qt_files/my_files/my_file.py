from os.path import exists


class MyFile:
    def __init__(self, file_name=None):
        super().__init__()
        self.__file_name = file_name

    def change_file_name(self, file_name=None):
        if file_name is not None:
            self.__file_name = file_name

    def check_file_name(self, file_name):
        if file_name is None:
            file_name = self.get_file_name()
        return file_name

    def get_file_name(self):
        return self.__file_name

    def is_exist(self, file_name=None):
        if file_name is None:
            file_name = self.get_file_name()
        if file_name is not None:
            if exists(file_name):
                return True
        return False


class IText:
    def __init__(self):
        super().__init__()
        self.__text = ''

    def set_text(self, text: str):
        self.__text = text

    def get_text(self):
        return self.__text

    def read_text(self, file_name=None):
        pass

    def write_text(self, text, marker='a', file_name=None):
        pass


class IData:
    def __init__(self):
        super().__init__()
        self.__data = dict()

    def get_data(self):
        return self.__data

    def set_data(self, data=None):
        if data is not None:
            self.__data = data

    def read_data(self, file_name=None):
        pass

    def write_data(self, data: dict, marker='a', file_name=None):
        pass
