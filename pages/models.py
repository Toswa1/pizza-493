from django.db import models

class ScrollModel(models.Model):
    image = models.ImageField(upload_to="scroolls")
    dicount = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __def__(self):
        return self.title
    
    class Meta:
        verbose_name = "scroll"
        verbose_name_plural = "scrolls"

class GalleryModel(models.Model):
    image = models.ImageField(upload_to="gallery")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = "gallery"
        verbose_name_plural = "galleries"


# Create your models here.
