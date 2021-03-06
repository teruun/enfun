from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from blog.models import Post
from .forms import UserRegistrationForm


def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)

		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			return render(request,
				'account/register_done.html',
				{'new_user': new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'account/register.html', {'user_form': user_form})

def register_done(request):
	return "done"

@login_required
def dashboard(request):
	posts = Post.objects.all()
	return render(request, 'account/dashboard.html', {'posts': posts})

