from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']
    list_filter = ['updated', 'timestamp']
    list_display_links = ['timestamp']
    search_fields = ['title', 'content']
    list_editable = ['title']
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)