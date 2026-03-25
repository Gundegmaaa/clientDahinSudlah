from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from . import models


class HelloDjangoView(View):
    """Лаб №14 — class-based View + HttpResponse (HelloWorld хэсэг)."""
    message = 'Hello Django'

    def get(self, request):
        return HttpResponse('<h1>' + self.message + ' World</h1>')


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clubList'] = models.Club.objects.all()
        return context


class ClubListView(ListView):
    context_object_name = 'clubList'
    model = models.Club


class ClubDetailView(DetailView):
    context_object_name = 'clubDetails'
    model = models.Club
    template_name = 'basic_app/club_detail.html'


class ClubCreateView(CreateView):
    fields = ('name', 'location')
    model = models.Club


class ClubUpdateView(UpdateView):
    fields = ('name', 'location')
    model = models.Club


class ClubDeleteView(DeleteView):
    model = models.Club
    success_url = reverse_lazy('basic_app:list')
