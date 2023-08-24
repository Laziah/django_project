# forms for the workers to record sales
from django.forms import ModelForm
from .models import *
class AddForm(ModelForm):
    class Meta:
        model=Product
        fields=['received_quantity','unit_price'] # received stock for workers to edit(incoming stock)


class SaleForm(ModelForm):
    class Meta:
        model=Sale
        fields=['quantity', 'amount_received','issued_to','branch_name','customer_location','phone',]


        