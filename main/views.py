from django.views.generic.base import View, TemplateView
from django.http import JsonResponse
from accounts.views import LoginView
from .forms import CallBackForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


class MainView(TemplateView):
    template_name = 'main/index.html'


class AboutView(TemplateView):
    template_name = 'main/about/list.html'


class CallBackFormView(TemplateView, View):
    template_name = 'main/callback/form.html'
    call_back_forms = CallBackForm

    def get(self, request):
        call_back_form = CallBackForm()
        return self.render_to_response({'call_back_form': call_back_form})

    def post(self, request):
        call_back_form = CallBackForm(request.POST)
        if call_back_form.is_valid():
            call_back_form.save()
            messages.success(request, "Вы успешно отправили сумму заказа" )
            return redirect('main:MainView')
        return self.render_to_response({'call_back_form': call_back_form})