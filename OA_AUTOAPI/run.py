import pytest

if __name__ == '__main__':
    pytest.main(["-s","-v","--html","report/html/report.html","--alluredir","report/allure"])