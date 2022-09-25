from os.path import exists


class MyFile:
    def __init__(self, file_name=None):
        super().__init__()
        self.file_name = file_name
        self.mod_time = None

    def _change_file_name(self, file_name):
        if file_name:
            self.file_name = file_name

    def is_exist(self, file_name=None):
        self._change_file_name(file_name)
        if exists(self.file_name):
            return True
        else:
            return False
