from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # new 
    path('about/', AboutPageView.as_view(), name='about'),  # new
    path('contact/', ContactPageView.as_view(), name='contact'),  # new
    ]