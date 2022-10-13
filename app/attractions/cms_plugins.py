from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from .models import AttractionsPlugin

@plugin_pool.register_plugin
class AttractionPlugin(CMSPluginBase):
    model = AttractionsPlugin
    render_template = 'attractions_plugin.html'
    name = "Блок с аттракционами"   

    def render(self, context, instance, placeholder):
        context.update({
            'id': instance.generate_id(),
            'instance': instance,
            'attraction_list' : instance.get_attractions(limit=instance.num_objects),
        })
        return context

