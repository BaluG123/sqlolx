from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-uploaded',)

class Item(models.Model):
    CONDITION_CHOICES=(('good condition','Good Condition'),('very good condition','Very Good Conditon'))
    name=models.CharField(max_length=18)
    place=models.CharField(max_length=18)
    item=models.CharField(max_length=18)
    item_name=models.SlugField(max_length=256)
    item_image=models.ImageField(null=True,blank=True,upload_to='images/')
    about_item=models.CharField(max_length=18)
    price=models.PositiveIntegerField()
    description=models.TextField()
    uploaded=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    condition=models.CharField(max_length=20,choices=CONDITION_CHOICES,default="good condition")
    tags=TaggableManager()
    objects=CustomManager()

    class Meta:
        ordering=['-uploaded']

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('item_detail',args=[self.uploaded.year,self.uploaded.strftime('%m'),self.uploaded.strftime('%d'),self.item_name])
