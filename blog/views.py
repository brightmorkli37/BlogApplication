from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import NewUserForm, BlogForm

def index(request):
    blogs = Blog.objects.filter(status='published')
    categories = Category.objects.all()
    template_name = 'blog/index.html'
    context = {'blogs': blogs, 'categories': categories}
    return render(request, template_name, context)

def detail_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    template_name = 'blog/detail_view.html'
    context = {'blog': blog}
    return render(request, template_name, context)

def category_view(request, cat):
    category = get_object_or_404(Category, name=cat)
    posts = Blog.objects.filter(category=category)
    template_name = 'blog/categories.html'
    context = {'posts': posts, 'category': category}
    return render(request, template_name, context)

def user_login(request):
    template_name = 'blog/login.html'
    context = {'message': 'login failed, please try again'}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

        else:
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)

def user_logout(request):
    logout(request)
    return redirect('index')

def user_signup(request):
    form = NewUserForm
    error_message = ""
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('user_login')

        else: 
            error_message = "registration failed, please try again"
            form = NewUserForm()

    template_name = 'blog/register.html'
    context = {"error_msg": error_message, "form": form}
    return render(request, template_name, context)

# @login_required('blog/login.html')
def add_blog(request):
    categories = Category.objects.all()
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('index')

        else:
            form = BlogForm

    template_name = 'blog/add_blog.html'
    context = {"categories": categories, 'form': form}
    return render(request, template_name, context)