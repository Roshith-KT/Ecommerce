from django.shortcuts import render
from wholeshopview.models import Product

def search_products(request):
    context = {'searched_term': None, 'products': None, 'searched_word': None}  # Initialize the context dictionary
    if request.method == 'POST':
        searched_term = request.POST['search']
        searched_word = searched_term
        if contains_only_whitespaces(searched_term):
            searched_term = False
        else:
            products = Product.objects.filter(name__contains=searched_term)
            context = {
                'searched_term': searched_term,
                'products': products,
                'searched_word': searched_word
            }
    return render(request, 'search/search_result.html', context)


# To check whether the searched contains only whitespace
def contains_only_whitespaces(input_string):
    for char in input_string:
        if not char.isspace():
            return False
    return True
