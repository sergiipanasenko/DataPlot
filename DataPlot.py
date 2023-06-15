from PyQt5 import QtCore, QtWidgets, QtGui
from SP_Forms import MyDataPlotForm


class ProgramWindow(MyDataPlotForm):

    def TableRepaint(self):
        background_color = QtGui.QColor('white')
        if self.ListRowNumber:
            for j in self.ListRowNumber:
                for i in self.ListColNumber:
                    jj = int(j) - 1
                    ii = int(i) - 1
                    if self.currentTable.item(jj, ii):
                        self.currentTable.item(jj, ii).setBackground(background_color)
        # if self.check_Datavalue.isChecked():
        #     self.DataSelect()
        # if self.check_Xvalue.isChecked():
        #     self.XSelect()
        # if self.check_Yvalue.isChecked():
        #     self.YSelect()
        self.unsetCursor()

    def XSelect(self):
        if len(self.XRange):
            if self.XRange[2] < self.XRange[1]:
                step = -1
                begin = self.XRange[1]
                end = self.XRange[2] - 1
            else:
                step = 1
                begin = self.XRange[1]
                end = self.XRange[2] + 1
            if self.XRange[3]:
                for i in range(begin, end, step):
                    if self.currentTable.item(i, self.XRange[0]):
                        self.currentTable.item(i, self.XRange[0]).setBackground(self.XChooseColor)
            else:
                for i in range(begin, end, step):
                    if self.currentTable.item(self.XRange[0], i):
                        self.currentTable.item(self.XRange[0], i).setBackground(self.XChooseColor)

    def YSelect(self):
        if len(self.YRange):
            if self.YRange[2] < self.YRange[1]:
                step = -1
                begin = self.YRange[1]
                end = self.YRange[2] - 1
            else:
                step = 1
                begin = self.YRange[1]
                end = self.YRange[2] + 1
            if self.YRange[3]:
                for i in range(begin, end, step):
                    if self.currentTable.item(self.YRange[0], self.YRange[0]):
                        self.currentTable.item(self.YRange[0], i).setBackground(self.YChooseColor)
            else:
                for i in range(begin, end, step):
                    if self.currentTable.item(i, self.YRange[0]):
                        self.currentTable.item(i, self.YRange[0]).setBackground(self.YChooseColor)

    def XRangeInit(self):
        if len(self.XRange):
            self.XRange[0] = self.combo_Xnumber.currentIndex()
            self.XRange[1] = self.combo_Xbegin.currentIndex()
            self.XRange[2] = self.combo_Xend.currentIndex()
            # if self.combo_Xrowcol.currentIndex():
            #     self.XRange[3] = False
            # else:
            #     self.XRange[3] = True
        else:
            self.XRange.append(self.combo_Xnumber.currentIndex())
            self.XRange.append(self.combo_Xbegin.currentIndex())
            self.XRange.append(self.combo_Xend.currentIndex())
            # if self.combo_Xrowcol.currentIndex():
            #     self.XRange.append(False)
            # else:
            #     self.XRange.append(True)

    def YRangeInit(self):
        if len(self.YRange):
            self.YRange[0] = self.combo_Ynumber.currentIndex()
            self.YRange[1] = self.combo_Ybegin.currentIndex()
            self.YRange[2] = self.combo_Yend.currentIndex()
            if self.combo_Yrowcol.currentIndex():
                self.YRange[3] = False
            else:
                self.YRange[3] = True
        else:
            self.YRange.append(self.combo_Ynumber.currentIndex())
            self.YRange.append(self.combo_Ybegin.currentIndex())
            self.YRange.append(self.combo_Yend.currentIndex())
            # if self.combo_Yrowcol.currentIndex():
            #     self.YRange.append(False)
            # else:
            #     self.YRange.append(True)

    def XRowColChange(self):
        self.XRange = []
        self.combo_Xnumber.clear()
        self.combo_Xbegin.clear()
        self.combo_Xend.clear()
        # if self.combo_Xrowcol.currentIndex():
        #     self.label_Xrowcol.setText('Columns from')
        #     self.combo_Xnumber.addItems(self.ListRowNumber)
        #     self.combo_Xbegin.addItems(self.ListColNumber)
        #     self.combo_Xend.addItems(self.ListColNumber)
        #     self.combo_Xend.setCurrentIndex(len(self.ListColNumber) - 1)
        # else:
        #     self.label_Xrowcol.setText('Rows from')
        #     self.combo_Xnumber.addItems(self.ListColNumber)
        #     self.combo_Xbegin.addItems(self.ListRowNumber)
        #     self.combo_Xend.addItems(self.ListRowNumber)
        #     self.combo_Xend.setCurrentIndex(len(self.ListRowNumber) - 1)
        self.XRangeInit()

    def YRowColChange(self):
        self.YRange = []
        self.combo_Ynumber.clear()
        self.combo_Ybegin.clear()
        self.combo_Yend.clear()
        # if self.combo_Yrowcol.currentIndex():
        #     self.label_Yrowcol.setText('Rows from')
        #     self.combo_Ynumber.addItems(self.ListColNumber)
        #     self.combo_Ybegin.addItems(self.ListRowNumber)
        #     self.combo_Yend.addItems(self.ListRowNumber)
        #     self.combo_Yend.setCurrentIndex(len(self.ListRowNumber) - 1)
        # else:
        #     self.label_Yrowcol.setText('Columns from')
        #     self.combo_Ynumber.addItems(self.ListRowNumber)
        #     self.combo_Ybegin.addItems(self.ListColNumber)
        #     self.combo_Yend.addItems(self.ListColNumber)
        #     self.combo_Yend.setCurrentIndex(len(self.ListColNumber) - 1)
        self.YRangeInit()

    # def XChangeState(self):
    #     if self.currentTable.rowCount():
    #         if self.check_Xvalue.isChecked():
    #             self.XRangeInit()
    #         else:
    #             self.XRange = []
    #         self.TableRepaint()

    # def YChangeState(self):
    #     if self.currentTable.rowCount():
    #         if self.check_Yvalue.isChecked():
    #             self.YRangeInit()
    #         else:
    #             self.YRange = []
    #         self.TableRepaint()
    #
    # def DataChangeState(self):
    #     if self.currentTable.rowCount():
    #         if self.check_Datavalue.isChecked():
    #             self.DataRangeInit()
    #         else:
    #             self.DataRange = []
    #         self.TableRepaint()

    def DataRangeInit(self):
        row_begin = self.combo_Datarowbegin.currentIndex()
        row_end = self.combo_Datarowend.currentIndex()
        col_begin = self.combo_Datacolbegin.currentIndex()
        col_end = self.combo_Datacolend.currentIndex()
        if len(self.DataRange):
            self.DataRange[0] = [row_begin, col_begin]
            self.DataRange[1] = [row_end, col_end]
        else:
            self.DataRange.append([row_begin, col_begin])
            self.DataRange.append([row_end, col_end])

    def DataSelect(self):
        if len(self.DataRange):
            row_begin = self.DataRange[0][0]
            row_end = self.DataRange[1][0]
            col_begin = self.DataRange[0][1]
            col_end = self.DataRange[1][1]
            if row_end < row_begin:
                step_row = -1
                begin_row = row_begin
                end_row = row_end - 1
            else:
                step_row = 1
                begin_row = row_begin
                end_row = row_end + 1
            if col_end < col_begin:
                step_col = -1
                begin_col = col_begin
                end_col = col_end - 1
            else:
                step_col = 1
                begin_col = col_begin
                end_col = col_end + 1
            # if self.check_Datavalue.isChecked():
            #     for j in range(begin_row, end_row, step_row):
            #         for i in range(begin_col, end_col, step_col):
            #             if self.currentTable.item(j, i):
            #                 self.currentTable.item(j, i).setBackground(self.DataChooseColor)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyDataPlotForm()
    MainWindow.show()
    sys.exit(app.exec_())
