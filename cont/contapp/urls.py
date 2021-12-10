from django.urls import path
from . import views
from .views import (ContCreateView, ContDetailView)

urlpatterns = [
    path('cont/<int:pk>/', ContDetailView.as_view(), name='count-detail'),
    path('', ContCreateView.as_view(), name='home'),

]