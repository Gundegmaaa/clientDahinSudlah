from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from branch_app.models import Branch

from .models import Worker


def worker(request: HttpRequest) -> HttpResponse:
    workers = Worker.objects.select_related("branch").order_by("id").all()
    branches = Branch.objects.order_by("bname").all()
    return render(
        request,
        "worker_app/worker.html",
        {"workers": workers, "branches": branches},
    )


@require_http_methods(["POST"])
def worker_add(request: HttpRequest) -> HttpResponse:
    wname = (request.POST.get("txtWorker") or "").strip()
    branch_id = request.POST.get("branch_id")
    if wname and branch_id:
        branch = get_object_or_404(Branch, pk=branch_id)
        Worker.objects.create(wname=wname, branch=branch)
    return redirect("worker_app:worker")


@require_http_methods(["GET", "POST"])
def worker_edit(request: HttpRequest, id: int) -> HttpResponse:
    w = get_object_or_404(Worker.objects.select_related("branch"), pk=id)
    branches = Branch.objects.order_by("bname").all()
    if request.method == "POST":
        wname = (request.POST.get("txtWorker") or "").strip()
        branch_id = request.POST.get("branch_id")
        if wname:
            w.wname = wname
        if branch_id:
            w.branch = get_object_or_404(Branch, pk=branch_id)
        w.save()
        return redirect("worker_app:worker")
    return render(
        request,
        "worker_app/worker_edit.html",
        {"worker": w, "branches": branches},
    )


@require_http_methods(["GET"])
def worker_delete(request: HttpRequest, id: int) -> HttpResponse:
    w = get_object_or_404(Worker, pk=id)
    w.delete()
    return redirect("worker_app:worker")
