from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('accounts/', views.AccountList.as_view(), name='account_list'),
    path('accounts/<int:pk>', views.AccountDetail.as_view(), name='account_detail'),
    path('institutions/', views.InstitutionList.as_view(), name='institution_list'),
    path('institutions/<int:pk>', views.InstitutionDetail.as_view(), name='institution_detail'),
    path('transactions/', views.TransactionList.as_view(), name='transaction_list'),
    path('transactions/<int:pk>', views.TransactionDetail.as_view(), name='transaction_detail'),
]
