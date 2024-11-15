from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from library_app.models import Member, Book, Issuance
from rest_framework import viewsets
from library_app.serializers import MemberSerializer, BookSerializer, IssuanceSerializer
from django.http import HttpResponse
from library_app.models import *
from library_app.serializers import MemberSerializer


# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class IssuanceViewSet(viewsets.ModelViewSet):
    queryset = Issuance.objects.all()
    serializer_class = IssuanceSerializer


def pending_returns_dashboard(request):
    outstanding_books = Issuance.objects.filter(issuance_status='outstanding')
    records = [
        {
            'member_name': issuance.issuance_member.mem_name,
            'book_name': issuance.book.book_name,
            'issued_date': issuance.issuance_date,
            'target_return_date': issuance.target_return_date,
            'author': issuance.book.book_publisher
        }
        for issuance in outstanding_books
    ]
    return render(request, 'dashboard.html', {'records': records})
