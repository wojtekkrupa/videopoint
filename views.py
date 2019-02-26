from django.schortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

@login_required
def panel(request):
    return render(request, 'panel.html')
