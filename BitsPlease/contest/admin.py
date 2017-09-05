from django.contrib import admin
from .models import Question, Contest, Tag

admin.site.register(Question)
admin.site.register(Contest)
admin.site.register(Tag)
