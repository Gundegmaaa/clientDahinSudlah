from django.shortcuts import get_object_or_404, redirect, render
from .forms import WorkerForm
from .models import Worker


def worker_list(request):
    workers = Worker.objects.select_related('branch').all().order_by('first_name', 'last_name')
    return render(request, 'worker_app/worker_list.html', {'workers': workers})


def worker_create(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker_app:worker_list')
    else:
        form = WorkerForm()
    return render(request, 'worker_app/worker_form.html', {'form': form, 'title': 'Add Worker'})


def worker_update(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == 'POST':
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('worker_app:worker_list')
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'worker_app/worker_form.html', {'form': form, 'title': 'Edit Worker'})


def worker_delete(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == 'POST':
        worker.delete()
        return redirect('worker_app:worker_list')
    return render(request, 'worker_app/worker_confirm_delete.html', {'worker': worker})
