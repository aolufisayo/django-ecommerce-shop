from django.http import request
from cart.models import Cart, CartItem
from cart.views import _get_cart_id


def cart_counter(request):
    cart_total = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_get_cart_id(request))
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_total += cart_item.quantity
        except Cart.DoesNotExist or CartItem.DoesNotExist:
            cart_total = 0

    return dict(cart_total=cart_total)
