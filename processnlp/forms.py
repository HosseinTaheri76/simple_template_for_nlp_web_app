import time

import torch
from datasets import Dataset

from django.utils.translation import gettext as _
from django import forms
from django.core.validators import FileExtensionValidator

from .models import NlpModel
from .model_1.helper_bert2bert import Helper

helper = Helper("processnlp/model_1/checkpoint-18138", do_tr_lowercase=False, source_prefix="",
                max_source_length=512,
                max_target_length=120, num_beams=4, ngram_blocking_size=3, early_stopping=None,
                use_cuda=torch.cuda.is_available(),
                batch_size=1, language="fa")


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
        start_time = time.time()
        if nlp_model_num == '1':
            inp_dict = {"input": [original_text.replace('\n', '')]}
            test_data = Dataset.from_dict(inp_dict)
            test_data = test_data.map(
                helper.preprocess_function,
                batched=True,
                load_from_cache_file=False
            )
            result = test_data.map(helper.generate_summary, batched=True, batch_size=helper.batch_size,
                                   load_from_cache_file=False)
            summary = result['predictions'][0]
        end_time = time.time()
        obj = NlpModel.objects.create(
            original_text=original_text,
            nlp_model_num=nlp_model_num,
            summary=summary,
            processing_time=round(end_time - start_time, 5)
        )
        return obj
