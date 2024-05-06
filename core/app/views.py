from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, CustomPermission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'app/list_post.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  
    return render(request, 'app/post_detail.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('post_list') 


@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user
        post = Post.objects.create(title=title, content=content, author=author)
        post.save()
        return redirect('post_list')
    return render(request, 'app/create_post.html')

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user == post.author or request.user.custompermission.can_edit:
        if request.method == 'POST':
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()
            return redirect('post_list')
        return render(request, 'app/edit_post.html', {'post': post})
    else:
        return redirect('post_list')

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user == post.author or request.user.custompermission.can_delete:
        post.delete()
        return redirect('post_list')
    else:
        return redirect('post_list')

