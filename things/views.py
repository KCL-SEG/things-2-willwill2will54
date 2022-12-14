from django.http import HttpRequest
from django.shortcuts import render
from .forms import ThingForm

def home(request: HttpRequest):
    if request.method == "POST":
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ThingForm()

    return render(request, 'home.html', {'form': form})
