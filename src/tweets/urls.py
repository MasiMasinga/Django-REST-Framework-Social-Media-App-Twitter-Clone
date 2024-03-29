from django.urls import path
from .views import (TweetListCreateView, CommentListCreateView, LikeListCreateView,
                    TweetRetrieveUpdateDestroyView, CommentListView, 
                    CommentCreateView, CommentRetrieveUpdateDestroyView, LikeRetrieveUpdateDestroyView)

urlpatterns = [
    path('', TweetListCreateView.as_view(), name='tweet_list'),
    path('<int:pk>/', TweetRetrieveUpdateDestroyView.as_view(), name='tweet_detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment_list'),
    path('<int:tweet_id>/comments/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment_detail'),
    path('likes/', LikeListCreateView.as_view(), name='like_list'),
    path('likes/<int:pk>/', LikeRetrieveUpdateDestroyView.as_view(), name='like_detail'),
]