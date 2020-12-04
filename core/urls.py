from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    add_to_wishlist,
    remove_from_wishlist,
    WishlistView,
    order_history, addcomment, move_to_wishlist, HomeView_Search, HomeView_Category, search_auto, edituser,
    remove_address, editaddress
)

app_name = 'core'




urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView, name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('add-to-wishlist/<slug>/', add_to_wishlist, name='add-to-wishlist'),
    path('move-to-wishlist/<slug>/', move_to_wishlist, name='move-to-wishlist'),
    path('remove-from-wishlist/<slug>/', remove_from_wishlist, name='remove-from-wishlist'),
    path('wishlist-summary/', WishlistView.as_view(), name='wishlist-summary'),
    path('order-history/', order_history.as_view(), name='order-history'),
    path('addcomment/<int:id>', addcomment, name='addcomment'),
    path('search/', HomeView_Search, name='HomeView-Search'),
    path('search_auto/', search_auto, name='search_auto'),
    path('search/<str:category>/<str:gender>', HomeView_Category, name='HomeView-category'),
    path('edituser/', edituser, name='edituser'),
    path('editaddress/<id>', editaddress, name='editaddress'),
    path('remove-address/<id>/', remove_address, name='remove-address')
]
