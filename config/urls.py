from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework.routers import DefaultRouter

# def index(request):
#     html_ = (f'<h1>Welcome to the Restaurant!</h1>'
#              '<a href="restaurant/menu/">Menu</a> <br>'
#              '<a href="restaurant/contactinfo/">Contact Information</a> <br>'
#              '<a href="restaurant/booking/">Booking Place</a> <br>'
#              '<a href="restaurant/orders/">Dishes Delivery</a> <br>'
#              )
#     return HttpResponse(html_)

def index(request):
    return render(request, 'restaurant/IndexPage.html')

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('restaurant.api_urls')),
] #+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
