from rest_framework import serializers
from library_app.models import Member, Book, Issuance


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class IssuanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issuance
        fields = '__all__'
