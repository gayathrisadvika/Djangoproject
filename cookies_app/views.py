from django.shortcuts import render

# Create your views here.
from django .http import HttpResponse
def set_cookie(request):
    response = HttpResponse("Cookie set!")
    response.set_cookie('username','Gayathri')
     
    return response
def get_cookie(request):
    username = request.COOKIES.get('username','guest')
    return HttpResponse(f"Hello, {username}!")
