from rest_framework import viewsets, parsers
from .models import MediaFile, ModelInner, ModelOuter
from .serializers import MediaFileSerializer, InnerSerializer, OuterSerializer


class MediaFileViewSet(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
    parser_classes = [parsers.FileUploadParser, parsers.MultiPartParser]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class InnerViewSet(viewsets.ModelViewSet):
    queryset = ModelInner.objects.all()
    serializer_class = InnerSerializer


class OuterViewSet(viewsets.ModelViewSet):
    queryset = ModelOuter.objects.all()
    serializer_class = OuterSerializer
