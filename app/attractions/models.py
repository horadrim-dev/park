from email.policy import default
from django.db import models
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from django.urls import reverse
from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PlaceholderField
import uuid

class Attraction(models.Model):
    title = models.CharField("Название", max_length=255, default="")

    price_card = models.PositiveIntegerField('Цена билета по карте', default=0)
    price_nocard = models.PositiveIntegerField('Цена билета без карты', default=0)
    short_description = models.CharField("Короткое описание", max_length=1024, default="")
    description = HTMLField("Описание", default="", blank=True, null=True)
    placeholder_top = PlaceholderField('top')
    placeholder_bottom = PlaceholderField('bottom', related_name="placeholder_bottom")

    main_photo = FilerImageField(
        verbose_name='Главное фото',
        on_delete=models.CASCADE, 
    )


    def get_photos(self):
        return self.photo_set.all()

    @property
    def gen_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

    def get_absolute_url(self):
        return reverse("attractions:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'аттракцион'
        verbose_name_plural = 'аттракционы'

class Photo(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    image = FilerImageField(
        verbose_name='Фото',
        on_delete=models.CASCADE, 
    )

class AttractionsPlugin(CMSPlugin):

    num_objects = models.PositiveIntegerField("Количество аттракционов", default=4)

    def get_attractions(self, limit):
        return Attraction.objects.all()[:limit]

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]