from homework.views import health
from pyramid.response import Response


def test_health():
    response:Response = health(None)
    assert response.body == b"OK"
    assert response.status_code == 200