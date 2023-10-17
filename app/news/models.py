from email.policy import default
from django.db import models
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from django.urls import reverse
from filer.fields.file import FilerFileField, File
from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PlaceholderField
import uuid
import datetime
from core.utils import slugify_rus
import locale
from django.dispatch import receiver
import os


class ContentManager(models.Manager):

    def published(self):
        return self.filter(published=True, published_at__lte=datetime.date.today())

class ImagePost(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    image = FilerImageField(verbose_name="Изображение", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"


@receiver(models.signals.post_delete, sender=ImagePost)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Удаляет файл при удалении объекта
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            # delete file from file system
            os.remove(instance.image.path)
            # delete Filer File object
            File.objects.filter(id=instance.image_id).delete()

class VideoPost(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    video_url = models.CharField("Ссылка на видео", null=True, blank=True, max_length=512,
                             help_text="Как правило содержится в атрибуте 'src'\
                                         тега 'iframe' экспортируемого видео.")

    class Meta:
        verbose_name = "видео"
        verbose_name_plural = "видео"

class Post(models.Model):
    title = models.CharField(
        default="", max_length=1000, verbose_name="Заголовок")
    alias = models.SlugField(default="", blank=True, unique=True,
                             max_length=1000, help_text="Краткое название транслитом через тире (пример: 'kratkoe-nazvanie-translitom'). Чем короче тем лучше. Для автоматического заполнения - оставьте пустым.")
    published = models.BooleanField(default=True, verbose_name='Опубликовано')
    published_at = models.DateField(default=datetime.date.today, 
                                    verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")

    text = HTMLField("Содержимое", default="", blank=True, null=True)

    # image = FilerImageField(verbose_name="Изображение", on_delete=models.CASCADE)

    # IMAGE_POSITION_CHOICES = [
    #     ('left', 'Слева'),
    #     ('stretch', 'Растянуть'),
    #     ('right', 'Справа'),
    #     ('hide', 'Скрыть'),
    # ]
    # image_position = models.CharField(max_length=64, choices=IMAGE_POSITION_CHOICES, default=IMAGE_POSITION_CHOICES[0][0],
    #     verbose_name="Расположение изображения")

    placeholder_top = PlaceholderField('top', related_name="post_top")
    placeholder_bottom = PlaceholderField('bottom', related_name="post_bottom")

    objects = ContentManager()

    @property
    def gen_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

    @property
    def cover(self):
        return self.imagepost_set.first()

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"slug": self.alias})

    def __str__(self):
        return self.title

    def save(self, lock_recursion=False, *args, **kwargs):
        # только при создании объекта, id еще не существует
        if not self.id or not self.alias:
            # заполняем алиас
            self.alias = slugify_rus(self.title)

        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-published_at']


class NewsPlugin(CMSPlugin):

    num_objects = models.PositiveIntegerField("Количество новостей", default=3)

    def get_objects(self, limit):
        return Post.objects.published()[:limit]

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]