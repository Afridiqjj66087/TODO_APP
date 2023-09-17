from django.urls import path
from . import views

urlpatterns =[
    path('addTask/',views.addTask,name='addTask'),
    # mark as done
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    # mark as undone
    path('Not_yet_done/<int:pk>/',views.Not_yet_done,name='Not_yet_done'),
    # EDIT feature
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    # Delete Feature 
     path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
]