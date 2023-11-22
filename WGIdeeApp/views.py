from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def landingPage(request):
    return render(request, 'landingPage.html')

def outgoings(request):
    if request.method == 'POST':
        form = forms.AusgabenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landingPage')
    else:
        form = forms.AusgabenForm()

    return render(request, 'outgoings.html', {'form': form})