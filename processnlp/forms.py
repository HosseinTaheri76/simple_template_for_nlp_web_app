from django.utils.translation import gettext as _
from django import forms
from django.core.validators import FileExtensionValidator

from .models import NlpModel


class NlpModelForm(forms.Form):
    nlp_model_num = forms.ChoiceField(choices=NlpModel.NLP_MODEL_NUM_CHOICES)
    original_text = forms.CharField(required=False)
    text_file = forms.FileField(validators=[FileExtensionValidator(['txt', ]), ], required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        file, text = cleaned_data.get('text_file'), cleaned_data.get('original_text')
        if not (text or file):
            raise forms.ValidationError(_('You must either upload a file or fill the text field.'))
        return cleaned_data

    def save(self):
        if self.errors:
            raise ValueError('you must call is_valid before calling save method.')
        cleaned_data = self.cleaned_data
        file, text = cleaned_data.get('text_file'), cleaned_data.get('original_text')
        original_text = file.read().decode('utf-8') if file else text
        nlp_model_num = cleaned_data.get('nlp_model_num')
        obj = NlpModel(original_text=original_text, nlp_model_num=nlp_model_num)
        obj.save()
        return obj

