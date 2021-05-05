from django.db import models
from django.utils import timezone
from users.models import User


class Scheduling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    scheduling_date = models.DateTimeField()
    scheduling_done = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.scheduling_done = 'Will be done'
        super(Scheduling, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    """
    To create a new schedule, you need to import the module "datetime" this way:
    
        import datetime
        from pages.models import Scheduling
        
        date = datetime.datetime(<year>,<mouth>,<day>,<hour><minutes>,<seconds>,<milliseconds>)
        new_scheduling = Scheduling(nome="name", scheduling_date=date)
        new_scheduling.save()
    """
