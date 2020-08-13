import pytest
from PageObj.login_page import LoginPage
from TestData.read_test_data import TestData

@pytest.mark.usefixtures("in_web","logins_data")
class TestLogin():
    b=[]
    b.append(TestData().login_data()[0])
    #If N argnames were specified, argvalues must be a list of N-tuples,
    @pytest.mark.parametrize("logins_data",b ,
                             indirect=True)  # indirect=True是为了把login当成一个函数去执行，把data当作参数传入函数
    # @pytest.mark.smoke
    def test_login_success(self, in_web, logins_data):
        LoginPage(in_web).login(logins_data['username'], logins_data['password'], logins_data['code'])
        assert logins_data['expect'] == 200


    @pytest.mark.parametrize("logins_data", TestData().login_data()[1:],
                             indirect=True)  # indirect=True是为了把login当成一个函数去执行，把data当作参数传入函数
    def test_login_error(self,in_web,logins_data):
        LoginPage(in_web).login(logins_data['username'],logins_data['password'],logins_data['code'])
        assert LoginPage(in_web).error_msg() == logins_data['expect']
