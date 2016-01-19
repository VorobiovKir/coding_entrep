from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post


# Create your views here.
def post_create(request):
    return HttpResponse('<h1>Create post</h1>')


def post_detail(request, id=None):
    # instance = Post.objects.get(id=16)
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': 'detail',
        'instance': instance,
    }
    return render(request, 'post_detail.html', context)


def post_list(request):
    queryset = Post.objects.all()
    if request.user.is_authenticated():
        context = {
            'title': request.user.username,
        }
    else:
        context = {
            'title': 'list',
        }
    context['object_list'] = queryset
    return render(request, 'index.html', context)


def post_update(request):
    return HttpResponse('<h1>Update post</h1>')


def post_delete(request):
    return HttpResponse('<h1>Delete post</h1>')
