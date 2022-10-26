from django.contrib import admin
from .models import *
from .forms import AttractionForm
from cms.admin.placeholderadmin import PlaceholderAdminMixin

class PhotoAttractionInline(admin.TabularInline):
    model = Photo

@admin.register(Attraction)
class ReviewAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    # 
    list_display = ['title', 'order']
    form = AttractionForm
    inlines = (PhotoAttractionInline, )
