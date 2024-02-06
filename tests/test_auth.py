from tests.conftest import client

jwt_token = None


def auth_header():
    global jwt_token
    return {"Authorization": f"Bearer {jwt_token}"}


def test_register():
    # TestCase1 register user
    response = client.post('/auth/register',
                           json={'username': 'testname', 'email': 'test@mail.ru', 'password': 'testpass'})
    assert response.status_code == 200


def test_login():
    global jwt_token
    # TestCase2 login user
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    response = client.post('/auth/login',
                           data={'username': 'testname', 'password': 'testpass'}, headers=headers)

    jwt_token = response.json().get("access_token")
    print(response.json())

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_about_me():
    # TestCase3 read info for user

    response = client.get('/auth/about_me', headers=auth_header())
    assert response.status_code == 200
