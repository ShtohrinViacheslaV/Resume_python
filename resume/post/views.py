from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def post_home(request):
    post = Articles.objects.order_by('date')
    return render(request, 'post/post_home.html', {'post': post})


class PostDetailView(DetailView):
    model = Articles
    template_name = 'post/details_view.html'
    context_object_name = 'article'


class PostUpdateView(UpdateView):
    model = Articles
    template_name = 'post/create.html'
    form_class = ArticlesForm


class PostDeleteView(DeleteView):
    model = Articles
    success_url = '/post/'
    template_name = 'post/post-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Incorrect form'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'post/create.html', data)
