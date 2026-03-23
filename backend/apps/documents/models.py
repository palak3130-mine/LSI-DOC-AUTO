from django.db import models

class Document(models.Model):
    DOCUMENT_TYPE = (
        ('MAIN', 'Main Document'),
        ('SOURCE', 'Source Document'),
    )

    file = models.FileField(upload_to='documents/')
    doc_type = models.CharField(max_length=10, choices=DOCUMENT_TYPE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doc_type} - {self.id}"
