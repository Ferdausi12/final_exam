from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('add_task/',views.TaskAdd.as_view(),name='add_task'),
    path('show_task/',views.ShowTask.as_view(),name='show_task'),
    path('update_task/<int:pk>',views.TaskUpdate.as_view(),name='update_task'),
    path('delete_task/<int:pk>',views.DeleteTask.as_view(),name='delete_task'),
    path('complete_task/',views.CompletedTask.as_view(), name='complete_task'),
]
