from django.contrib import admin
from blog.models import Post, Tag, Comment


admin.site.register(Post)
admin.site.register(Tag)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['post']
    list_display = ('post', 'author', 'text', 'published_at')
