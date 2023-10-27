from django.http import JsonResponse
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView

from crispy_forms.utils import render_crispy_form

from actions.utils import create_action
from accounts.forms import RegisterForm
from accounts.views import AuthMixin
from .mixin_views import DemandMixin, DemandEditMixin, DemandDistributionMixin, DemandDistributionEditMixin
from django.contrib import messages

# Создать заявку
from .models import Demand, DemandFile


class DemandRegisterCreateView(DemandMixin, DemandEditMixin, AuthMixin, CreateView):
    template_name = 'task_management/demand_register/form.html'
    register_form_class = RegisterForm
    demand_file_form_set = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = self.register_form_class()
        context['demand_file_form_set'] = self.get_demand_file_formset()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        demand_file_formset = self.get_demand_file_formset(
            data=request.POST, files_data=request.FILES, instance=None)
        register_form = self.register_form_class(request.POST)
        if form.is_valid() and register_form.is_valid() and demand_file_formset.is_valid():
            instance = form.save(commit=False)
            demand_files = demand_file_formset.save(commit=False)
            student = register_form.save()
            instance.student = student
            instance.save()
            self.save_demand_file_formset(instance, demand_files)
            self.user_auth()
            return JsonResponse({'success': True, 'redirect_url': reverse('student_dashboard:demand_list')})
        else:
            form_html = render_crispy_form(form)
            register_form_html = render_crispy_form(register_form)
            return JsonResponse({'success': False, 'form_html': form_html,
                                 'register_form_html': register_form_html})


class DemandDistributionUpdateView(DemandDistributionMixin, DemandDistributionEditMixin, UpdateView):
    template_name = 'task_management/demand_distribution/form.html'

    def get_initial(self):
        return {'status': 2}

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            label = 'Новый отклик, от эксперта ' + str(instance.expert)
            create_action(instance.demand.student, label, instance)
            messages.success(request, "Вы успешно отправили сумму заказа" )
            channel_layer = get_channel_layer()
            data = {
                'demand_distribution': instance.id,
                'demand': instance.demand.id,
                'count_expert': instance.demand.get_count_responsive_distributions(),
                'type': 'notification'
            }
            group_manager = 'notification_%s' % instance.demand.student.id
            return JsonResponse({'success': True, 'redirect_url': reverse('expert_dashboard:new_task_list')})
        form_html = render_crispy_form(form)
        return JsonResponse({'success': False, 'form_html': form_html})
