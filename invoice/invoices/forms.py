import requests
from django import forms
from django.forms import ModelForm
from invoices.models import Invoice


class InvoiceForm(ModelForm):

    orders = forms.MultipleChoiceField()

    class Meta:
        model = Invoice
        fields = ['number']

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields['orders'] = forms.MultipleChoiceField(
            label='Заказы',
            choices=self._get_choices()
        )
        self.fields['number'] = forms.CharField(
            label='Номер накладной',
            widget=forms.TextInput(attrs={'placeholder': 'Введите номер накладной'})
        )

    @staticmethod
    def _get_choices():
        r_api = requests.get('http://order:8000/api/v1/orders/?format=json')
        api_orders = []
        for o in r_api.json():
            if o['is_ready'] is True:
                api_orders.append(o['id'])

        existing_orders = set()
        orders_in_invoice = Invoice.objects.all()
        for o in orders_in_invoice:
            existing_orders.update(o.orders)

        choices_orders = set(api_orders) - existing_orders

        choices = [
            (order, 'Заказ №{}'.format(order))
            for order in choices_orders
        ]
        return choices

    def save(self, commit=True):
        self.instance.orders = list(map(int, self.cleaned_data['orders']))
        return super(InvoiceForm, self).save(commit=commit)

