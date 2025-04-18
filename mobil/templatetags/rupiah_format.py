from django import template

register = template.Library()

@register.filter(name='rupiah')
def rupiah_format(value):
    if value:
        return f"Rp {value:,.0f}".replace(',', '.')
    return ''