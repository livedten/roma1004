from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import *
from .forms import *

# Create your views here.


class MyProjectListView(ListView):
    model = MyProject
    template_name = "list.html"


class MyProjectTemplateView(TemplateView):
    template_name = "add.html"

    def get(self, *args, **kwargs):
        formset = MyProjectFormSet(queryset=MyProject.objects.none())
        return self.render_to_response({"formset": formset})

    def post(self, *args, **kwargs):
        formset = MyProjectFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("list"))

        return self.render_to_response({"formset": formset})
