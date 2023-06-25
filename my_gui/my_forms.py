from PyQt5 import QtCore, QtWidgets


class AbstractForm(QtCore.QObject):
    def __init__(self):
        super().__init__()

        # settings
        self.settings_file = 'settings.ini'
        self.settings = QtCore.QSettings(self.settings_file, QtCore.QSettings.IniFormat)

    def set_style(self, qss_file_name):
        if self.sender():
            self.settings.setValue("theme_action_checked", self.sender().objectName())
        try:
            with open(qss_file_name, 'r') as qss_file:
                with qss_file:
                    qss = qss_file.read()
        except (FileNotFoundError, OSError, IOError):
            qss = ""
        QtWidgets.qApp.setStyleSheet(qss)
        self.settings.setValue("theme_checked", qss_file_name)
        self.settings.sync()


