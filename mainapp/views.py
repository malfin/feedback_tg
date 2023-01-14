from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from mainapp.forms import FeedbackForm
from mainapp.utils.tg import send_message_to_tg


def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            send_message_to_tg(first_name, phone_number, email, text)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = FeedbackForm()
    context = {
        'form': form,
    }
    return render(request, 'mainapp/index.html', context)
