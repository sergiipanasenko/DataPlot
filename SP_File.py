from os.path import exists, getmtime


class MyFile:
    def __init__(self):
        super().__init__()
        self.file_name = None
        self.mod_time = None


class MyFileToReadText(MyFile):
    def __init__(self):
        MyFile.__init__(self)
        self.text = ''

    def read_text(self, file_name):
        if (self.file_name != file_name) or (self.mod_time != getmtime(file_name)):
            with open(file_name) as file:
                self.text = file.read()
                self.file_name = file_name
                self.mod_time = getmtime(file_name)


class MyFileToReadData(MyFileToReadText):
    def __init__(self):
        MyFileToReadText.__init__(self)
        self.data = None

    def read_data(self, file_name):
        self.read_text(file_name)
        self.text = self.text.strip()
        self.data = []
        for row in self.text.splitlines():
            row_data = row.rstrip().split()
            self.data.append(row_data)
