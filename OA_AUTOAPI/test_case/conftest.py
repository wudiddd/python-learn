import pytest

@pytest.fixture()
def login_data(request):
    param = request.param #接收登录的数据
    return param