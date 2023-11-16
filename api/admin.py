from django.contrib import admin
from .models import Post, Comment
from django.db import models
from django.utils.safestring import mark_safe


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_created', 'date_updated')

    def formatted_content(self, obj):
        return mark_safe(obj.content)
    formatted_content.short_description = 'Content'

    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget},
    }

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'date_created', 'post', 'active')
    list_filter = ('active', 'date_created')
    # search_fields = ('content', 'post')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

