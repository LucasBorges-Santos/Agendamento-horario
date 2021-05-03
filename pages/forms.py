from django import forms
from .models import Scheduling
from django.core.exceptions import ValidationError
from .models import Scheduling
import datetime


class DateTimeInput(forms.DateTimeInput):
    input_type = 'text'


class NewScheduling(forms.ModelForm):
    class Meta:
        model = Scheduling
        fields = ['name', 'scheduling_date', 'phone_number']
        widgets = {'scheduling_date': DateTimeInput()}
        help_texts = {'phone_number': 'DDD plus the phone number'}

    def clean_scheduling_date(self):
        data = self.cleaned_data['scheduling_date']

        schedules = Scheduling.objects.filter(scheduling_date=data)

        if schedules.first() is not None:
            raise ValidationError('Already have an scheduling for this date')

        elif data < datetime.datetime.now():
            raise ValidationError('Invalid date')

        return data

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']

        if phone == '':
            return phone

        elif len(phone) == 11 or len(phone) == 10:
            for character in phone:
                if character.isdigit():
                    pass
                else:
                    raise ValidationError('enter a valid phone number')

        else:
            raise ValidationError('enter a valid phone number')

        return phone
