from django.contrib import admin
from app.models import Post, CustomPermission
# Register your models here.
admin.site.register(Post)
admin.site.register(CustomPermission)