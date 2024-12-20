from django import template

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return fr'/media/{val}'
    return '/static/dummydog.jpg'


@register.filter()
def user_media(val):
    if val:
        return f'/media/{val}'
    return '/static/noavatar.png'
