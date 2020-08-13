from tools.do_excel import DoExcel
import os
from conf.project_path import test_data_path

class TestData():
    def login_data(self):
        fileName = os.path.join(test_data_path,"login_data.xlsx")
        return DoExcel(fileName,"login").read_excel()

if __name__ == '__main__':
    b = []
    b.append(TestData().login_data()[0])
    print(b)
    print(TestData().login_data()[1:])