from django.shortcuts import render

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Initialize the form variable
    form = AddToCartForm()
    if request.method == 'POST':
        if 'add_to_cart' in request.POST:
            form = AddToCartForm(request.POST)
            if form.is_valid():
                quantity = form.cleaned_data['quantity']
                if item_created:
                    cart_item.quantity = quantity
                else:
                    cart_item.quantity += quantity
                cart_item.save()
                messages.success(request, 'Product added to cart successfully.')
                return redirect('product_detail', pk=product_id)
        elif 'remove_from_cart' in request.POST:
            cart_item.delete()
            messages.success(request, 'Product removed from cart successfully.')
            return redirect('product_detail', pk=product_id)
    else:
        form = AddToCartForm()

    context = {
        'form': form,
        'product': product,
        'cart_count': get_cart_count(request.user),
        'cart_item': cart_item if not item_created else None  # Include cart_item if it already exists in the cart
    }

    return render(request, 'myapp/add_to_cart.html', context)



@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    # Calculate total price
    total_price = 0
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
        total_price += item.total_price
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        cart_item = get_object_or_404(CartItem, id=cart_item_id)

        if 'add_quantity' in request.POST:
            cart_item.quantity += 1
            cart_item.save()
        elif 'remove_quantity' in request.POST:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

        # Recalculate total price after updates
        total_price = 0
        for item in cart_items:
            item.total_price = item.product.price * item.quantity
            total_price += item.total_price
    context = {
        'cart_items': cart_items,
        'cart_count': get_cart_count(request.user),
        'total_price': total_price
    }
    return render(request, 'myapp/view_cart.html', context)


@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        messages.error(request, 'Your cart is empty. Please add items to your cart before checking out.')
        return redirect('view_cart')

    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)
            order = Order.objects.create(user=request.user)

            try:
                charge = stripe.Charge.create(
                    amount=int(cart.total_price() * 100),  # Amount in cents
                    currency='cad',
                    description='Example charge',
                    source=token,
                )

                for item in cart_items:
                    product = item.product
                    if product.stock >= item.quantity:
                        product.stock -= item.quantity
                        product.save()
                        OrderItem.objects.create(order=order, product=product, quantity=item.quantity)
                    else:
                        messages.error(request, f'Not enough stock for {product.name}')
                        return redirect('view_cart')

                cart_items.delete()
                # Render the email message using the template
                subject = 'Order Confirmation'
                html_message = render_to_string('emails/order_confirmation_email.html', {
                    'user': request.user,
                    'order_details': order,
                })
                plain_message = 'Your order has been placed successfully.'

                # Use EmailMultiAlternatives to send the email
                email = EmailMultiAlternatives(subject, plain_message, 'your_email@gmail.com', [request.user.email])
                email.attach_alternative(html_message, "text/html")
                email.send()
                messages.success(request, 'Order placed successfully.')
                return redirect('order_confirmation')
            except stripe.error.StripeError as e:
                messages.error(request, f"Payment error: {str(e)}")
                return redirect('checkout')
    else:
        form = CheckoutForm()

    return render(request, 'myapp/checkout.html', {
        'form': form,
        'cart_count': get_cart_count(request.user),
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'cart_items': cart_items,
        'total_price': cart.total_price(),
    })
