from django import forms
from .models import Resume, Comment, Claim


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [
            'university',
            'speciality',
            'university_year_end',
            'now_study_university',
            'now_study_speciality',
            'now_study_university_year_end',
            'course',
            'current_city',
            'date_birth',
            'additional_education',
            'experience',
            'work_type',
            'subjects',
            'languages',
            'social_profile_networks',
            'support_document',
        ]
        labels = {
            'university': 'Университет',
            'speciality': 'Специальность',
            'university_year_end': 'Год окончания университета',
            'now_study_university': 'Теперь учитесь в университете:',
            'now_study_speciality': 'Теперь изучайте специальности:',
            'now_study_university_year_end': 'Теперь учитесь в университете в конце года:',
            'course': 'Курс:',
            'current_city': 'Текущий город проживания:',
            'date_birth': 'Дата рождения',
            'additional_education': 'Дополнительное образование:',
            'experience': 'Опыт',
            'work_type': 'Тип работы:',
            'subjects': 'Предметы',
            'languages': 'Языки, которые вы знаете',
            'social_profile_networks': 'Социальные сети профиля:',
            'support_document': 'Документ поддержки:'
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['rating', 'text']
        exclude = ('expert', 'student', 'date')


class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim
        fields = ['text']
        exclude = ('expert', )
