from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('institutions/', views.InstitutionList.as_view(), name='institution_list'),
    path('institutions/new/', views.InstitutionCreate.as_view(), name='institution_create'),
    path('institutions/<int:pk>/', views.InstitutionDetail.as_view(), name='institution_detail'),
    path('institutions/<int:pk>/update', views.InstitutionUpdate.as_view(), name='institution_update'),
    path('accounts/', views.AccountList.as_view(), name='account_list'),
    path('accounts/new/', views.AccountCreate.as_view(), name='account_create'),
    path('accounts/<int:pk>/', views.AccountDetail.as_view(), name='account_detail'),
    path('accounts/<int:pk>/update', views.AccountUpdate.as_view(), name='account_update'),
    path('accounts/<int:pk>/delete', views.AccountDelete.as_view(), name='account_delete'),
    path('transactions/', views.TransactionList.as_view(), name='transaction_list'),
    path('transaction/new/', views.TransactionCreate.as_view(), name='transaction_create'),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transaction_detail'),
    path('transactions/<int:pk>/update', views.TransactionUpdate.as_view(), name='transaction_update'),
    path('transactions/<int:pk>/delete', views.TransactionDelete.as_view(), name='transaction_delete'),
]
