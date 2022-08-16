from django.views.generic import FormView, DetailView
from django.urls import reverse

from .models import NlpModel
from .forms import NlpModelForm


class NlpModelListCreateView(FormView):
    form_class = NlpModelForm
    template_name = 'processnlp/nlp_list_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nlp_models'] = NlpModel.objects.all()
        context['model_num_choices'] = NlpModel.NLP_MODEL_NUM_CHOICES
        return context

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class NlpResultView(DetailView):
    model = NlpModel
    template_name = 'processnlp/nlp_result.html'
    context_object_name = 'nlp_model'
