from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket


# -------------------------------- TICKET --------------------------------------------
def ticket_create(request):
    form = TicketForm()
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            ticket = Ticket(title=title, description=description, image=image, user=request.user)
            ticket.save()
            return redirect('ticket-test')


    return render(request, template_name='litreviews/ticket-create.html', context={'form': form})


def ticket_update(request, id):
    ticket = Ticket.objects.get(id=id)
    message = ''
    if request.user == ticket.user:
        if request.method == "POST":
            form = TicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('ticket-test')
        else:
            form = TicketForm(instance=ticket)
    else:
        message = 'Vous n\'êtes pas autorisé à modifier ce ticket.'

    return render(request, template_name='litreviews/ticket-update.html', context={'form': form, 'message': message})


def ticket_delete(request, id):
    ticket = Ticket.objects.get(id=id)
    message = ''
    if request.user == ticket.user:
        if request.method == "POST":
            ticket.delete()
            return redirect('ticket-test')

    else:
        message = 'Vous n\'êtes pas autorisé à supprimer ce ticket.'

    return render(request, template_name='litreviews/ticket-delete.html', context={'ticket': ticket, 'message': message})

def ticket_test(request):
    return render(request, template_name='litreviews/test-ticket.html')


# --------------------------------- REVIEWS --------------------------------------------------




