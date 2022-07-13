from django.contrib import admin
from blog.models import Topic, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'likes_count', 'name', 'text')
    list_filter = ('topic', 'likes_count', 'name', 'text')
    search_fields = ('topic__name', 'name')
    fieldsets = [
        ('Post info', {'fields': ('likes_count', 'name', 'text')}),
        ('Additional info', {'fields': ('topic',)}),
    ]

    readonly_fields = ('id', 'likes_count')

    actions = ['drop_likes_count']

    def drop_likes_count(self, request, queryset):
        queryset.update(likes_count=0)


admin.site.register(Topic)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
