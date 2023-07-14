from django.shortcuts import render
from .models import About, History

def about_view(request):
    about = About.objects.first()  # Retrieve the first About object
    return render(request, 'About/about.html', {'about': about})

def history_view(request):
    history = History.objects.first()  # Retrieve the first History object
    return render(request, 'About/history.html', {'history': history})
