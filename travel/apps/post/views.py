from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from django.db.models import Q
from .forms import SearchForm, CommentsForm
from django.db.models import Count

from rest_framework import generics, mixins, viewsets, permissions
from rest_framework.response import Response
from .models import Post, Category, Tag, Comment
from .serializers import PostSerializer
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ..accounts.custom_permission import IsAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination


# from .for import CommentForm
# Create your views here.

class CategoryListView(ListView):
    model = Post
    template_name = 'pages/category_list.html'
    context_object_name = 'post_category'
    paginate_by = 3

    # queryset = Post.objects.filter(category__slug=self.kwarqs['slug'])
    def get_queryset(self):
        return Post.objects.filter(
            category__slug=self.kwargs['slug']
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_post'] = Category.objects.filter(
            slug=self.kwargs['slug']
            )
        context['categories'] = Category.objects.annotate(num_posts=Count('post'))
        context['last_post'] = Post.objects.all()[:3]
        context['post_tags'] = Tag.objects.all()
        context['form'] = SearchForm(self.request.GET)
        return context


class TagListView(ListView):
    model = Tag
    template_name = 'pages/tag_list.html'
    context_object_name = 'tags'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(
            tag__slug=self.kwargs['slug']
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(num_posts=Count('post'))
        context['last_post'] = Post.objects.all()[:3]
        context['post_tags'] = Tag.objects.all()
        context['form'] = SearchForm(self.request.GET)
        return context


class BlogListPageView(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_at')
    template_name = 'pages/blog_list.html'
    context_object_name = 'posts'  # указываем в html, в цикле Ror для листинга постов
    paginate_by = 6

    def get_queryset(self):
        search_text = self.request.GET.get('query', None)
        if search_text is None:
            return Post.objects.all()
        q = self.model.objects.filter(
            Q(title__icontains=search_text) |
            Q(text__icontains=search_text) |
            Q(text2__icontains=search_text) |
            Q(text3__icontains=search_text)
            )
        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(
            num_posts=Count('post')
            )  # categories указываем в html в цикле For для листинга категорий
        context['last_post'] = Post.objects.all()[:3]  # last_post указываем в html в цикле For для листинга категорий
        context['post_tags'] = Tag.objects.all()  # last_post указываем в html в цикле For для листинга категорий
        context['form'] = SearchForm(self.request.GET)
        return context


class BlogDetailPageView(DetailView):
    template_name = 'pages/blog_details.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        post = self.get_object()
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(num_posts=Count('post'))
        context['last_post'] = Post.objects.all()[:3]
        context['post_tags'] = Tag.objects.all()
        context['form'] = SearchForm(self.request.GET)

        context['comments'] = Comment.objects.filter(post=post)
        context['comment_form'] = CommentsForm()
        context['comments_count'] = Comment.objects.filter(post=post).count()
        # context['categories_count'] = Category.objects.filter(post=post).count()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            comment.author = request.user
            comment.save()
            return redirect('blog_details', pk=self.get_object().pk)
        return self.render_to_response(self.get_context_data(form=form))


class PostPagePagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):  # ModelViewSet
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = PostPagePagination
    permission_classes = [IsAdminOrReadOnly]

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = Category.objects.all().values()
        return Response({'cats': [cats]})


class PostListCreateApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagePagination
