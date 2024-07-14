from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from Contact_Page import forms

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your messages send successfully') # Redirect to a success page
        else:
            # Print form errors to console for debugging
            print(form.errors)
            messages.error(request, 'Invalid! Please try again.')
    else:
        form = forms.ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)