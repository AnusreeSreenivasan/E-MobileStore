from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,FormView,View
from .models import CustUser
from .forms import RegForm,LogForm
from django.contrib.auth import authenticate,login
# Create your views here.

class Home(View):
    def get(self,req):
        return render(req,'home.html')

class LogView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        form_data=self.form_class(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            ps=form_data.cleaned_data.get("password")
            user=authenticate(request,username=un,password=ps)
            if user:
                if user.usertype=="Customer":
                    login(request,user)
                    return redirect("chome")
                elif user.usertype=="Store":
                    login(request,user)
                    return redirect("shome")
            else:
                return redirect("log")


class RegView(CreateView):
    model=CustUser
    template_name="reg.html"
    form_class=RegForm
    success_url=reverse_lazy("log")
