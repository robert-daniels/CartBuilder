from django.shortcuts import redirect, render
from .models import Ingredient, Recipe, Allergy, Profile, RecipeIngredient, SimpleRecipe
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from djangoProject import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from . tokens import generate_token
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode



class SearchView(ListView):
    template_name = 'search.html'
    model = Recipe
    context_object_name = 'recipes'
    paginate_by = 10

    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#icontains
    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return self.model.objects.filter(recipe_name__icontains=query)
        else:
            return Recipe.objects.none()


# Create your views here.
def home(request):
    popular_recipes = Recipe.get_popular_recipes()
    ctx = {'popular_recipes': popular_recipes}
    return render(request, 'home.html', ctx)


def about(request):
    return render(request, 'about.html')


def recipes(request):
    recipe_list = SimpleRecipe.objects.all()
    context = {'full_recipe_list': recipe_list}
    return render(request, 'recipes.html', context)


# Not yet implemented
def recipe(request):
    return render(request, 'recipe.html')


def ingredients(request):
    return render(request, 'ingredients.html')


def allergies(request):
    return render(request, 'allergies.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    #My apologies but I was not able to find the correct variable names so I unfortunately have no idea which variable
    #names are correct or not. You'll either have to correct them yourself or tell me what they are so I can be the one
    #to correct them. Same applies for registration, signout, and activate methods.
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
    return render(request, 'login.html')

def registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request,
                         "Your Account has been successfully created. We have sent you a confirmation email, please confirm your email in order to activate your account.")
        # Welcome Email
        subject = "Welcome to GFG - Django Login!!"
        message = "Hello " + myuser.first_name + "|| \n" + "Welcome to GFG!! \n Thank you for visiting our website \n We have also sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thanking You\n The Cart Builder Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        return redirect('signin')
    return render(request, 'registration.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')
