from django.shortcuts import render

# Create your views here.
def search_ecoproduct(request):
    products = Ecoproducts.objects.all()
    form = EcoproductsSearchForm(request.GET or None)
    results = None
    if form.is_valid():
        name = form.cleaned_data.get('name')
        category = form.cleaned_data.get('category')
        price = form.cleaned_data.get('price')
        results = Ecoproducts.objects.all()

        if name:
            results = results.filter(name__icontains=name)
        if category:
            results = results.filter(category=category)
        if price:
            results = results.filter(price__lte=price)

    return render(request, 'myapp/search_ecoproduct.html', {'form': form, 'results': results, 'products': products})
