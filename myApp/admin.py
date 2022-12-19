from django.contrib import admin
from .models import Post
class post_admin(admin.ModelAdmin):
    pass
admin.site.register(Post,post_admin)
