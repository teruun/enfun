from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
