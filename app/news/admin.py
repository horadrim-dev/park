from django.contrib import admin
from .models import *
from .forms import PostForm
from cms.admin.placeholderadmin import PlaceholderAdminMixin

class ImagePostInline(admin.TabularInline):
    model = ImagePost
    extra = 1

class VideoPostInline(admin.TabularInline):
    model = VideoPost
    extra = 0

@admin.register(Post)
class PostAdmin( PlaceholderAdminMixin, admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    form = PostForm
    inlines = (ImagePostInline, VideoPostInline)
