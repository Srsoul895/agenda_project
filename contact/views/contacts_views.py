from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator


from contact.models import Contact

# Create your views here.
def home(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':  page_obj,
        'title': 'home',
    }

    return render(
        request,
        'contacts/home.html',
        context,
)

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('home')

    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) 
        ).order_by('-id')
    
    paginator = Paginator(contacts, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title': 'search',
    }

    return render(
        request,
        'contacts/home.html',
        context,
)

def contact(request, id_contact):
    single_contact = get_object_or_404(Contact, pk=id_contact, show=True)

    context = {
        'contact': single_contact,
        'title': 'contato',
    }

    return render(
        request,
        'contacts/contacts.html',
        context,
)