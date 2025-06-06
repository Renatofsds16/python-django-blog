from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='index'),
    path('post/<slug:slug>/', views.PostDatailView.as_view(),name='post'),
    path('page/<slug:slug>/', views.PageDatailView.as_view(),name='page'),

    path('created_by/<int:id>/', views.CreatedByListView.as_view(),name='created_by'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(),name='category'),
    path('tag/<slug:slug>/', views.TagListView.as_view(),name='tag'),
    path('search/', views.SearchListView.as_view(),name='search'),
]