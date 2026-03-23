from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Document
from apps.services.pipeline.document_updater import update_document

from rest_framework.generics import ListAPIView
from .serializers import DocumentSerializer

class DocumentListView(ListAPIView):
    queryset = Document.objects.all().order_by('-uploaded_at')
    serializer_class = DocumentSerializer

class UploadDocumentView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        doc_type = request.data.get('doc_type')

        if not file or not doc_type:
            return Response(
                {"error": "file and doc_type required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        document = Document.objects.create(
            file=file,
            doc_type=doc_type
        )

        return Response(
            {
                "message": "Uploaded successfully",
                "id": document.id
            },
            status=status.HTTP_201_CREATED
        )


class ProcessDocumentView(APIView):
    def post(self, request):
        try:
            main_doc = Document.objects.filter(doc_type="MAIN").first()
            source_docs = Document.objects.filter(doc_type="SOURCE")

            if not main_doc or not source_docs.exists():
                return Response(
                    {"error": "Main and at least one Source required"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # 🔥 MULTI SOURCE PROCESSING
            output_relative_path = update_document(main_doc, source_docs)
            
            # Generate full URL for the output file
            output_url = request.build_absolute_uri(settings.MEDIA_URL + output_relative_path.replace('\\', '/'))

            return Response(
                {
                    "message": "Processed successfully",
                    "file": output_url
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

