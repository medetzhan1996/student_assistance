from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class TypeTask(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=320)
    )

    def __str__(self):
        return self.title


class Subject(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=320)
    )

    def __str__(self):
        return self.title
