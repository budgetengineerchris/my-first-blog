from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.http import HttpResponse, Http404


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method =="POST":
		form = PostForm(request.POST)
		if form.is_valid():
		    post = form.save(commit=False)
		    post.author = request.user
		    post.published_date = timezone.now()
		    post.save()
		    return redirect('blog:post_detail', pk=post.pk)

	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    poster = request.user

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
        	if post.author != request.user:
        		raise Http404("You are not allowed to edit this post.")

        	else:
	            post = form.save(commit=False)
	            #post.author = poster
	            post.published_date = timezone.now()
	            post.save()
	            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def category(request, category_name_slug):
	context_dict = {}
	category = get_object_or_404(Category, slug=category_name_slug)
	context_dict['category_name'] = category.name

	post = Post.objects.filter(category=category)
	#post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	context_dict['post'] = post
	context_dict['category'] = category

	return render(request, 'blog/category.html', context_dict)



