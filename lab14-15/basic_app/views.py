from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from basic_app.forms import (
    UserForm,
    UserProfileInfoForm,
    UserUpdateForm,
    UserProfileUpdateForm,
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


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'user_pic' in request.FILES:
                profile.user_pic = request.FILES['user_pic']

            profile.save()
            registered = True
        else:
            # Re-render form with errors.
            pass
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(
        request,
        'basic_app/registration.html',
        {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered,
        },
    )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            return HttpResponse('Бүртгэлгүй хэрэглэгч байна.')
        return HttpResponse('invalid login details')

    return render(request, 'basic_app/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return render(request, 'basic_app/special.html', {})


@login_required
def profile_update(request):
    user = request.user
    profile, _created = models.UserProfileInfo.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('basic_app:profile'))
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = UserProfileUpdateForm(instance=profile)

    return render(
        request,
        'basic_app/profile.html',
        {'user_form': user_form, 'profile_form': profile_form},
    )
