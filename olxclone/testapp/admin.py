from django.contrib import admin
from testapp.models import Item

class Itemadmin(admin.ModelAdmin):
    list_display=['id','name','place','item','item_name','item_image','about_item','price','description','uploaded','updated','condition']
    list_filter=('name','uploaded','place')
    prepopulated_fields={'item_name':('item',)}
    search_fields=('name','item_name','item','description')
    date_hierarchy='uploaded'

# Register your models here.
admin.site.register(Item,Itemadmin)
