from rest_framework.serializers import ModelSerializer
from cabinet.models import Document
from rest_framework.viewsets import ModelViewSet

class DocumentModelSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"

class DocumentModelViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentModelSerializer
