from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('add_task/',views.TaskAdd.as_view(),name='add_task'),
    path('show_task/',views.ShowTask.as_view(),name='show_task'),
]
