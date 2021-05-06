from django.shortcuts import redirect, render
from pages.models import *
from .forms import NewScheduling as NewSchedulingForm
import datetime, calendar
from .calendarFunction import calendarFunction


def HomePageView(request, month=datetime.date.today().month):
    user = request.user

    print(month)

    if user.is_authenticated:
        # atualizando 'scheduling_date' para done
        Scheduling.objects.filter(scheduling_date__lte=timezone.now(), user=user).update(scheduling_done='done')

        # verificando se existe algum agendamento
        schedules = Scheduling.objects.filter(user=user)
        calendar_values = calendarFunction(month)

        context = {
            'schedules': schedules,
            'calendar_values': calendar_values
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

    return render(request, 'Schedules/new_scheduling.html', {'form': form})


def UpdateScheduling(request, id):
    
    return render(request, 'Schedules/update_scheduling.html', {'form': form})


def DeleteScheduling(request, id):
    context = {}
    return render(request, 'Schedules/delete_scheduling.html', context=context)

