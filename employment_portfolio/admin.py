from django.contrib import admin

from .models import Resume, Portfolio, Comment, Claim

admin.site.register(Resume)
admin.site.register(Portfolio)
admin.site.register(Comment)
admin.site.register(Claim)
