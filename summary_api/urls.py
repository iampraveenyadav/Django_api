from django.urls import path
from . import views 
 
urlpatterns = [ 
    path('summary_api', views.dbase_name),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #url(r'^api/tutorials/published$', views.tutorial_list_published)
]