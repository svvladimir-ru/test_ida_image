from django.urls import path

from .views import index, upload_images, miniature

urlpatterns = [
    path('', index, name='index'), # главная страница
    path('upload-image/', upload_images, name='upload'), # страница загрузки изображения
    path('image/<int:images_id>/', miniature, name='miniature'), # страница изменения размеров изображения
]
