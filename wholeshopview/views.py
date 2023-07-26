from django.shortcuts import render
from django.db.models import Q
from . models import Type, Product, Category

# views


# view function for display 'type'of products
def home(request):
    latest_products = Product.objects.all().order_by(
        '-id')[:3]  # queryset for 3 latest added products
    category = Category.objects.all()  # query set for all the category
    type = Type.objects.all()  # qyuery set for all the type

    type_men = Type.objects.get(name="Men")  # object for category men
    type_women = Type.objects.get(name="Women")  # object for category women
    products_men = Product.objects.all().filter(
        type=type_men).order_by("-id")[:3]# query set for latest 3 men products
    products_women = Product.objects.all().filter(
        type=type_women).order_by("-id")[:3]# query set for latest 3 women products

    context = {
        'type': type,
        'category': category,
        'latest_products': latest_products,

        'type_men': type_men,
        'type_women': type_women,
        'products_men': products_men,
        'products_women': products_women
    }
    return render(request, 'wholeshopview/home.html', context)


def typeProductsView(request, slug):
    type = Type.objects.get(slug=slug)
    products_by_type = Product.objects.all().filter(type=type)
    context = {
        'products_by_type': products_by_type,
        'type': type
    }
    return render(request, 'wholeshopview/type_products_view.html', context)


def singleProductView(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'wholeshopview/single_product_view.html', context)


def allProductsView(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'wholeshopview/all_products_view.html', context)


def categoryProductView(request, slug):
    category = Category.objects.get(slug=slug)
    products_by_category = Product.objects.all().filter(category=category)
    context = {
        'products_by_category': products_by_category,
        'category_name': category

    }
    return render(request, 'wholeshopview/category_products_view.html', context)
