from django import template
import datetime

register = template.Library()

@register.filter(name='get_datetime_by_timestamp')
def get_datetime_by_timestamp(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp, 16)).strftime('%Y-%m-%d %H:%M:%S')



