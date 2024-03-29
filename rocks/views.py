from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from . import forms
from .forms import RockCreateForm
from .models import MountainPass


# Create your views here.
class MainView(ListView):
    model = MountainPass
    ordering = '-add_time'
    template_name = 'rocks/main_view.html'
    context_object_name = 'rocks'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.now()
        context['rocks_quantity'] = len(MountainPass.objects.all())
        return context


class RockView(ListView):
    model = MountainPass
    template_name = 'rocks/rock.html'
    context_object_name = 'rock'
    ordering = '-add_time'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['time_now'] = datetime.datetime.utcnow()
        context['rock'] = MountainPass.objects.get(id=_id)
        # return render(request, 'main_view.html', context)
        return context


# @login_required
class RockCreateView(PermissionRequiredMixin, CreateView):
    form_class = RockCreateForm
    model = MountainPass
    permission_required = ('rocks.add_mountainpass',
                           'rocks.change_mountainpass')
    context_object_name = 'rock'
    template_name = 'rocks/create.html'

    def form_valid(self, form):
        rock = form.save(commit=False)
        if self.request.method == 'POST':
            rock.tourist = self.request.user.tourist
            rock.RockForm = datetime.date.today()
            rock.save()
            return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.utcnow()
        return context

    success_url = reverse_lazy('rocks:home')


class RockUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('rocks.change_mountainpass')
    form_class = RockCreateForm
    model = MountainPass
    context_object_name = 'rock'
    template_name = 'rocks/update.html'
    success_url = '/'

    # success_url = f'/Rock<int:{_id}>
    def test_func(self):
        rock = self.get_object()
        if self.request.user == rock.tourist:
            return True
        return False

    def form_valid(self, form):
        form.instance.tourist = self.request.user.tourist
        return super().form_valid(form)

    # получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return MountainPass.objects.get(pk=_id)


class RockDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('rocks.delete_mountainpass')
    template_name = 'rocks/delete.html'
    queryset = MountainPass.objects.all()
    context_object_name = 'rock'
    success_url = '/'

    def test_func(self):
        rock = self.get_object()
        if self.request.user == rock.tourist:
            return True
        return False
