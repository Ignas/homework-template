from homework import hello_world
from pyramid.response import Response


def test_hello_world():
    response:Response = hello_world(None)
    assert response.body == b"Hello World!"
    assert response.status_code == 200