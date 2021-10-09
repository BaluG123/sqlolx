from django import forms
from testapp.models import Item
from django.contrib.auth.models import User

class CreateForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['name','place','item','item_name','about_item','item_image','price','description','condition','tags']

class SignUpform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
