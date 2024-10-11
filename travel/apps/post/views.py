from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag, Comment
from django.db.models import Q
from .forms import SearchForm, CommentsForm
# from .forms import CommentForm
# Create your views here.

class CategoryListView(ListView):
    model = Post
    template_name = 'pages/category_list.html'
    context_object_name = 'post_category'
    paginate_by = 3
    # queryset = Post.objects.filter(category__slug=self.kwarqs['slug'])
    def get_queryset(self):
        return Post.objects.filter(
            category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_post'] = Category.objects.filter(
            slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
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
            tag__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['last_post'] = Post.objects.all()[:3]
        context['post_tags'] = Tag.objects.all()
        context['form'] = SearchForm(self.request.GET)
        return context

class BlogListPageView(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_at')
    template_name = 'pages/blog_list.html'
    context_object_name = 'posts' # указываем в html, в цикле Ror для листинга постов
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
        context['categories'] = Category.objects.all() # categories указываем в html в цикле For для листинга категорий
        context['last_post'] = Post.objects.all()[:3] # last_post указываем в html в цикле For для листинга категорий
        context['post_tags'] = Tag.objects.all() # last_post указываем в html в цикле For для листинга категорий
        context['form'] = SearchForm(self.request.GET)
        return context



class BlogDetailPageView(DetailView):
    template_name = 'pages/blog_details.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['last_post'] = Post.objects.all()[:3]
        context['post_tags'] = Tag.objects.all()
        context['form'] = SearchForm(self.request.GET)
        post = self.get_object()
        context['comments'] = Comment.objects.filter(post=post)
        context['comment_form'] = CommentsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.get_object()
            # comment.author = request.user
            comment.save()
            return redirect('blog_details', pk=self.get_object().pk)
        return self.render_to_response(self.get_context_data(form=form))

