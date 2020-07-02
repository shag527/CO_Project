from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('doc',views.ViewDoc,name="doc"),
    path('doc1',views.ViewDoc1,name="doc1"),
    path('doc2',views.ViewDoc2,name="doc2"),
    path('doc3',views.ViewDoc3,name="doc3"),
    path('projreport',views.ProjectReport,name="projreport"),
    path('working',views.Working,name="working"),
]