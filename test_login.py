import requests

BASE_URL = "http://127.0.0.1:5000"  # 你本地启动的 Flask 接口地址

def test_login_success():
    data = {
        "phone": "13800000000",
        "code": "1234"
    }
    response = requests.post(f"{BASE_URL}/login", json=data)
    assert response.status_code == 200
    assert "token" in response.json()



def test_login_invalid_phone_format():
    data = {
        "phone": "1358888",  # 手机号格式错误
        "code": "1234"
    }
    response = requests.post(f"{BASE_URL}/login", json=data)
    assert response.status_code == 400


def test_login_wrong_code():
    data = {
        "phone": "13800000000",
        "code": "9999"  # 错误验证码
    }
    response = requests.post(f"{BASE_URL}/login", json=data)
    assert response.status_code == 400


def test_login_expired_code():
    data = {
        "phone": "13800000000",
        "code": "000000"  # 模拟过期验证码
    }
    response = requests.post(f"{BASE_URL}/login", json=data)
    assert response.status_code == 400

