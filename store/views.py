from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,View,UpdateView,DeleteView
from .forms import ProductForm
from django.contrib import messages
from customer.models import Product

# Create your views here.



# class StoreHome(TemplateView):
#     template_name="shome.html"

class StoreHome(CreateView):
    form_class = ProductForm
    model=Product
    template_name="shome.html"
    success_url=reverse_lazy("storehome")
def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
           messages.success(request,"product added!!!")
           return redirect('product')
  

class ViewPro(View):
    def get(self,req):
        data=Product.objects.all()
        return render(req,"sview.html",{"data":data}) 
    
class ProDelete(DeleteView):
    model=Product
    success_url=reverse_lazy("viewpro")
    template_name="delpro.html"
    # def form_valid(self,form):
    #     messages.success(self.request,"Product Deleted")
    #     self.object=form.save()
    #     return super().form_valid(form) 
        
    
class EditPro(UpdateView):
    form_class=ProductForm
    model=Product
    success_url=reverse_lazy("viewpro")
    template_name="editpro.html"
    pk_url_kwargs="pk"
    def form_valid(self,form):
        messages.success(self.request,"Product Updated")
        self.object=form.save()
        return super().form_valid(form)    

def post(self,req,*args,**kwargs):
    d_id=kwargs.get('id')
    dept=Product.objects.get(id=d_id)
    form_data=ProductForm(req.POST,instance=dept)
    if form_data.is_valid():
        form_data.save()
        return redirect('viewpro')
    else:
        messages.error(req,"failed")
        return redirect('editpro')
