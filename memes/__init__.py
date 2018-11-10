from django import template

register = template.Library()

@register.filter
def clear(value):
    return value.replace("memes2k18","")