from django import template

register = template.Library()

@register.filter
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter
def addplaceholder(value, arg):
    return value.as_widget(attrs={'placeholder': arg})
