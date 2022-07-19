from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import PostForm, CommentForm
from .models import Post, Comments


def index(request):
    return render(request, 'main/src/index.html')


def about(request):
    return render(request, 'main/src/about.html')


def create(request):
    error = ''

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("forum"))
        else:
            error = 'Invalid post form'

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/src/create.html', context)


def add(request):
    error = ''

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("add_info"))
        else:
            error = 'Invalid post form'

    form = CommentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/src/add_info.html', context)


def all_comments(request):
    comments = Comments.objects.order_by('-id')
    return render(request, 'main/src/add_info.html', {'comments': comments})


def forum(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'main/src/forum.html', {'posts': posts})


def add_info(request, id):
    get_post = Post.objects.get(id=id)
    return render(request, 'main/src/add_info.html', {'get_post': get_post})


def logout(request):
    auth.logout(request)
    return render(request, 'main/src/index.html')


def edit_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = User.objects.get(username=username)
        if user is not None:
            if password == password2:
                user.set_password(password)
                user.save()
                return redirect(reverse("profile"))
    return redirect(reverse("profile"))


class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


class ProfilePage(TemplateView):
    template_name = "registration/profile.html"


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)
