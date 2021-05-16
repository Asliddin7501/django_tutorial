from django import template
register = template.Library()

@register.filter
def from_dict(value, index):
    return value[index]