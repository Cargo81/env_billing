
from django.shortcuts import render, redirect
from .forms import InvoiceForm
from .models import Invoice


def invoice_list(request):
    invoices = Invoice.objects.all()

    context = {
        'invoices': invoices
    }

    return render(request, 'invoices/invoice_list.html', context)


def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('invoice_list')

    else:
        form = InvoiceForm()

    return render(request, 'invoices/invoice_create.html', {
        'form': form
    })
