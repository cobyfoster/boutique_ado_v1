from django.shortcuts import render, redirect, reverse
from django.contrib import messages
# Create your views here.

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "There's nothing in your bag at the moemnt.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IDUO8HbTIrT6qJdbIm7a8EoeDQOyh8IooKD8OKj0mKQb7ALmLr6BFyFKaAOKeehAX4RJtNJAZZM8wb4uOQYZOtr00AoW0fqDS',
        'slient_secret': 'test client secret'
    }

    return render(request, template, context)