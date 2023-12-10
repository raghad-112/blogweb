from django.http import HttpResponse
from django.template import loader
from .models import User, Post, Comment, Category


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def users(request):
    users_list = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        ' users_list': users_list,
    }
    return HttpResponse(template.render(context, request))


def blogs(request):
    posts_list = Post.objects.all()
    template = loader.get_template('blogs.html')
    context = {
        ' posts_list': posts_list,
    }
    return HttpResponse(template.render(context, request))


def comments(request):
    comments_list = Comment.objects.all()
    template = loader.get_template('comments.html')
    context = {
        'comments_list': comments_list,
    }
    return HttpResponse(template.render(context, request))


def categories(request):
    categories_list = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'categories_list': categories_list,
    }
    return HttpResponse(template.render(context, request))


def blog_details(request, id):
    posts = Post.objects.get(id=id)
    template = loader.get_template('categories.html')
    context = {
        'blog_details': blog_details,
    }
    return HttpResponse(template.render(context, request))
