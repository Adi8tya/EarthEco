from django.shortcuts import render
from django.template.loader import render_to_string

from contact.forms import ContactForm
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            order_number = form.cleaned_data['order_number']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['content']

            html = render_to_string('email_response.html', {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'order_number': order_number,
                'subject': subject,
                'message': message,
            })

            contact = form.save()
            contact.save()

            if (order_number):
                subject_to_send = subject + ' | ' + order_number
            else:
                subject_to_send = subject

            #send_mail(contact.subject, subject_to_send, contact.email, ['earthecoo@gmail.com'], html_message=html)
            send_mail(subject_to_send, contact.content, contact.email, ['earthecoo@gmail.com'], html_message=html)
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
