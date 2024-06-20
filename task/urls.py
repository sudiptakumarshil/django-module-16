from django.urls import path
from .views import add_task, delete_task, edit_task, show_task

urlpatterns = [
    path('add/', add_task,name='task.add'),
    path('show/', show_task,name='task.show'),
    path('edit/<int:id>', edit_task,name='task.edit'),
    path('delete/<int:id>', delete_task,name='task.delete')
]