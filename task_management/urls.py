from django.urls import path
from . import views

app_name = 'task_management'

urlpatterns = [
    path('demand_register/create/', views.DemandRegisterCreateView.as_view(), name='demand_register_create'),
    path('demand_distribution/<int:pk>/update/', views.DemandDistributionUpdateView.as_view(),
         name='demand_distribution_update'),
]
