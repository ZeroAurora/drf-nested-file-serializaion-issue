from rest_framework import serializers
from .models import MediaFile, ModelInner, ModelOuter


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ["id", "file", "owner", "created_at"]
        read_only_fields = ["id", "owner", "created_at"]


class InnerSerializer(serializers.ModelSerializer):
    file = MediaFileSerializer(read_only=True)

    class Meta:
        model = ModelInner
        fields = ["id", "file"]
        read_only_fields = ["id"]

class OuterSerializer(serializers.ModelSerializer):
    inner = serializers.SerializerMethodField(read_only=True)
    file = MediaFileSerializer(read_only=True)

    class Meta:
        model = ModelOuter
        fields = ["id", "inner", "file"]
        read_only_fields = ["id"]

    def get_inner(self, obj):
        return InnerSerializer(obj.inner).data
