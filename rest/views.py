from rest_framework.exceptions import NotFound


def error404(request):
    raise NotFound(detail="Error 404, page not found", code=404)
