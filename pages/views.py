from django.views.generic.edit import FormView
from .forms import NewScheduling as NewSchedulingForm
from .models import Scheduling
from pages.models import *
from django.shortcuts import redirect, render


def HomePageView(request):
    user = request.user

    if user.is_authenticated:
        Scheduling.objects.filter(scheduling_date__lte=timezone.now(), user=user).update(scheduling_done='done')

        context = {
            'schedules': Scheduling.objects.filter(user=user)
        }
    else:
        context = {}

    return render(request, 'home.html', context=context)


def NewScheduling(request):
    user = request.user

    if user.is_authenticated:
        if request.method == 'POST':
            form = NewSchedulingForm(request.POST)

            if form.is_valid():
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
    else:
        return redirect('/')

    return render(request, 'Schedules/new_scheduling.html', {'form':form})
