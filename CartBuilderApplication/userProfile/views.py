from django.shortcuts import  render, redirect
from .forms import NewUserForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
#from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this



# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Registration successful." )
			return redirect("login")
		
	else:
		form = NewUserForm()

	return render (request, "registration.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = LoginForm()
	return render(request, "login.html", context={"login_form":form})

def profile(request):
    return render(request, 'profile.html')

def logout_user(request):
    logout(request)
    return redirect('home')