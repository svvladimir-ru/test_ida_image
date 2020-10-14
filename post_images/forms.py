from urllib.error import HTTPError
from urllib.request import urlopen
import mimetypes
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from .models import Images


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = ('image_url', 'image_file')

    def clean_url(self):
        '''Валидация поля url для проверки корректности ссылки'''
        image_url = self.cleaned_data.get("image_url")

        if image_url == "":
            return image_url

        def valid_url_mimetype(
                image_url: str, mimetype_list: list = 'images') -> bool:
            '''Проверка того, что ссылка является изображением'''
            mimetype, _ = mimetypes.guess_type(image_url)
            if mimetype:
                return any([mimetype.startswith(m) for m in mimetype_list])
            else:
                return False

        try:
            urlopen(image_url)
        except HTTPError:
            raise ValidationError("Проверьте работоспособность ссылки")

        if image_url and not valid_url_mimetype(image_url):
            raise ValidationError(
             "Неверное расширение файла. "
             "Ссылка должна оканчиваться расширением изображения "
             )
        return image_url


class SizeForm(forms.Form):
    '''Форма для изменения размера изображения'''
    width = forms.IntegerField(
        required=False, label="Ширина", validators=[MinValueValidator(1)])
    height = forms.IntegerField(
        required=False, label="Высота", validators=[MinValueValidator(1)])

    def clean(self):
        '''Валидация формы для проверки, что хотя бы одно поле заполнено'''
        cleaned_data = self.cleaned_data
        width = cleaned_data.get("width")
        height = cleaned_data.get("height")

        if not width and not height:
            raise ValidationError("Заполните хотя бы одно поле")

        return cleaned_data
