from django.forms import ModelForm

from Robot.main.models import Site


class URLForm(ModelForm):
    class Meta:
        model = Site
        fields = ['url',]
