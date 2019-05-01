from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post

# Create your views here.
# def post_list(request):
# 	posts = Post.objects.all()
# 	return render(request, 'blog/list.html', {'posts': posts})

class PostListView(ListView):
	model = Post
	context_object_name = 'posts'
	pagenate_by = 3
	template_name = 'blog/list.html'

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post,
		publish__year=year,
		publish__month=month,
		publish__day=day)
	print("thisispost:")
	print(post.id)
	return render(request, 'blog/detail.html', {'post':post})
