from django.contrib import admin
from django.contrib import admin
from .models import Post

# Reference: https://docs.djangoproject.com/en/1.10/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_text', 'post_date']

admin.site.register(Post, PostAdmin)
