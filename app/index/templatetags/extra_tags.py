from django import template
from django.http import HttpRequest

register = template.Library()


@register.simple_tag
def active(request: HttpRequest, name: str) -> str:
    if request.resolver_match.url_name == name:
        return 'active'
    return ''
