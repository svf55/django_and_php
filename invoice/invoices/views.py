from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from invoices.forms import InvoiceForm


class MainView(TemplateView):
    template_name = "base.html"


class InvoiceView(FormView):
    template_name = 'add_invoice.html'
    form_class = InvoiceForm
    success_url = '/invoice/'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            messages.add_message(self.request, messages.INFO, 'Data uploaded to the server.')
        else:
            messages.add_message(self.request, messages.ERROR, 'Validation error.')

        return super().form_valid(form)

