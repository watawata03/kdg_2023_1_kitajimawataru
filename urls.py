from django.urls import path

from . import views

urlpatterns = [
    #トップページ
    path('rebels/', views.ListRebelsView.as_view(),name='index'),
    path('company/', views.ListCompanyView.as_view(),name='company'),
    path('service/', views.ListServiceView.as_view(),name='service'),
    path('faq/', views.ListFaqView.as_view(),name='faq'),
    path('contact/', views.ListContactView.as_view(),name='contact'),
    path('service1/', views.ListService1View.as_view(),name='service1'),
    path('service2/', views.ListService2View.as_view(),name='service2'),
    path('service3/', views.ListService3View.as_view(),name='service3'),
    path('service4/', views.ListService4View.as_view(),name='service4'),
    path('service5/', views.ListService5View.as_view(),name='service5'),
    path('service6/', views.ListService6View.as_view(),name='service6'),
    path('/accounts/login', views.ListLoginView.as_view(),name='login'),
]