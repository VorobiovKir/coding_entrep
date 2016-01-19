from django.contrib import admin

from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'timestamp', 'updated', 'content']
    list_display_links = ['updated']
    list_editable = ['content']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']

    class Meta:
        model = Post

# Register your models here.
admin.site.register(Post, PostModelAdmin)
