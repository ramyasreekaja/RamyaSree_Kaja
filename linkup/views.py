

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm



# View to list all contacts
def linkup_list(request):
    contacts = Contact.objects.all()
    return render(request, 'linkup/linkup_list.html', {'contacts': contacts})

# View to create a new contact
def linkup_form(request):
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('linkup_list')
    else:
        form = Contactform()
    return render(request, 'linkup/linkup_form.html', {'form': form})

# View to display contact details
def linkup_detail(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'linkup/linkup_detail.html', {'contact': contact})

# View to edit an existing contact
def linkup_edit(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('linkup_detail', id=contact.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'linkup/linkup_update.html', {'form': form})

# View to delete a contact
def linkup_confirm_delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == "POST":
        contact.delete()
        return redirect('linkup_list')
    return render(request, 'linkup/linkup_confirm_delete.html', {'contact': contact})

    

# #view for creating a contact
# def linkup_form(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('linkup_list')
#     else:
#         form = ContactForm()
#     return render(request, 'linkup/linkup_create.html', {'form': form})


def linkup_update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('linkup_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'linkup/linkup_update.html', {'form': form, 'contact': contact})


def linkup_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('linkup:linkup_list')  # Redirect to the contact list page
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'linkup/linkup_create.html', context)

def linkup_update(request, id):
    contact = get_object_or_404(Contact, id=id)
    # Rest of the view logic
    return render(request, 'linkup/linkup_update.html', {'contact': contact})
