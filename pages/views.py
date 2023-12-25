from django.shortcuts import render

from pages.models import ScrollModel, GalleryModel

def home_page_view(request):
    scrolls = ScrollModel.objects.all().order_by('-pk')[:5]
    images = GalleryModel.objects.all().order_by('-pk')
    context = {
        "scrolls": scrolls,
        "images": images
    }
    return render(request, 'index.html', context)