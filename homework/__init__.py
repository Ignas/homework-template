from pyramid.config import Configurator
from pyramid.response import Response


def make_application():
    with Configurator() as config:
        config.add_route('health', '/')
        config.scan("homework.views")
        return config.make_wsgi_app()


application = make_application()