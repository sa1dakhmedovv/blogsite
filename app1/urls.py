from django.urls import path
from .views import post_detail,post_list

urlpatterns = [
    path('', post_list, name='post-list'),
    path('post/<slug:slug>/', post_detail, name='post-detail'),
    # path('post/<slug:slug>/share/', post_share, name='post-share')
]