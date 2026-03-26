from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .models import Branch


def salbar(request: HttpRequest) -> HttpResponse:
    branches = Branch.objects.order_by("id").all()
    return render(request, "branch_app/branch.html", {"branches": branches})


@require_http_methods(["POST"])
def salbar_add(request: HttpRequest) -> HttpResponse:
    bname = (request.POST.get("txtBranch") or "").strip()
    if bname:
        Branch.objects.create(bname=bname)
    return redirect("branch_app:salbar")


@require_http_methods(["GET", "POST"])
def salbar_edit(request: HttpRequest, id: int) -> HttpResponse:
    branch = get_object_or_404(Branch, pk=id)
    if request.method == "POST":
        bname = (request.POST.get("txtBranch") or "").strip()
        if bname:
            branch.bname = bname
            branch.save(update_fields=["bname"])
        return redirect("branch_app:salbar")
    return render(request, "branch_app/branch_edit.html", {"bname": branch.bname})


@require_http_methods(["GET"])
def salbar_delete(request: HttpRequest, id: int) -> HttpResponse:
    branch = get_object_or_404(Branch, pk=id)
    branch.delete()
    return redirect("branch_app:salbar")
