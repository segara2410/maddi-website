from django.forms import ModelForm

from .models import *

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = '__all__'

class ItemForm(ModelForm):
  class Meta:
    model = Item
    fields = '__all__'