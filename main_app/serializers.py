from dataclasses import fields
from rest_framework import serializers
from .models import Account, Institution, Transaction, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail'
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'user_url')



class AccountSerializer(serializers.HyperlinkedModelSerializer):
    institution = serializers.HyperlinkedRelatedField(
        view_name='institution_detail',
        read_only=True
    )

    user = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        read_only=True
    )

    account_url = serializers.ModelSerializer.serializer_url_field(
        view_name='account_detail'
    )

    class Meta:
        model = Account
        fields = ('account_identification', 'balance_available', 'balance_current', 'name', 'account_type', 'account_subtype', 'institution', 'user', 'account_url')



class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        read_only=True
    )

    institution_url = serializers.ModelSerializer.serializer_url_field(
        view_name='institution_detail'
    )

    class Meta:
        model = Institution
        fields = ('institution_identification', 'name', 'logo', 'user', 'institution_url')



class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    debited_account = serializers.HyperlinkedRelatedField(
        view_name = 'account_detail',
        read_only = True
    )
    
    credited_account = serializers.HyperlinkedRelatedField(
        view_name = 'account_detail',
        read_only = True
    )

    user = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        read_only=True
    )

    transaction_url = serializers.ModelSerializer.serializer_url_field(
        view_name='transaction_detail'
    )

    class Meta:
        model = Transaction
        fields = ('transaction_identification', 'amount', 'description', 'category', 'sub_category', 'sub_sub_category', 'debited_account', 'credited_account', 'transaction_date', 'created_at', 'user', 'transaction_url')


