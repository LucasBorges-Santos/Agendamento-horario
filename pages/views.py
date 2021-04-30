from django.views.generic import TemplateView
from pages.models import *


class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['schedules'] = Scheduling.objects.all()

        return context
