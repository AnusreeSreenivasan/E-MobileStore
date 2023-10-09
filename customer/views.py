from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
from .models import *
from django.contrib import messages
from .forms import Cartform,OrderForm
# Create your views here.

class CustHome(TemplateView):
    template_name="chome.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['products']=Product.objects.all()
        return context

class CartView(TemplateView):
    template_name="cart.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['cartitems']=CartItem.objects.filter(user=self.request.user)
        return context

class OrderPro(CreateView):
    model=Order
    form_class=OrderForm
    template_name='order.html'
    success_url=reverse_lazy('products')

class AddCart(CreateView):
    template_name="addcart.html"
    form_class=Cartform
    model=CartItem
    success_url=reverse_lazy("cart")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['pro']=Product.objects.get(id=self.kwargs.get("pid"))
        return context
    def form_valid(self, form):
        form.instance.user=self.request.user
        form.instance.product=Product.objects.get(id=self.kwargs.get("pid"))
        self.object=form.save()
        return super().form_valid(form)



class CheckView(TemplateView):
    template_name="checkout.html"
