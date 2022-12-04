from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from .forms import CreatePollForm
from .models import Poll


# Create your views here.

# def Home(request):
#     return  render(request,"Home.html")


def public(request):
    polls = Poll.objects.all().order_by('-id')
    contest = {'polls': polls}
    print(polls)
    return render(request, 'public.html', contest)


def Home5(request):
    logout(request)
    return redirect('Home')


def Home2(request):
    if request.user.is_authenticated:
        return redirect('public')
    else:
        if request.method == 'POST':
            Username = request.POST.get('username')
            Password = request.POST.get('password')
            user = authenticate(username=Username, password=Password)

            if user is not None:
                login(request, user)
                return redirect('public')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'Home.html', context)


def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # print(user)
            # print(email)
            messages.success(request, 'Account was created for you can sign in now ' + user)

            return redirect( 'Home')

    context = {'form': form}
    return render(request, 'Home.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('public')
    else:
        form = CreatePollForm()
        context = {
        'form': form
        }
    return render(request, 'create-poll.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('result', poll.id)

    context = {
        'poll': poll
    }
    return render(request, 'view-poll.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }
    return render(request, 'result-poll.html', context)


from django.shortcuts import render

# Create your views here.

# Create your views here.

def profile(request):
    return render(request,'profile.html')

def profile_poll(request):
    user = request.user.username
    polls = Poll.objects.all().filter(user=user).order_by('-id')
    contest = {'polls': polls}
    print(polls)
    return render(request, 'profile-poll.html', contest)


def profile_poll_delete(request,poll_id):
    polls = Poll.objects.get(pk=poll_id)
    polls.delete()
    return redirect('profile_poll')
