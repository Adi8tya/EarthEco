from datetime import timezone
import random
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect,reverse
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import  reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from datetime import timedelta
from .models import Profile
from django.contrib.auth import logout


class UserRegisterView(generic.CreateView):
    #form_class = UserCreationForm
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')
# Create your views here.

class CustomLogoutView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        # Log out the user
        logout(request)

        # Render the login page
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        # Log out the user
        logout(request)

        # Render the login page
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    


class UserLoginView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    # Store current datetime in session
                    request.session['last_login'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
                    request.session.set_expiry(3600)  # 1 hour expiry

                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, self.template_name, {'form': form})


class ProfileView(View):
    template_name = 'profile.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        # Generate a random number between 1 and 100
        random_number = random.randint(1, 100)

        # Check if the cookie exists
        cookie_value = request.COOKIES.get('random_number', random_number)

        # Get last login time from session
        if 'last_login' in request.session:
            last_login = request.session['last_login']
            last_login_time = timezone.datetime.fromisoformat(last_login)
            last_login_formatted = last_login_time.strftime('%Y-%m-%d %H:%M:%S')
            login_message = f"Your last login was at {last_login_formatted}."
        else:
            login_message = "Your last login was more than one hour ago."

        # Create the response
        response = render(request, self.template_name, {
            'profile': profile,
            'random_number': cookie_value,
            'login_message': login_message
        })

        # Set the cookie with the random number if not already set
        if not request.COOKIES.get('random_number'):
            response.set_cookie('random_number', random_number, max_age=120)  # 120 seconds = 2 minutes

        return response
