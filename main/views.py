from django.shortcuts import render, redirect
from .models import *
import datetime
from .forms import *
from django.contrib import messages

def visit_list(request):
    today = datetime.date.today()
    items = Visit.objects.filter(date=today)
    query = request.GET.get('date',None)
    print(query)
    if query:
        items = Visit.objects.filter(date=query)
    context = {
        "items":items
    }
    return render(request, 'list.html', context)

def add_patient(request):
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            myobject = form.save()
            messages.success(request, "Successfully Created Patient name: %s with the ID %d!"%(myobject.name,myobject.id))

            return redirect("/?id=%d"%(myobject.id))
    context = {
        "form": form
    }
    return render(request, 'add_patient.html', context)


def add_visit(request):
    form = VisitForm(initial={'patient': request.GET.get('id', None)})
    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            myobject = form.save()
            messages.success(request, "Successfully Created Visit at date %s at time %s!"%(myobject.date,myobject.time))
            return redirect("visit_list")

    context = {
        "form": form
    }
    return render(request, 'add_patient.html', context)
