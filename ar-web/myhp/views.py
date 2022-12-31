from django.shortcuts import render
from random import randint
from .models import MyhpModel
from .forms import  MyhpFormClass
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from .forms import ImageUploadForm


def myhpListView(request):
    ctx = {}
    qs = MyhpModel.objects.all()
    ctx["object_list"] = qs
    return render(request, "myhp/list.html", ctx)

def myhpDetailView(request, pk):
    ctx = {}
    q = get_object_or_404(MyhpModel, pk=pk)
    ctx["object"] = q
    return render(request, "myhp/detail.html", ctx)

def myhpCreateView(request):
    form = MyhpFormClass(request.POST or None)
    ctx = {"form": form}
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        obj = MyhpModel(title=title, content=content)
        obj.save()
        return redirect("myhp-list")
    return render(request, "myhp/form.html", ctx)


def myhpUpdateFormView(request, pk):
    obj = get_object_or_404(MyhpModel, pk=pk)
    initial_values = {"title": obj.title, "content":obj.content}
    form = MyhpFormClass(request.POST or initial_values)
    ctx = {"form": form}
    ctx["object"] = obj #ココです。
    if form.is_valid(): #フォームが正しくPOST送信された後の処理を記述
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        obj.title = title
        obj.content = content
        obj.save()
        if request.POST:
            return redirect("myhp-list")
    return render(request, "myhp/form.html", ctx)

def myhpDeleteView(request, pk):
    obj = get_object_or_404(MyhpModel, pk=pk)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
        return redirect("myhp-list")
    return render(request, "myhp/delete.html", ctx)

class ImageUploadView(CreateView):
    template_name = "myhp/image-upload.html"
    form_class = ImageUploadForm
    success_url = "/"


