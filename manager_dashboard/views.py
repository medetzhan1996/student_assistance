from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from task_management.mixin_views import DemandMixin, DemandEditMixin
from task_management.models import Demand, DemandDistribution
from manager_dashboard.filters import DemandFilter
from .forms import DemandManagerForm, DemandDistributionManagerForm
from accounts.forms import RegisterForm
from task_management.forms import DemandDistributionForm
from accounts.models import CustomUser 
from task_management.mixin_views import DemandMixin
from task_management.models import Demand
from manager_dashboard.filters import DemandFilter, CallBackFilter
from main.models import CallBack
from django.db.models import Q


class TaskListView(DemandMixin, ListView):
    template_name = 'manager_dashboard/index.html'

    def get_queryset(self):
        qs = super().get_queryset() 
        qs = qs.filter(type_task__translations__title='Дипломная работа')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DemandFilter(self.request.GET, queryset=self.get_queryset())
        return context


class TaskDetailView(TemplateView):
    template_name = 'manager_dashboard/task/detail.html'

    def get(self, request, **kwargs):
        pk = self.kwargs.get('pk', None)
        demand = Demand.objects.get(pk=pk)
        demand_distribution = DemandDistribution.objects.get(demand=pk, is_expert_selected=True)
        return self.render_to_response({'demand': demand, 'demand_distribution': demand_distribution})


class TaskDocumentsDetailView(TemplateView):
    template_name = 'manager_dashboard/task/documents/detail.html'

    def get(self, request, **kwargs):
        pk = self.kwargs.get('pk', None)
        demand = Demand.objects.get(pk=pk)
        return self.render_to_response({'demand': demand})


class RegisterStudentCreateView(CreateView):
    template_name = 'manager_dashboard/student_register/form.html'
    form_class = RegisterForm
    success_url = reverse_lazy('manager_dashboard:task_list')
    

class TaskEditMixin:
    form_class = DemandManagerForm


class TaskCreateView(DemandMixin, TaskEditMixin, CreateView):
    template_name = 'manager_dashboard/task/form.html'
    distribution_form_class = DemandDistributionManagerForm
    demand_file_form_set = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['distribution_form'] = self.distribution_form_class()
        context['demand_file_form_set'] = self.get_demand_file_formset()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        demand_file_formset = self.get_demand_file_formset(
            data=request.POST, files_data=request.FILES, instance=None)
        distribution_form = self.distribution_form_class(request.POST)
        if form.is_valid() and distribution_form.is_valid() and demand_file_formset.is_valid():
            instance = form.save(commit=False)
            instance.is_expert_selected = True
            instance.save()
            demand_files = demand_file_formset.save(commit=False)
            distribution_form_obj = distribution_form.save(commit=False)
            distribution_form_obj.demand = instance
            distribution_form_obj.is_expert_selected = True
            distribution_form_obj.save()
            self.save_demand_file_formset(instance, demand_files)
            return redirect("manager_dashboard:task_list")

class TaskUdateView(DemandMixin, TaskEditMixin, UpdateView):
    template_name = 'manager_dashboard/task/form.html'
    distribution_form_class = DemandDistributionManagerForm
    demand_file_form_set = None

    def dispatch(self, *args, **kwargs):
        self.pk = self.kwargs.get('pk')
        self.demand = Demand.objects.get(pk=self.pk)
        self.demand_distribution = DemandDistribution.objects.get(demand=self.demand, is_expert_selected=True)
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['distribution_form'] = self.distribution_form_class(instance=self.demand_distribution)
        context['demand_file_form_set'] = self.get_demand_file_formset(instance=self.demand)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.demand)
        demand_file_formset = self.get_demand_file_formset(
            data=request.POST, files_data=request.FILES, instance=self.demand)
        distribution_form = self.distribution_form_class(request.POST, instance=self.demand_distribution)
        if form.is_valid() and distribution_form.is_valid() and demand_file_formset.is_valid():
            instance = form.save()
            demand_files = demand_file_formset.save(commit=False)
            distribution_form_obj = distribution_form.save(commit=False)
            distribution_form_obj.demand = instance
            distribution_form_obj.save()
            self.save_demand_file_formset(instance, demand_files)
            return redirect("manager_dashboard:task_list")

    
  
class CallBackListView(ListView):
    template_name = 'manager_dashboard/callback/list.html'
    model = CallBack
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CallBackFilter(self.request.GET, queryset=CallBack.objects.all())
        return context
