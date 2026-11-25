
from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice

        fields = [
            'customer_name',
            'invoice_number',
            'amount',
            'is_paid',
            'notes',
        ]

        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter customer name'
            }),

            'invoice_number': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter invoice number'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter amount'
            }),

            'is_paid': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 accent-blue-600 mt-2'
            }),

            'notes': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 mt-1 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter invoice notes',
                'rows': 5
            }),
        }
