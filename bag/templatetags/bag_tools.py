from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ to calculate the subtotal by multiplying the
    price and the quantity """
    return price * quantity
