from django.http import HttpResponseRedirect

class FakeLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path starts with '/admin/'
        if request.path.startswith('/admin/'):
            # Redirect to '/admin/'
            return HttpResponseRedirect('/adminBot/')
        return self.get_response(request)

