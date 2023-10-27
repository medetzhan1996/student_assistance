from django.urls import path
from .import views

app_name = 'student_dashboard'

urlpatterns = [
    path('', views.DemandListView.as_view(), name='demand_list'),
    path('demand/create', views.DemandCreateView.as_view(), name='demand_create'),
    path('demand/update/<int:pk>', views.DemandUpdateView.as_view(), name='demand_update'),
    path('demand/delete/<int:pk>', views.DemandDeleteView.as_view(), name='demand_delete'),
    path('profile/', views.StudentProfileView.as_view(), name='student_profile'),
    path('profile/edit', views.StudentProfileEditView.as_view(), name='student_profile_edit'),
    path('balance/', views.MyBalanceView.as_view(), name='my_balance_list'),
    # path('demand/distribution/', views.DemandDistributionListView.as_view(), name='demand_distribution'),
    path('demand_distribution/<int:pk>/delete', views.DemandDistributionDeleteView.as_view(),
         name='demand_distribution_delete'),
    path('expert/choose/<int:pk>', views.ExpertChooseView.as_view(), name='expert_choose'),
    path('comment/create/<int:expert>', views.CommentCreateView.as_view(), name='comment_create'),
    path('expert/detail/<int:pk>', views.ExpertDetailView.as_view(), name='expert_detail'),
    path('notification/list', views.NotificationListView.as_view(), name='notification_list'),
    path('claim/create/<int:pk>', views.ClaimCreateView.as_view(), name='claim_create'),
    path('<str:room>/message/list', views.MessageListView.as_view(), name='message_list'),
    path('archive/<int:pk>', views.DemandArchiveView.as_view(), name='archive'),
    path('archive/list/', views.DemandArchiveListView.as_view(), name='archive_list'),
    path('finished/task/list/', views.FinishedTaskListView.as_view(), name='finished_task_list'),
    path('demand/detail/', views.DemandDetailView.as_view(), name='demand_detail'),
    path('action/delete/', views.ActionDeleleteView.as_view(), name='action_delete'),
]
