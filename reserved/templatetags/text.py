from django import template
from reserved.models import SiteText
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.simple_tag
def db_text(name, default=None):
    try:
        p = SiteText.objects.get(name=name).value
    except ObjectDoesNotExist as e:
        p = name if default is None else default

    return str(p)
