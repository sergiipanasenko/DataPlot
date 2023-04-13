from .my_file import MyFile, IData, IText


class MyTextFile(MyFile, IText):
    def __init__(self, file_name=None):
        super().__init__(file_name)

    def read_text(self, file_name=None):
        file_name = self.check_file_name(file_name)
        with open(file_name) as file:
            text = file.read()
        self.set_text(text)

    def write_text(self, text: str, marker='a', file_name=None):
        file_name = self.check_file_name(file_name)
        if marker != 'a' and marker != 'w':
            marker = 'a'
        with open(file_name, marker) as file:
            file.write(text)


class MyTextDataFile(MyFile, IData):
    def __init__(self, file_name=None):
        super().__init__(file_name)

    def read_data(self, file_name=None):
        file_name = self.check_file_name(file_name)
        text_file = MyTextFile(file_name)
        text_file.read_text()
        text = text_file.get_text().strip()
        data = []
        for row in text.splitlines():
            row_data = row.rstrip().split()
            data.append(row_data)
        self.set_data({'data': data})

    def write_data(self, data: list, marker='a', file_name=None):
        file_name = self.check_file_name(file_name)
        if marker != 'a' and marker != 'w':
            marker = 'a'
        with open(file_name, marker) as file:
            for row in data:
                for item in row:
                    file.write(item)
                file.write('\n')
