from django.views.generic import CreateView, DetailView
from django.urls import reverse

from .models import NlpModel


class NlpModelListCreateView(CreateView):
    model = NlpModel
    fields = ['original_text', 'nlp_model_num']
    template_name = 'processnlp/nlp_list_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nlp_models'] = NlpModel.objects.all()
        context['model_num_choices'] = NlpModel.NLP_MODEL_NUM_CHOICES
        return context


class NlpResultView(DetailView):
    model = NlpModel
    template_name = 'processnlp/nlp_result.html'
    context_object_name = 'nlp_model'
