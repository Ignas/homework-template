from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name="health")
def health(request):
    return Response('OK')
