from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import NewsForm
from .models import News


def news_list(request):
    news_items = News.objects.select_related('category').all()
    return render(request, 'news_app/news_list.html', {'news_items': news_items})


@require_http_methods(["GET", "POST"])
def news_create(request):
    form = NewsForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('news_list')
    return render(request, 'news_app/news_form.html', {'form': form, 'mode': 'create'})


@require_http_methods(["GET", "POST"])
def news_update(request, pk: int):
    instance = get_object_or_404(News, pk=pk)
    form = NewsForm(data=request.POST or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('news_list')
    return render(
        request,
        'news_app/news_form.html',
        {'form': form, 'mode': 'update', 'news': instance},
    )


@require_http_methods(["GET", "POST"])
def news_delete(request, pk: int):
    instance = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('news_list')
    return render(request, 'news_app/news_confirm_delete.html', {'news': instance})
