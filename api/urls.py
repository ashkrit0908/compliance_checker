from django.urls import path
from .views import check_compliance_api

urlpatterns = [
    path('check_compliance/', check_compliance_api, name='check_compliance'),
]
