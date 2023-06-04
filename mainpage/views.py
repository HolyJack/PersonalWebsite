from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm

def main_page(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(".")
    
    form = ContactForm()

    
    return render(request, "mainpage/index.html", {"form": form})
