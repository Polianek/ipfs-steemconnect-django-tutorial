from django.db import models
from django.forms import ModelForm
from ipfs_storage import InterPlanetaryFileSystemStorage


class Upload(models.Model):
    ipfs_file = models.FileField(storage=InterPlanetaryFileSystemStorage())

    def __str__(self):
        return self.ipfs_file.name

class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['ipfs_file',]
