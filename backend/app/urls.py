from django.urls import path
from .views import *

urlpatterns = [
    path('', ReactView.as_view(),name="list"),
    path('<int:pk>/', UpdateView.as_view(),name="update"),
]
