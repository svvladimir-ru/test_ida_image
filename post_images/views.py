import os
from django.shortcuts import render, redirect
from .models import Images
from .forms import UploadImageForm, SizeForm
from PIL import Image
from django.utils import timezone


def get_file_path(file):
    '''Добавление имени'''
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split(".")[-1]
    head = file.split(".")[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + "_" + time + "." + end_extention
    return os.path.join("{0}").format(file_name)


def index(request):
    '''Главная страница со списком изображений'''
    image_list = Images.objects.all()
    return render(request, "index.html", {"images": image_list})


def upload_images(request):
    '''Страница добавления изображения'''
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = form.save()
            # Тут задаю имя миниатюре
            name = get_file_path(images.image_file.name)
            images.miniature.save(name, images.image_file)
            return redirect("miniature", images_id=images.id)
    else:
        form = UploadImageForm()
    return render(request, "upload.html", {"form": form})


def miniature(request, images_id):
    '''Страница изменения размеров миниатюры'''
    images = Images.objects.get(id=images_id)
    if request.method == "POST":
        form = SizeForm(request.POST)
        if form.is_valid():
            width = form.cleaned_data["width"]
            height = form.cleaned_data["height"]
            old_image = images.miniature.path
            im_path = images.image_file.path
            im = Image.open(im_path)
            # Проверка на поля высоты и ширины, если пустые беру размеры из картинки.
            if width is None:
                width = im.size[0]
            if height is None:
                height = im.size[1]
            size = (int(width), int(height))
            im.thumbnail(size)
            im.save(old_image, "JPEG")
            return redirect('miniature', images_id=images.id)
    else:
        form = SizeForm(request.POST)
    return render(request, 'miniature.html', {'images': images, "form": form})
