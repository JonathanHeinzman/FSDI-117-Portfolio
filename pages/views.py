from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def about_me_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def contact_me_view(request):
    if request.method == 'POST':
        # Means the form has been submitted and is not empty
        form = ContactForm(request.POST)
        # Collect the data from the form and validate it
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Build the full email message
            message_body = (
                f' You have a new email from your portfolio contact form.\n\n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Message: {message}'
            )
            try: 
                send_mail(
                    "Email from portfolio contact form", # Subject
                    message_body, # Message body -> the user typed in the form
                    email, # From email -> the email address the user typed in the form
                    ['mrketchupman11@gmail.com'] # To: where you want to receive the email
                )
                # After sending the email
                form = ContactForm() # reset the form
                return render(request, 'pages/contact_me.html', {'form': form})
            except Exception as e:
                print(f'Error, sending email: {e}')
                return render(request, 'pages/contact_me.html', {'form': form})
        else:
            # if the from is not valid, render the form with error messages
            return render(request, 'pages/contact_me.html', {'form': form})

    else:
        form = ContactForm()
        return render(request, 'pages/contact_me.html', {'form': form})      
