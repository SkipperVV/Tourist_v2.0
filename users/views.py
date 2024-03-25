# users/views.py

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Tourist
from django.contrib.auth.models import Group


# Создаем здесь представления.

def home(request):
    return render(request, "users/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("create_user_profile")
    template_name = "registration/signup.html"


class CreateProfilePageView(CreateView):
    model = Tourist
    template_name = 'users/create_profile.html'
    fields = "__all__"

    # def add_to_group(self, request):
    #     user = super(CreateProfilePageView, self).save(request)
    #     tourust_group = Group.objects.get(name='gamer')
    #     tourust_group.user_set.add(user)

    def form_valid(self, form, request):
        user = super(CreateProfilePageView, self).save(request)
        tourist_group = Group.objects.get(name='tourist')
        tourist_group.user_set.add(user)
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class UpdateProfilePageView(UpdateView):
    model = Tourist
    fields = ["__all__"]
    template_name = "users/create_profile.html"


class ShowProfilePageView(DetailView):
    model = Tourist
    template_name = 'users/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Tourist.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(users, pk=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
