from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

mymail = "a.d.zaluzhnyi@gmail.com"
sitemail = "a.z.contact.personalwebsite@gmail.com"

def main_page(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            html = render_to_string('mainpage/emails/contactform.html', {
                'full_name': full_name,
                'email': email,
                'message': message
            })
            try:
                send_mail('The contact form subject', 'This is the message', sitemail, [mymail], html_message=html)
            except:
                print('error')
            
            return HttpResponseRedirect("/")
    else:
        form = ContactForm()

    return render(request, "mainpage/index.html", {"form": form})
