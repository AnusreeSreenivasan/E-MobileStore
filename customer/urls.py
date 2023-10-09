from django.urls import path
from .views import *

urlpatterns=[
    path("custhome",CustHome.as_view(),name="chome"),
    path("cart",CartView.as_view(),name="cart"),
    path("checkout",CheckView.as_view(),name="c_out"),
    path("order",OrderPro.as_view(),name="order"),
    path("addcart/<int:pid>",AddCart.as_view(),name="addcart")
]