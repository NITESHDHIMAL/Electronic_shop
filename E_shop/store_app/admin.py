from django.contrib import admin

# Register your models here.
from .models import *


class ImagesTublerinLine(admin.TabularInline):
    model = Images

class TagTublerinLine(admin.TabularInline):
    model = Tag
4
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTublerinLine,TagTublerinLine]




admin.site.register(Images)
admin.site.register(Tag)

admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)




