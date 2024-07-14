from django.forms import ModelForm
from myapp.models import update_user

class add_form(ModelForm):
    class Meta:
        model = update_user
        fields = '__all__'
