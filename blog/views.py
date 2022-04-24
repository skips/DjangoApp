from django.views.generic.edit import FormMixin
from blog.models import Topic, Post, Comment
from django.views.generic import ListView, DetailView, CreateView
from .forms import TopicForm, PostForm, CommentForm, SignUpForm
from django.shortcuts import redirect
from django.urls import reverse_lazy


class TopicsListView(ListView):
    model = Topic
    context_object_name = 'topics_list'
    template_name = "topics.html"
    paginate_by = 2


class TopicPostsDetailView(ListView):
    model = Post
    context_object_name = 'posts_list'
    template_name = "posts.html"
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(topic_id=self.kwargs['pk'])


class CreateTopicView(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = "add_topic.html"


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    def form_valid(self, form):
        form.instance.topic_id = self.kwargs['pk']
        return super().form_valid(form)


def LikePostView(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes_count += 1
    post.save()
    return redirect('post_detail', pk=post.id)


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm
    context_object_name = 'post_detail'
    template_name = 'post_detail.html'


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("login")
