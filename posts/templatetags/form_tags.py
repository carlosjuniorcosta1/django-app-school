from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='add_attrs')
def add_attrs(field, args):
    attrs = {}
    for arg in args.split(','):
        key, value = arg.split('=')
        attrs[key] = value
    return field.as_widget(attrs=attrs)

@register.filter
def to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return value 