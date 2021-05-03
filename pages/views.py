from django.views.generic.edit import FormView
from .forms import NewScheduling as NewSchedulingForm
from .models import Scheduling
from pages.models import *
from django.shortcuts import redirect, render


def HomePageView(request):
    user = request.user

    if user.is_authenticated:
        context = {
            'schedules': Scheduling.objects.filter(user=user)
        }
    else:
        context = {}

    return render(request, 'home.html', context=context)


def NewScheduling(request):
    if request.method == 'POST':
        form = NewSchedulingForm(request.POST)

        if form.is_valid():
            user = request.user
            scheduling_date = form.cleaned_data['scheduling_date']
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']

            new_schedule = Scheduling(
                user=user,
                name=name,
                scheduling_date=scheduling_date,
                phone_number=phone_number,
            )

            new_schedule.save()

            return redirect('/')

    else:
        form = NewSchedulingForm()

    return render(request, 'Schedules/new_scheduling.html', {'form':form})
