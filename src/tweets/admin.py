from django.contrib import admin
from .models import Tweet, Comment, Like

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'tweet', 'text', 'created_at')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'tweet', 'created_at')

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)