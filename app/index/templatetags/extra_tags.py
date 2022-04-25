from django import template
from django.http import HttpRequest

register = template.Library()


@register.simple_tag
def active(request: HttpRequest, name: str) -> str:
    if request.resolver_match.url_name == name:
        return 'active'
    return ''


@register.simple_tag
def make_hash(input: str, obj_name: str) -> str:
    import hashlib

    hex_out = hashlib.sha256(bytes(f"{input}{obj_name}", "utf-8"))
    return hex_out.hexdigest()
