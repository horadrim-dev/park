from django.contrib import admin
from .models import Review
from .forms import ReviewForm
from cms.admin.placeholderadmin import PlaceholderAdminMixin

@admin.register(Review)
class ReviewAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    # 
    form = ReviewForm