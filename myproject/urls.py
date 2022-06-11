from django.urls import path

from .views import *

urlpatterns = [
    path('add/', MyProjectTemplateView.as_view(), name='add'),
    path('', MyProjectListView.as_view(), name='list'),
]
