from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.template import Template
from .models import  PureCodePlugin


@plugin_pool.register_plugin
class PureCodePluginPublisher(CMSPluginBase):
    module = "Общий"
    name = "Код"
    model = PureCodePlugin
    allow_children = False
    render_template = "core/plugins/purecode.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context['code'] = instance.code
        context['css'] = instance.css
        context['js'] = instance.js
        return context