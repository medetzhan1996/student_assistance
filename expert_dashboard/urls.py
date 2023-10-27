from django.urls import path
from . import views

app_name = 'expert_dashboard'

urlpatterns = [
    path('expert/profile/', views.ExpertProfileView.as_view(), name='expert_profile'),
    path('new_task/list', views.NewTaskListView.as_view(), name='new_task_list'),
    path('my_task/list', views.MyTaskListView.as_view(), name='my_task_list'),
    path('team_task/list', views.TeamTaskListView.as_view(), name='team_task_list'),
    path('team_task/create', views.TeamTaskCreateView.as_view(), name='team_task_create'),
    path('team_task/employee_day_rating', views.EmployeeDayRatingUpdateView.as_view(), name='team_task_employee_day_rating'),
    path('team_task/<int:pk>/update', views.TeamTaskUpdateView.as_view(), name='team_task_update'),
    path('waiting_task/list', views.WaitingTaskListView.as_view(), name='waiting_task_list'),
    path('resume/create/', views.ResumeCreateView.as_view(), name='resume_create'),
    path('notification/list', views.NotificationListView.as_view(), name='notification_list'),
    path('attached/document/list/<int:pk>', views.AttachedDocumentListView.as_view(), name='attached_document_list'),
    path('<str:room>/message/list', views.MessageListView.as_view(), name='message_list'),
    path('demand_distribution/delete/<int:pk>', views.DemandDistributionDeleteView.as_view(),
         name='demand_distribution_delete'),
    path('demand_completed_file/create/<int:pk>', views.CompletedFileCreateView.as_view(), name='demand_completed_file_create'),
    path('demand_completed_file/delete/<int:pk>', views.CompletedFileDeleteView.as_view(), name='demand_completed_file_delete'),
    path('demand/demand_distribution/detail', views.DemandDistributionDetailView.as_view(), name='demand_distribution_detail'),
]
