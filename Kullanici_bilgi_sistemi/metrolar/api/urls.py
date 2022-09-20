from django.urls import path
from metrolar.api import views as api_views

urlpatterns=[
    path('metrolar/', api_views.metro_list_create_api_view, name='metro-listesi'),
    path('metrolar/<int:pk>', api_views.metro_detail_api_view, name='metro-detay'),
] 