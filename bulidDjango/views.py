from django.http import HttpResponse

from django.http import HttpResponseNotFound


def handler404(request, exception):
    """Custom 404 page."""
    return HttpResponse("404: this page not found", status=404)
    # or
    # return HttpResponseNotFound("404: this page not found")


def test_page(request):
    """Test page."""
    return HttpResponse("Test page")