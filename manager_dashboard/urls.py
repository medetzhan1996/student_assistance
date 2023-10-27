from django.urls import path
from . import views

app_name = 'manager_dashboard'

urlpatterns = [
    path('task/list', views.TaskListView.as_view(), name='task_list'),
    path('task/detail/<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/documents/detail/<int:pk>', views.TaskDocumentsDetailView.as_view(), name='task_documents_detail'),
    path('register/student/', views.RegisterStudentCreateView.as_view(), 
        name='register_student_create'),
    path('task/create/', views.TaskCreateView.as_view(), 
        name='task_create'),
    path('task/update/<int:pk>>', views.TaskUdateView.as_view(), 
        name='task_update'),
    path('call_back/list', views.CallBackListView.as_view(), name='call_back_list'),
]
