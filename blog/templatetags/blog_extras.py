from django import template
from django.utils import timezone

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if context['user'] == user:
        return 'you'
    return user.username


@register.filter
def get_posted_at_display(time):
    interval = (timezone.now() - time).total_seconds()
    if interval <= HOUR:
        return f'Posted {int(interval // MINUTE)} minutes ago.'
    elif interval <= DAY:
        return f'Posted {int(interval // HOUR)} hours ago.'
    else:
        return f'Posted at {time.strftime("%H:%M %d %b %y")}'
