from audioop import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.timezone import make_aware

from .forms import FeedbackForm, SearchForm, OrderForm, ReviewForm, EcoEarthServiceRequestForm, JoinTeamForm, \
    ContactForm, EcoproductsSearchForm
from django.urls import reverse
import random
from datetime import timedelta, datetime

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from models import ServiceRequest, TeamApplication, WhyEcoEarth

from django.shortcuts import redirect



def index(request):
    booklist = Book.objects.all().order_by('id')[:10]
    last_login = request.session.get('last_login')

    if last_login:
        last_login_time = make_aware(datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S'))
        current_time = timezone.now()
        time_difference = current_time - last_login_time

        if time_difference.total_seconds() < 3600:  # Check if within 1 hour
            message = f"Your last login was on {last_login_time.strftime('%Y-%m-%d %H:%M:%S')}"
        else:
            message = "Your last login was more than one hour ago."
    else:
        message = "Your last login time is not available."

    return render(request, 'myapp/indexEco.html', {'booklist': booklist, 'message': message})


# To add
def indexEco(request):
    reasons = WhyEcoEarth.objects.all().order_by('id')[:10]
    last_login = request.session.get('last_login')

    if last_login:
        last_login_time = make_aware(datetime.strptime(last_login, '%Y-%m-%d %H:%M:%S'))
        current_time = timezone.now()
        time_difference = current_time - last_login_time

        if time_difference.total_seconds() < 3600:  # Check if within 1 hour
            message = f"Your last login was on {last_login_time.strftime('%Y-%m-%d %H:%M:%S')}"
        else:
            message = "Your last login was more than one hour ago."
    else:
        message = "Your last login time is not available."

    return render(request, 'myapp/indexEco.html', {'reasons': reasons, 'message': message})




def request_service(request):
    if request.method == 'POST':
        form = EcoEarthServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = ServiceRequest(
                service_name=form.cleaned_data['service_name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                urgency=form.cleaned_data['urgency'],
                max_budget=form.cleaned_data['max_budget']
            )

            service_request.save()

            # Redirect to a success page
            return redirect('myapp:application_success')
    else:
        form = EcoEarthServiceRequestForm()

    return render(request, 'myapp/request_services.html', {'form': form})


def join_team(request):
    if request.method == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            application = TeamApplication(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                position=form.cleaned_data['position'],
                cover_letter=form.cleaned_data['cover_letter']
            )
            application.save()
            return redirect('myapp:application_success')
    else:
        form = JoinTeamForm()
    return render(request, 'myapp/join_team.html', {'form': form})


def application_success(request):
    return render(request, 'myapp/application_success.html')




