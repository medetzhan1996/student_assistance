from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from accounts.views import LoginView, ExpertRegisterView, StudentRegisterView


urlpatterns = i18n_patterns(
    path('', include('main.urls', namespace='main')),
    path('student/dashboard/', include('student_dashboard.urls', namespace='student_dashboard')),
    path('task/management/', include('task_management.urls', namespace='task_management')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('expert/register/', ExpertRegisterView.as_view(), name='expert_register'),
    path('student/register/', StudentRegisterView.as_view(), name='student_register'),
)

urlpatterns += [
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # change password urls
    path('password-change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # reset password urls
    path('password-reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('expert_dashboard/', include('expert_dashboard.urls', namespace='expert_dashboard')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('directory/', include('directory.urls', namespace='directory')),
    path('manager_dashboard/', include('manager_dashboard.urls', namespace='manager_dashboard')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

