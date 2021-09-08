# ALL MODEL FORMS ARE STORED HERE
from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link', 'tags']
        # widgets are used to customize the form
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    # add class for fields
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            placeholder = 'Add '+ name
            field.widget.attrs.update({'class': 'input', 'placeholder': placeholder })
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})
        # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Description'})
