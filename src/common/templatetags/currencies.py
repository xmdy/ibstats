from django.contrib.humanize.templatetags.humanize import intcomma
from django import template

register = template.Library()


@register.filter
def currency(val):
    val = round(float(val), 2)
    if val > 0:
        return "$%s%s" % (int(val), ("%0.2f" % val)[-3:])
    else:
        val = abs(val)
        return "-$%s%s" % (int(val), ("%0.2f" % val)[-3:])