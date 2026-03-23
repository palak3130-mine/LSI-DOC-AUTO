from django.urls import path
from .views import UploadDocumentView, ProcessDocumentView, DocumentListView

urlpatterns = [
    path('list/', DocumentListView.as_view(), name='list'),
    path('upload/', UploadDocumentView.as_view(), name='upload'),
    path('process/', ProcessDocumentView.as_view(), name='process'),
]