from django.contrib import admin
from .models import Question, Contest, Tag, Notice

admin.site.register(Question)
admin.site.register(Notice)
admin.site.register(Contest)
admin.site.register(Tag)
