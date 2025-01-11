from django.contrib import admin

from .models import MediaFile, ModelInner, ModelOuter

admin.site.register(MediaFile)
admin.site.register(ModelInner)
admin.site.register(ModelOuter)
