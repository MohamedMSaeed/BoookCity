from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    # /bookcity/logout
    path('logout/', auth_views.logout, name='logged_out'),
    # /bookcity/login
    url(r'^login/$', auth_views.login, name='login'),
    # ex: /bookcity/
    path('', views.home, name='index'),
    # ex: /bookcity/signup
    path('signup/', views.signup.as_view(), name='signup'),
    # ex: /bookcity/home
    path('home/', views.home, name='home'),
    # ex: /bookcity/books
    path('books/', views.book, name='books'),
    # ex: /bookcity/books/3
    path('books/<int:book_id>/', views.bookDetail, name='detail'),
    # ex: /bookcity/books/rate
    path('books/<int:book_id>/rate/<int:rateVal>', views.rate, name='rate'),
    # ex: /bookcity/authors
    path('authors/', views.author, name='authors'),
    # ex: /bookcity/authors/3
    path('authors/<int:author_id>/', views.authorDetail, name='detail'),
    # ex: /bookcity/authors/3/follow
    path('authors/<int:author_id>/follow/', views.follow, name='follow'),
    # ex: /bookcity/authors/3/unfollow
    path('authors/<int:author_id>/unfollow/', views.unfollow, name='unfollow'),
    # ex: /bookcity/categories
    path('categories/', views.category, name='categories'),
    # ex: /bookcity/authors/3
    path('categories/<int:category_id>/', views.categoryDetail, name='categoryDetail'),
    # ex: /bookcity/books/3/read
    path('books/<int:book_id>/read/', views.read, name='read'),
    # ex: /bookcity/books/3/unread
    path('books/<int:book_id>/unread/', views.unread, name='unread'),
    # ex: /bookcity/books/3/wishList
    path('books/<int:book_id>/wishList/', views.wishList, name='wishList'),
    # ex: /bookcity/books/3/unWish
    path('books/<int:book_id>/unWish/', views.unWish, name='unWish'),
    # ex: /bookcity/categories/3/follow
    path('categories/<int:category_id>/followCate/', views.followCate, name='followCate'),
    # ex: /bookcity/categories/3/unfollow
    path('categories/<int:category_id>/unfollowCate/', views.unfollowCate, name='unfollowCate'),
    # ex: /bookcity/profile
    path('profile/', views.profile, name='profile'),
    # ex: /bookcity/profile/edit
    path('profile/edit/', views.edit, name='profile_edit'),
    # ex: /bookcity/profile/password
    path('profile/password/', views.changePassword, name='changePassword'),
    # ex: /bookcity/search
    path('search/<str:searchWord>', views.search, name='search'),
]

