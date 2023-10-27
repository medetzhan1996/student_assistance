from django.urls import path
from . import views
app_name = 'directory'
urlpatterns = [
    path('subject/search', views.SubjectSearchView.as_view(), name="subject_search"),
]
