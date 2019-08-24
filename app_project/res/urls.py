from django.urls import path

from . import views

urlpatterns = [
    path('country/create/', views.CountryCreateView.as_view(), name='res_country_create')
]
