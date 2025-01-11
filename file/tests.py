import json

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .models import ModelOuter, ModelInner, MediaFile


class IsStr:
    def __eq__(self, other):
        return isinstance(other, str)


class TestOuterViewSet(TestCase):
    maxDiff = None

    def test_nested(self):
        user = User.objects.create_user(
            username="test",
        )
        inner_file = MediaFile.objects.create(
            file=SimpleUploadedFile("inner.txt", b"test"),
            owner=user,
        )
        inner_obj = ModelInner.objects.create(
            file=inner_file,
        )
        outer_file = MediaFile.objects.create(
            file=SimpleUploadedFile("outer.txt", b"test"),
            owner=user,
        )
        outer_obj = ModelOuter.objects.create(
            inner=inner_obj,
            file=outer_file,
        )
        response = self.client.get(
            f"/outer/{outer_obj.pk}/", content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        body = json.loads(response.content)
        self.assertDictEqual(
            body,
            {
                "id": outer_obj.pk,
                "file": {
                    "id": str(outer_file.pk),
                    "file": f"http://testserver/media_files/{outer_file.pk}.txt",
                    "owner": user.pk,
                    "created_at": IsStr(),
                },
                "inner": {
                    "id": inner_obj.pk,
                    "file": {
                        "id": str(inner_file.pk),
                        "file": f"http://testserver/media_files/{inner_file.pk}.txt",
                        "owner": user.pk,
                        "created_at": IsStr(),
                    },
                },
            },
        )


class TestInnerViewSet(TestCase):
    maxDiff = None

    def test_nested(self):
        user = User.objects.create_user(
            username="test",
        )
        inner_file = MediaFile.objects.create(
            file=SimpleUploadedFile("inner.txt", b"test"),
            owner=user,
        )
        inner_obj = ModelInner.objects.create(
            file=inner_file,
        )
        response = self.client.get(
            f"/inner/{inner_obj.pk}/", content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        body = json.loads(response.content)
        self.assertDictEqual(
            body,
            {
                "id": inner_obj.pk,
                "file": {
                    "id": str(inner_file.pk),
                    "file": f"http://testserver/media_files/{inner_file.pk}.txt",
                    "owner": user.pk,
                    "created_at": IsStr(),
                },
            },
        )
