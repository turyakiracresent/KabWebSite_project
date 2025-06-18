from django.urls import path
from .views import HomePage, ServicesPage, NewsPage, FacultiesPage        

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('services/', ServicesPage.as_view(), name='services'),
    path('news/', NewsPage.as_view(), name='news'),
    path('faculties/', FacultiesPage.as_view(), name='faculties'),
]   
