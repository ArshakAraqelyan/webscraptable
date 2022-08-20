from django.urls import path

from webtables_bs4 import views

urlpatterns = [
    path('', views.webtablebs4, name='webtablebs4')
]