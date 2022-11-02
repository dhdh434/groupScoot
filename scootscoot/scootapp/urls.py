from django.urls import path
from .views import indexPageView
from .views import aboutPageView, tablePageView, resourcesPageView, customerPageView

urlpatterns = [
    path("", indexPageView, name="index"),    
    path("about/", aboutPageView, name="about"),
    path("table/", tablePageView, name="table"),
    path("resources/", resourcesPageView, name="resources"),
    path("customer/", customerPageView, name="customer"),
]             