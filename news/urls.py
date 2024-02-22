from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('single/<str:news_slug>/', single_page, name='single'),
    path('category/<str:category_slug>/', category_page, name='category'),
]