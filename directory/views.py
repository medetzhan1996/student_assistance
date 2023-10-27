from django.http import JsonResponse
from django.views.generic.base import View
from .models import Subject


# Поиск предмета
class SubjectSearchView(View):

    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.filter(
            translations__title__icontains=request.GET.get('q'))[:5]
        values = [{
            'id': subject.id,
            'title': subject.title} for subject in subjects]
        return JsonResponse(values, safe=False)
