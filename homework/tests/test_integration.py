import pytest
from webtest import TestApp
from homework import make_application

@pytest.fixture(scope="module")
def application():
    return TestApp(make_application())


def test_health(application:TestApp):
    assert application.get("/").body == b'OK'