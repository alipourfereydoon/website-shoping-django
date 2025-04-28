from django.contrib import admin
from .models import article, category,Comment


admin.site.register(article)
admin.site.register(category)
admin.site.register(Comment)


