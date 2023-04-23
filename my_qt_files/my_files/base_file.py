from os.path import exists


class FileNotSpecifiedError(Exception):
    pass


class DataTypeMismatchError(Exception):
    pass


class MyFile:
    def __init__(self, file_name=None):
        super().__init__()
        self.__file_name = file_name

    def set_file_name(self, file_name):
        self.__file_name = file_name

    def check_file_name(self, file_name):
        if file_name is None:
            file_name = self.get_file_name()
            if file_name is None:
                raise FileNotSpecifiedError
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

    def set_data(self, data):
        self.__data = data

    def read_data(self, file_name=None):
        pass

    def write_data(self, data: dict, marker='a', file_name=None):
        pass


class IFileType:
    def __init__(self):
        super().__init__()
        self.__file_type = None
        self.__type_dict = None

    def set_file_type(self, file_type):
        self.__file_type = file_type

    def set_type_dict(self, type_dict):
        self.__type_dict = type_dict

    def get_file_type(self):
        return self.__file_type

    def get_type_dict(self):
        return self.__type_dict

    def check_file_type(self, file_type):
        if file_type not in self.get_type_dict().keys():
            raise DataTypeMismatchError
