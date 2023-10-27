from django.http import HttpResponseRedirect



class ForceDefaultLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the path is root and no language code in path
        if request.path == '/':
            return HttpResponseRedirect('/kk/')
        
        response = self.get_response(request)
        return response