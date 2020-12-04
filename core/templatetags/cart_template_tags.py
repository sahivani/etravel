from django import template
from core.models import Order, Wishlist, Item, Comment
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0

@register.filter
def wishlist_item_count(user):
    if user.is_authenticated:
        qs = Wishlist.objects.filter(user=user)
        if qs.exists():
            return qs.count()
    return 0

@register.filter
def wishlist_product_count(slug):

    qs = Wishlist.objects.filter(item__slug=slug)
    if qs.count()>1:
        return "{} People(s) have this item is in their wishlist".format(qs.count()-1 )
    return "No one have this item is in their wishlist"

@register.filter
def review_count(slug):
    qs = Comment.objects.filter(product__slug=slug)
    if qs.exists():
        return qs.count()
    return "No "

@register.filter
def review_avg(slug):
    qs = Comment.objects.filter(product__slug=slug)
    if qs.exists():
        avg = qs.aggregate(Avg('rate'))
        return avg['rate__avg']
    return 0

@register.filter
def disable_count(user, slug):
    qs = Comment.objects.filter(user=user,product__slug=slug)
    if qs.exists():
        return 1
    return 0