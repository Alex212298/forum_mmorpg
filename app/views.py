from datetime import datetime
from django.core.mail import send_mail
import requests
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect, render

from app.filters import RespFilter
from app.forms import AddPostForm, AddResp
from app.models import *
from django.views.generic import ListView, CreateView, DetailView, DeleteView


class PostsList(ListView):
    model = Posts
    template_name = 'index.html'
    context_object_name = 'posts'
    queryset = model.objects.order_by('-data_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resp'] = Repsponses.objects.all().count()
        context['title'] = 'Главная страница'
        return context



    def get_queryset(self):
        return Posts.objects.order_by('-data_create').select_related('user_id')

class RespSearch(LoginRequiredMixin, ListView):
    model = Repsponses
    template_name = 'my_posts.html'
    context_object_name = 'resp'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RespFilter(self.request.GET, queryset=self.get_queryset())
        return context
def addpage(request):
    if request.method == 'POST':
            form = AddPostForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                Posts.objects.create(**form.cleaned_data, user_id_id=user.id)
                return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'post_create.html', {'form': form, 'title': 'Добавление статьи'})


class PostOne(DetailView):
    model = Posts
    template_name = 'post_one.html'
    context_object_name = 'post'


def addresp(request):
    id = request.GET.get("id")
    post = Posts.objects.get(post_id=id)
    if request.method == 'POST':
        id = request.GET.get("id")
        post = Posts.objects.get(post_id=id)
        form = AddResp(request.POST)
        if form.is_valid():
            user = request.user
            Repsponses.objects.create(**form.cleaned_data, user_id_id=user.pk, post_id_id=id)
            return redirect('home')
    else:
        form = AddResp()
    return render(request, 'add_responses.html', {'form': form, 'title': "Отклик", 'post': post})


class RespDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Repsponses.objects.all()
    success_url = '/posts/my/'

def mail(request):
    resp = request.GET.get("r")
    mail_to = Repsponses.objects.get(pk=resp).user_id.email
    send_mail(
        'Твой отклик принят!',
        'Привет. Твой отклик принят!',
        None,
        [f'{mail_to}']
    )
    return redirect('my')