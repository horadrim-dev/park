from django.contrib import admin
from .models import *
from .forms import PostForm

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # поле alias будет автоматически заполнено на основе заголовка
    # prepopulated_fields = {
    #     "alias" : ("title",)
    # 
    form = PostForm
