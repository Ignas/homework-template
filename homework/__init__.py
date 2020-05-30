from pyramid.config import Configurator
from pyramid.response import Response


def health(request):
    return Response('OK')

def make_application():
    with Configurator() as config:
        config.add_route('health', '/')
        config.add_view(health, route_name='health')
        return config.make_wsgi_app()

application = make_application()