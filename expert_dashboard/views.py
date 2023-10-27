from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateResponseMixin, View
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from actions.mixin_views import ActionMixin
from django.views.generic.base import TemplateView
from chat.mixin_views import MessageMixin
from task_management.models import DemandDistribution, DemandFile, Demand, DemandCompletedFile
from team_task_management.models import Task,EmployeeDayRating
from task_management.mixin_views import DemandDistributionMixin, DemandMixin
from team_task_management.mixin_views import TaskMixin, TaskEditMixin
from accounts.models import Profile
from employment_portfolio.models import Comment
from employment_portfolio.forms import ResumeForm
from task_management.forms import DemandForm
from team_task_management.forms import TaskForm, EmployeeDayRatingForm
from datetime import date


class NewTaskListView(DemandDistributionMixin, ListView):
    template_name = 'expert_dashboard/new_task/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(expert=self.request.user.id, status=1)


class WaitingTaskListView(DemandDistributionMixin, ListView):
    template_name = 'expert_dashboard/waiting_task/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(expert=self.request.user.id, status__in=[2, 3])


class MyTaskListView(DemandDistributionMixin, ListView):
    template_name = 'expert_dashboard/my_task/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(expert=self.request.user.id, status=4)


class TeamTaskListView(TaskMixin, ListView):
    template_name = 'team_task_management/team_task/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        today = date.today()
        return qs.filter(user=self.request.user.id, date=today)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        rating_exists = EmployeeDayRating.objects.filter(
            date=today, user=self.request.user).exists()
        context['today'] = today
        context['s'] = rating_exists
        return context


class TeamTaskCreateView(TaskMixin, TaskEditMixin, CreateView):
    template_name = 'team_task_management/team_task/create.html'
    success_url = reverse_lazy('expert_dashboard:team_task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        return {
            'user': self.request.user
        }


class TeamTaskUpdateView(TaskMixin, UpdateView):
    template_name = 'team_task_management/team_task/update.html'
    success_url = reverse_lazy('expert_dashboard:team_task_list')
    fields = ('status', 'comment', )


class EmployeeDayRatingUpdateView(CreateView):
    form_class = EmployeeDayRatingForm
    template_name = 'team_task_management/team_task/employee_day_rating.html'

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return redirect('expert_dashboard:team_task_list')

class DemandDistributionDeleteView(DemandDistributionMixin, DeleteView):
    template_name = 'student_dashboard/demand/delete.html'
    success_url = reverse_lazy('expert_dashboard:new_task_list')


class ExpertProfileView(ListView):
    template_name = "expert_dashboard/profile/profile.html"
    model = Profile
    context_object_name = 'profiles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context


class ResumeCreateView(CreateView):
    form_class = ResumeForm
    template_name = 'expert_dashboard/resume/create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return redirect('expert_dashboard:new_task_list')


class NotificationListView(ActionMixin, ListView):
    template_name = 'expert_dashboard/notification/list.html'
    context_object_name = 'notifications'


class AttachedDocumentListView(ListView):
    template_name = 'expert_dashboard/attached_document/list.html'
    model = DemandFile
    context_object_name = 'documents'


class MessageListView(MessageMixin, ListView):
    template_name = 'expert_dashboard/chat/message/list.html'
    content_type_model = DemandDistribution

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demand'] = get_object_or_404(Demand, pk=self.room_split_0)
        return context


class CompletedFileCreateView(DemandMixin, TemplateResponseMixin, View):
    template_name = 'task_management/demand_completed_file/form.html'

    def get(self, request, *args, **kwargs):
        demand_completed_file_form_set = self.get_demand_completed_file_formset()
        return self.render_to_response({
            'demand_completed_file_form_set': demand_completed_file_form_set})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        demand_distribution = DemandDistribution.objects.get(pk=pk)
        demand = demand_distribution.demand.id
        instance = Demand.objects.get(pk=demand)
        demand_completed_file_form_set = self.get_demand_completed_file_formset(
            data=request.POST, files_data=request.FILES, instance=None)
        if demand_completed_file_form_set.is_valid():
            demand_completed_file = demand_completed_file_form_set.save(commit=False)
            self.save_demand_completed_file_formset(instance, demand_completed_file)
            return JsonResponse({'success': True, 'redirect_url': reverse('expert_dashboard:my_task_list')})
        demand_completed_file_form_set = self.get_demand_completed_file_formset()
        return JsonResponse({'success': False, 'demand_completed_file_form_set': demand_completed_file_form_set})

class CompletedFileDeleteView(DeleteView):
    template_name = 'task_management/demand_completed_file/delete.html'
    model = DemandCompletedFile
    success_url = reverse_lazy('expert_dashboard:my_task_list')

class DemandDistributionDetailView(TemplateResponseMixin, View):
    template_name = 'task_management/demand_distribution/detail.html'

    def get(self, request):
        pk = request.GET.get('id')
        demand_distribution = DemandDistribution.objects.get(pk=pk)
        return self.render_to_response({
            'demand_distribution': demand_distribution})






