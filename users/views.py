# users/views.py
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Tourist
from django.contrib.auth.models import User, Group

# class SignUp(CreateView):
#     form_class = UserCreationForm
#     template_name = "registration/signup.html"
#     success_url = reverse_lazy("rocks:home")

def UserRegister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            group = Group.objects.get(name='tourist')
            user.groups.add(group)
            user.save()
            login(request, user)
            return redirect('rocks:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class CreateProfilePageView(CreateView):
    model = Tourist
    template_name = 'users/create_profile.html'
    fields = ["first_name", "middle_name", "last_name", "email", "phone"]

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    success_url = reverse_lazy('rocks:home')


class UpdateProfilePageView(UpdateView):
    model = Tourist
    fields = ["first_name", "middle_name", "last_name", "email", "phone"]
    template_name = "users/create_profile.html"
    success_url = reverse_lazy('rocks:home')


class ShowProfilePageView(DetailView):
    model = Tourist
    template_name = 'users/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Tourist.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(users, pk=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
