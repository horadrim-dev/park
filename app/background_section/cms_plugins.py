from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from .models import BackgroundSection

@plugin_pool.register_plugin
class BackgroundSectionPlugin(CMSPluginBase):
    model = BackgroundSection
    render_template = 'background_section.html'
    name = "Секция с фоном"   
    allow_children = True

    fieldsets = (
        (None, {
            'fields': [
                'title',
                'text',
                'text_bottom',
                'background_image',
                'background_color',
                'css_classes',
                'use_parallax',
            ]
        }),
        ('Настройки оверлея', {
            'fields': [
                ('use_overlay',
                'overlay_color',
                'overlay_opacity'),
            ]
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({
            'id': instance.generate_id(),
            'instance': instance,
            'background_image':instance.background_image,
            'background_color':instance.background_color,
        })
        return context

