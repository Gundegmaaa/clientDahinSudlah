from django.shortcuts import get_object_or_404, redirect, render
from .forms import BranchForm
from .models import Branch


def branch_list(request):
    branches = Branch.objects.all().order_by('name')
    return render(request, 'branch_app/branch_list.html', {'branches': branches})


def branch_create(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_app:branch_list')
    else:
        form = BranchForm()
    return render(request, 'branch_app/branch_form.html', {'form': form, 'title': 'Add Branch'})


def branch_update(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_app:branch_list')
    else:
        form = BranchForm(instance=branch)
    return render(request, 'branch_app/branch_form.html', {'form': form, 'title': 'Edit Branch'})


def branch_delete(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    if request.method == 'POST':
        branch.delete()
        return redirect('branch_app:branch_list')
    return render(request, 'branch_app/branch_confirm_delete.html', {'branch': branch})
