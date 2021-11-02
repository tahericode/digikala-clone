from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
# for add product in cart
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label=_('تعداد'),choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
