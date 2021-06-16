from django import forms

from .models import Order


class CreateOrderForms(forms.ModelForm):
     class Meta:
         model = Order
         fields = '__all__'

#здесь мы валидируем
     def clean_phone(self):
         data = self.cleaned_data
         phone = data.get('phone')

         if not phone.startswith('+996'):
             raise forms.ValidationError('Number should start with +996')
         if len(phone) != 13:
             raise forms.ValidationError('Invalid phone number')
         return phone

