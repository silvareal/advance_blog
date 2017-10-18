from urllib.parse import quote
from django import template

register = template.Library()

@register.filter(name="urlify")
def urlify(value):
    return quote(value)