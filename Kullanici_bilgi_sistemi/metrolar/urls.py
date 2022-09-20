from django.urls import path
from . import views
from django.contrib import admin  
from metrolar import views
from django.conf import settings
from django.conf.urls.static import static

"""" movies/views.py deki fonksiyon isimlerimize göre url vermemizi ve
    bu url lere name vererek href="{"%" url 'İsparklar'%} url ismi vermemizi sağlar.
"""
urlpatterns = [
    path("Metrolar", views.Metrolar_list, name='Metrolarlink'),
    path("Hastaneler", views.Hastaneler_list, name='Hastanelerlink'),
    path("home", views.home, name='Homelink'),
    path("", views.home),
    path('admin/', admin.site.urls), 
    ]

 