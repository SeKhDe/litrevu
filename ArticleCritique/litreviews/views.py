from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket



def ticket_create(request):
    form = TicketForm()

    return render(request, template_name='litreviews/ticket-create.html', context={'form': form})