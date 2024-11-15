from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library_app.views import MemberViewSet, BookViewSet, IssuanceViewSet, pending_returns_dashboard
from django.contrib import admin
from library_app import views
from .custom_views import books_never_borrowed, outstanding_books, top_borrowed_books, top_member

router = DefaultRouter()
router.register(r'member', MemberViewSet)
router.register(r'book', BookViewSet)
router.register(r'issuance', IssuanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', pending_returns_dashboard, name='pending_returns_dashboard'),
    path('api/books/never-borrowed/', books_never_borrowed, name='books_never_borrowed'),
    path('api/books/outstanding/', outstanding_books, name='outstanding_books'),
    path('api/books/top-borrowed/', top_borrowed_books, name='top_borrowed_books'),
    path('api/member/top/', top_member, name='top_member'),
]
