from django import template

register = template.Library()

@register.filter
def getMessage(messages, field = 'message'):
    for msg in messages:
        if field == 'message':
            return msg.message
        elif field == 'icon':
            return msg.extra_tags