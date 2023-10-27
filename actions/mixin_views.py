from .models import Action


class ActionMixin:
    model = Action
    context_object_name = 'actions'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user.id)


class ActionContextMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actions'] = Action.objects.filter(
            user=self.request.user.id).all()
        return context
