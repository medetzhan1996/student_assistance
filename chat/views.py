from django.contrib.contenttypes.models import ContentType
from django.views.generic.base import TemplateView, View
from django.urls import reverse
from django.http import JsonResponse
from .forms import MessageForm
from .models import Message
from task_management.models import DemandDistribution
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class MessageCreateView(View):

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(DemandDistribution)
            obj = form.save(commit=False)
            obj.from_user = request.user
            obj.content_type = content_type
            obj.save()
            channel_layer = get_channel_layer()
            demand_distributions = DemandDistribution.objects.filter(
                demand__student=obj.content_object.demand.student).values_list('id')
            content_type = ContentType.objects.get(model='demanddistribution')
            message_count = Message.objects.filter(
                content_type=content_type,
                object_id__in=demand_distributions,
                is_read=False, from_user__role=2).count()
            data = {
                'type': 'chat_notification',
                'text': obj.text,
                'user_from': obj.from_user.email,
                'message_count': message_count,
                'demand_id': obj.content_object.demand.id,
                'demand_distribution_id': obj.content_object.id
            }
            group_manager = 'notification_%s' % obj.content_object.demand.student.id
            async_to_sync(channel_layer.group_send)(
                group_manager, data)
            # create_action(request.user, 'Новое сообщение', obj)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})

class MessageDeleteView(TemplateView, View):
    template_name = 'chat/message/delete.html'

    def post(self, request, pk=None):
        if pk:
            message = Message.objects.get(pk=pk)
            message.is_read = True
            message.save()
            return JsonResponse({'success': True})
        else:
            demand_distributions = DemandDistribution.objects.filter(
                demand__student=self.request.user).values_list('id')
            content_type = ContentType.objects.get(model='demanddistribution')
            messages = Message.objects.filter(
                content_type=content_type,
                object_id__in=demand_distributions)
            for message in messages:
                message.is_read = True
                message.save()
            return JsonResponse({'success': True, 'redirect_url': reverse('student_dashboard:demand_list')})