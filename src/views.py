from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')
def education(request):
    return render(request, 'education.html')
def committess(request):
    return render(request, 'committess.html')
def organization(request):
    return render(request, 'organization.html')
def expertise(request):
    return render(request, 'expertise.html')