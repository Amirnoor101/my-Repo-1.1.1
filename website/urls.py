from django.urls import path
from website.views import index_views , about_views , contact_views


urlpatterns = [
    path ("",index_views),
    path ("about",about_views),
    path ("contact",contact_views),    
]