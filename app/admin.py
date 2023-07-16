from django.contrib import admin
from .models import Asanas

# Register your models here.
class AdminAsanas(admin.ModelAdmin):
    list_display=['symptoms','asana1','img1','asana2','img2','asana3','img3']
admin.site.register(Asanas)
