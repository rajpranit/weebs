from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('article-detail/<int:pk>',views.article_detail,name='article-detail'),

    
    # path('',views.index.as_view(),name='index'),
    # path('article-detail/<int:pk>',views.article_detail.as_view(),name='article-detail'),

    path('category',views.category,name='category'),
    
    path('category/manhwa',views.manhwa,name='manhwa'),
    path('category/manhua',views.manhua,name='manhua'),


    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact'),

    # api to be used
    
]