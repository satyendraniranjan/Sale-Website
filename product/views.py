from django.shortcuts import render
from .models import Product , ProductImages , Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404


def productlist(request , category_slug=None):
    category = None
    productlist = Product.objects.all()

    template = 'Product/product_list.html'
    context = {'product_list': productlist}
    return render(request, template, context)


def productdetail(request, product_slug):
    productdetail= Product.objects.get(slug=product_slug)

    template = 'Product/product_detail.html'
    context = {'product_detail': productdetail}
    return render(request, template, context)


