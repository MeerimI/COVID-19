from django.urls import path
from .views import homepage, get_data

urlpatterns = [
    path('', homepage, name="homepage"),
    path('get_covid/', get_data, name="get_covid")
]
