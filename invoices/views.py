
from django.shortcuts import render, redirect, get_object_or_404
from .forms import InvoiceForm
from .models import Invoice
from .forms import InvoiceForm


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

def invoice_update(request, pk):
    invoices = get_object_or_404(Invoice, pk=pk)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoices)
        
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
        else:
            form = InvoiceForm(instance=invoices)
            return render(request, 'invoices/invoice_update.html')