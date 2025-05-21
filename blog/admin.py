from django.contrib import admin
from .models import contacts,add_blogs, add_thought

admin.site.register(contacts)
admin.site.register(add_blogs)
admin.site.register(add_thought)