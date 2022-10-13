from django.contrib import admin
from .models import *
from .forms import AttractionForm

class PhotoAttractionInline(admin.TabularInline):
    model = Photo

@admin.register(Attraction)
class ReviewAdmin(admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    # 
    form = AttractionForm
    inlines = (PhotoAttractionInline, )
