from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from .forms import LoginForm, RegisterForm


class AuthMixin:

    def user_auth(self):
        email = self.request.POST['email']
        password = self.request.POST['password1']
        user = authenticate(username=email, password=password)
        is_login = login(self.request, user, backend='accounts.authentication.EmailAuthBackend')
        print('is_login...', is_login)
        return True


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        if self.request.user.role == 1:
            return reverse_lazy('student_dashboard:demand_list')
        elif self.request.user.role == 2:
            return reverse_lazy('expert_dashboard:new_task_list')


class ExpertRegisterView(AuthMixin, generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/expert_signup.html'
    success_url = reverse_lazy('expert_dashboard:new_task_list')

    def form_valid(self, form):
        user = super().form_valid(form)
        self.user_auth()
        return user


class StudentRegisterView(AuthMixin, generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/student_signup.html'
    success_url = reverse_lazy('student_dashboard:demand_list')

    def form_valid(self, form):
        user = super().form_valid(form)
        self.user_auth()
        return user