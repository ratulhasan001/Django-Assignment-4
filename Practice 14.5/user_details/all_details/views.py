from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def home(request):
    if request.method == 'POST':
        userform = forms.userform(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('homepage')
    else:
        userform = forms.userform()
    return render(request, 'all.html', {'form' : userform})