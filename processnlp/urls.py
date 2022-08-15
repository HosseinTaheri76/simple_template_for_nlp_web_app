from django.urls import path

from .views import NlpModelListCreateView, NlpResultView

app_name = 'processnlp'

urlpatterns = [
    path('', NlpModelListCreateView.as_view(), name='nlp_list_create'),
    path('result/<int:pk>/', NlpResultView.as_view(), name='nlp_result'),
]

