import os
from urllib.request import urlretrieve
from django.core.files import File
from django.db import models


class Images(models.Model):

    image_file = models.ImageField(
        upload_to='images/',
        verbose_name='Файл',
        blank=True,
        null=True
    )
    image_url = models.URLField(
        verbose_name='Ссылка',
        blank=True
    )

    miniature = models.ImageField(
        "Миниатюра",
        upload_to="miniature/",
    )

    def get_remote_image(self):
        '''Метод для загрузки изображения с url'''
        if self.image_url and not self.image_file:
            result = urlretrieve(self.image_url)
            self.image_file.save(os.path.basename(self.image_url),
                                     File(open(result[0], 'rb')))
            self.save()

    def save(self, *args, **kwargs):
        self.get_remote_image()
        super().save(*args, **kwargs)
