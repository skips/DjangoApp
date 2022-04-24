from django.urls import path
from .views import TopicsListView, TopicPostsDetailView, CreateTopicView, CreatePostView, LikePostView, \
                   CreateCommentView, PostDetailView, UserRegisterView

urlpatterns = []

urlpatterns += [
    path('', TopicsListView.as_view(), name='topics'),
    path('topic/<int:pk>/all_posts/', TopicPostsDetailView.as_view(), name='posts'),
    path('add_topic/', CreateTopicView.as_view(), name='add_topic'),
    path('topic/<int:pk>/all_posts/add_post/', CreatePostView.as_view(), name='add_post'),
    path('like/<int:pk>/', LikePostView, name='like_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('comment/<int:pk>', CreateCommentView.as_view(), name='add_comment'),
    path('register/', UserRegisterView.as_view(), name='register')
]
