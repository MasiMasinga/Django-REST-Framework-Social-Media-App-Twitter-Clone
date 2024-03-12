from rest_framework import serializers
from .models import Tweet, Comment, Like

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'tweet', 'text', 'created_at']

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment text cannot be empty")
        return value


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'tweet', 'created_at']

class TweetSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, required=False)
    likes = LikeSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Tweet
        fields = ['id', 'content', 'created_at', 'comments', 'likes']

    def validate_content(self, value):
        if len(value) > 280:
            raise serializers.ValidationError("Content is too long")
        return value

    def get_comments(self, obj):
        comments = Comment.objects.filter(tweet=obj)
        return CommentSerializer(comments, many=True).data

    def get_likes(self, obj):
        likes = Like.objects.filter(tweet=obj)
        return LikeSerializer(likes, many=True).data
