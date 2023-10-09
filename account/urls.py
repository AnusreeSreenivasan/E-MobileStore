from django.urls import path
from .views import RegView,LogView

urlpatterns=[
    path('log/',LogView.as_view(),name="log"),
    path('reg/',RegView.as_view(),name="reg"),
   

]