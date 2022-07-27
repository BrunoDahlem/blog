from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from .models import Post
from django.db.models import Q, Count, Case, When
from comments.forms import FormComment
from comments.models import Comments
from django.contrib import messages
# Create your views here.


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

# Sobrescrevendo a function de ordenar a listView
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(post_published=True)
        qs = qs.annotate(
            number_comments=Count(
                Case(
                    When(comments__comment_published=True, then=1)
                )
            )
        )
        return qs


class PostSearch(PostIndex):
    def get_queryset(self):
        qs = super().get_queryset()

        term = self.request.GET.get('term')

        if not term:
            return qs

        qs = qs.filter(
            Q(post_title__icontains=term) |
            Q(post_autor__first_name__iexact=term) |
            Q(post_data__icontains=term) |
            Q(post_content__icontains=term) |
            Q(post_category__name_category__iexact=term)
        )

        return qs


class PostCategory(PostIndex):

    def get_queryset(self):
        qs = super().get_queryset()

        category = self.kwargs.get('category', None)

        if not category:
            return qs

        qs = qs.filter(post_category__name_category__iexact=category)
        return qs


class PostDetail(UpdateView):
    template_name = 'posts/post_detail.html'
    model = Post
    form_class = FormComment
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comments.objects.filter(
            comment_published=True, comment_post=post.id)

        context['comments'] = comments

        return context

    def form_valid(self, form):
        post = self.get_object()
        comment = Comments(**form.cleaned_data)
        comment.comment_post = post

        if self.request.user.is_authenticated:
            comment.comment_autor = self.request.user

        comment.comment_published = True

        comment.save()
        messages.success(
            self.request, 'Comentário enviado com sucesso! Aguarde revisāo!')
        return redirect('posts-detail', pk=post.id)
