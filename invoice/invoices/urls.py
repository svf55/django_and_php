from django.conf.urls import url
from django.urls import path
from invoices.views import MainView, InvoiceView

urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^invoice/', InvoiceView.as_view(), name='add_invoice'),
    # url(r'^cars/catalog/$', CarsView.as_view(), name='catalog'),
    # path(r'cars/detail/<uuid:uuid>/', DetailCarView.as_view(), name='detail_car'),
]
