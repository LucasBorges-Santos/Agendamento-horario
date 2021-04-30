from django.db import models


class Scheduling(models.Model):
    STATUS = (
        (1, 'Done'),
        (2, ' Will be done'),
    )
    name = models.CharField(max_length=255)
    done = models.CharField(
        max_length=1,
        choices=STATUS,
    )
    scheduling_date = models.DateTimeField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    """
    To create a new schedule, you need to import the module "datetime" this way:
    
        import datetime
        from pages.models import Scheduling
        
        date = datetime.datetime(<year>,<mouth>,<day>,<hour><minutes>,<seconds>,<milliseconds>)
        new_scheduling = Scheduling(nome="name", done=2,scheduling_date=date)
        new_scheduling.save()
    """
