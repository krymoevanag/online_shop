from django.http import HttpResponse
from django.urls import path
def aPage(request):
    return HttpResponse("<h1>This is my testpage</h1>" )
urlpatterns = [
    path('', aPage),
]