from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse

from contact.forms import ContactForm

from contact.models import Contact



def create(request):
    form_action = reverse('create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
    }
        if form.is_valid():
            contact = form.save()
            return redirect('update', id_contact=contact.pk)
            

        return render(
            request,
            'contacts/create.html',
            context,
    )


    context = {
            'form': ContactForm(),
            'form_action': form_action,
    }

    return render(
        request,
        'contacts/create.html',
        context,
)

def update(request, id_contact):
    contact = get_object_or_404(
        Contact, pk=id_contact, show=True
    )
    form_action = reverse('update', args=(id_contact,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
    }
        if form.is_valid():
            contact = form.save()
            return redirect('update', id_contact=contact.pk)

        return render(
            request,
            'contacts/create.html',
            context,
    )


    context = {
            'form': ContactForm( instance=contact),
            'form_action': form_action,
    }

    return render(
        request,
        'contacts/create.html',
        context,
)

def delete(request, id_contact):
    contact = get_object_or_404(
        Contact, pk=id_contact, show=True
    )

    confirmation = request.POST.get('confirmation', 'no')
    print('confirmation', confirmation)

    if confirmation == 'yes':
        contact.delete()
        return redirect('home')

    return render(
        request,
        'contacts/contacts.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )
