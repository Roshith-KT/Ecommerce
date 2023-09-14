from django.shortcuts import redirect
from . views import is_customer
from django.http import HttpResponse


#custom middleware class added for generating response after user_passes_test deorator returns false
class CustomLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if is_customer(request.user) is False:
                return HttpResponse("Not authorized! Access denied")

        response = self.get_response(request)
        return response
    
    
#status - logic error , not working 