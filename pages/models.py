from io import BytesIO
import os
from django.db import models
from django.urls import reverse
from PIL import Image
from django.core.files.base import ContentFile


# Create your models here.


class ArtWork(models.Model):

    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='assets/')
    thumbnail = models.ImageField(
        upload_to='thumbnails/', blank=True, null=True)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})

    def make_thumbnail(self, dst_image_field, src_image_field, size, name_suffix, sep='_'):
        # create thumbnail image
        image = Image.open(src_image_field)
        image.thumbnail(size, Image.ANTIALIAS)

        # separate path from extension
        dst_path, dst_ext = os.path.splitext(src_image_field.name)
        # lowercase extension
        dst_ext = dst_ext.lower()
        # build file name for dst
        dst_fname = dst_path + sep + name_suffix + dst_ext

        # check extension
        if dst_ext in ['.jpg', '.jpeg']:
            filetype = 'JPEG'
        elif dst_ext == '.gif':
            filetype = 'GIF'
        elif dst_ext == '.png':
            filetype = 'PNG'
        else:
            raise RuntimeError('unrecognized file type of "%s"' % dst_ext)

        # Save thumbnail to in-memory file as StringIO
        dst_bytes = BytesIO()
        image.save(dst_bytes, filetype)
        dst_bytes.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        dst_image_field.save(dst_fname, ContentFile(
            dst_bytes.read()), save=False)
        dst_bytes.close()

    def save(self, *args, **kwargs):
        # save for image
        super(ArtWork, self).save(*args, **kwargs)

        self.make_thumbnail(self.thumbnail, self.image, (800, 800), 'thumb')

        # save for thumbnail and icon
        super(ArtWork, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.storage.delete(self.image.name)
        self.thumbnail.storage.delete(self.thumbnail.name)
        return super().delete(*args, **kwargs)
