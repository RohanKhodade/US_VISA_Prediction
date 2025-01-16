from django.urls import path
from . import views

urlpatterns=[
    path("",views.predict,name="get_predict"),
    path("result/",views.predicted,name="result"),
    
]