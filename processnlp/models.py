import time

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class NlpModel(models.Model):
    NLP_MODEL_NUM_CHOICES = (
        ('1', _('Number 1')),
        ('2', _('Number 2')),
        ('3', _('Number 3')),
        ('4', _('Number 4')),
        ('5', _('Number 5')),
    )
    original_text = models.TextField(_('Original text'))
    nlp_model_num = models.CharField(_('Nlp model number'), max_length=2, choices=NLP_MODEL_NUM_CHOICES)
    summary = models.TextField(_('Summary'), null=True, blank=True)
    datetime_created = models.DateTimeField(_('Datetime created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('Datetime modified'), auto_now=True)
    processing_time = models.DecimalField(_('Processing time'), max_digits=7, decimal_places=5, null=True, blank=True)

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = _('Nlp model')
        verbose_name_plural = _('Nlp models')

    def get_absolute_url(self):
        return reverse('processnlp:nlp_result', args=[self.id])
