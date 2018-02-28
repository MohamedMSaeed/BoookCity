from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Author, Category, Rates
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.views import generic
from bookcity.forms import RegistrationForm, Edit, changePassword
from django.db.models import Avg, Count
from django.views.decorators.cache import never_cache



def home(request):
    allBooks = Book.objects.all()
    followedAuthors = Author.objects.filter(followAuthor=request.user.id)
    followedAuthorsBooks = Book.objects.filter(author__aid__in=followedAuthors).order_by('-published_date')[:5]
    wishListBooks = Book.objects.filter(wishListBoos=request.user.id)
    likeCategories = Category.objects.filter(likeCategory=request.user.id)
    likeCategoriesBooks = Category.objects.values('bookCategory','cid')
    topRateBooks = Rates.objects.values('bid__name','bid').annotate(rateIt=Avg('rate'), count=Count('rate')).order_by('-rateIt')[:5]
    topFollowedAuthors = Author.objects.values('name','aid').annotate(count=Count('followAuthor')).order_by('-count')[:5]
    all_category_list = Category.objects.all()
    context = {'all_category_list': all_category_list,
               'followedAuthors': followedAuthors,
               'wishListBooks': wishListBooks,
               'likeCategories': likeCategories,
               'topRateBooks': topRateBooks,
               'topFollowedAuthors': topFollowedAuthors,
               'followedAuthorsBooks': followedAuthorsBooks,
               'allBooks': allBooks,
              'likeCategoriesBooks': likeCategoriesBooks,
               }
    return render(request, 'bookcity/home.html', context)


def book(request):
    book_list = Book.objects.all()
    all_category_list = Category.objects.all()
    context = {'book_list': book_list,
               'all_category_list': all_category_list}
    return render(request, 'bookcity/books.html', context)


def bookDetail(request, book_id):
    selectedBook = get_object_or_404(Book, pk=book_id)
    category = selectedBook.BookCategory.all()
    readFlag = Book.objects.filter(bid=book_id, readBooks=request.user.id)
    wishListFlag = Book.objects.filter(bid=book_id, wishListBoos=request.user.id)
    try:
        rateobj = Rates.objects.get(uid_id=request.user.id, bid_id=book_id)
        rateVal = rateobj.rate
    except Exception as e:
        rateVal = 0
    all_category_list = Category.objects.all()
    context = {'book': selectedBook,
               'category_list': category,
               'all_category_list': all_category_list,
               'readFlag': readFlag,
               'wishListFlag': wishListFlag,
               'rateing': rateVal,
               }
    return render(request, 'bookcity/bookDetail.html', context)


def rate(request, book_id, rateVal):
    try:
        r = Rates.objects.get(bid_id = book_id, uid_id = request.user.id)
        r.rate = rateVal
        r.save()
    except Exception as e:
        Rates.objects.create(rate = rateVal, bid_id = book_id, uid_id = request.user.id)
    return redirect('/bookcity/books/'+str(book_id))


def author(request):
    author_list = Author.objects.all()
    all_category_list = Category.objects.all()
    context = {'author_list': author_list,
               'all_category_list': all_category_list,
               }
    return render(request, 'bookcity/authors.html', context)


def authorDetail(request, author_id):
    selectedAuthor = get_object_or_404(Author, pk=author_id)
    authorBooks = Book.objects.filter(author = author_id)
    followFlag = Author.objects.filter(aid=author_id,followAuthor=request.user.id)
    all_category_list = Category.objects.all()
    context = {'author': selectedAuthor,
               'books': authorBooks,
               'followFlag': followFlag,
               'all_category_list': all_category_list,
               }
    return render(request, 'bookcity/authorDetail.html', context)


def category(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'bookcity/base.html', context)


def categoryDetail(request, category_id):
    selectedCategory = get_object_or_404(Category, pk=category_id)
    categoryBooks = selectedCategory.bookCategory.all()
    categoryFlag = Category.objects.filter(cid=category_id, likeCategory=request.user.id)
    all_category_list = Category.objects.all()
    context = {'category': selectedCategory,
               'books': categoryBooks,
               'all_category_list': all_category_list,
               'followFlag': categoryFlag,
               }
    return render(request, 'bookcity/categoryDetail.html', context)




def follow(request, author_id):
    curr_user = request.user
    author = Author.objects.get(pk=author_id)
    author.followAuthor.add(curr_user)
    author.save()
    return redirect('/bookcity/authors/'+str(author_id))


def unfollow(request, author_id):
    curr_user = request.user
    author = Author.objects.get(pk=author_id)
    author.followAuthor.remove(curr_user)
    author.save()
    return redirect('/bookcity/authors/' + str(author_id))


def read(request, book_id):
    curr_user = request.user
    book = Book.objects.get(pk=book_id)
    book.readBooks.add(curr_user)
    book.wishListBoos.remove(curr_user)
    book.save()
    return redirect('/bookcity/books/'+str(book_id))


def unread(request, book_id):
    curr_user = request.user
    book = Book.objects.get(pk=book_id)
    book.readBooks.remove(curr_user)
    book.save()
    return redirect('/bookcity/books/' + str(book_id))


def wishList(request, book_id):
    curr_user = request.user
    book = Book.objects.get(pk=book_id)
    book.wishListBoos.add(curr_user)
    book.save()
    return redirect('/bookcity/books/' + str(book_id))


def unWish(request, book_id):
    curr_user = request.user
    book = Book.objects.get(pk=book_id)
    book.wishListBoos.remove(curr_user)
    book.save()
    return redirect('/bookcity/books/' + str(book_id))

def followCate(request, category_id):
    curr_user = request.user
    category = Category.objects.get(pk=category_id)
    category.likeCategory.add(curr_user)
    category.save()
    return redirect('/bookcity/categories/'+str(category_id))


def unfollowCate(request, category_id):
    curr_user = request.user
    category = Category.objects.get(pk=category_id)
    category.likeCategory.remove(curr_user)
    category.save()
    return redirect('/bookcity/categories/' + str(category_id))

@never_cache
def profile(request):
    all_category_list = Category.objects.all()
    if request.user.is_authenticated :
        user = request.user
        context = {'all_category_list': all_category_list,
                   'user': user,
                   }
        return render(request, 'bookcity/profile.html', context)
    else:
        return redirect('/bookcity/')


class signup(generic.CreateView):
    template_name = 'bookcity/signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


@never_cache
def edit(request):
    all_category_list = Category.objects.all()
    if request.user.is_authenticated :
        if request.method == 'POST':
            form = Edit(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                return redirect('/bookcity/profile')

        else:
            form = Edit(instance=request.user)
            context = {'form': form,
                    'all_category_list': all_category_list,
                       }
            return render(request, 'bookcity/edit.html', context)
    else:
        return redirect('/bookcity/')

@never_cache
def changePassword(request):
    all_category_list = Category.objects.all()
    if request.user.is_authenticated :
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('/bookcity/profile')
            else:
                return redirect('/bookcity/profile/password')

        else:
            form = PasswordChangeForm(user=request.user)
            context = {'form': form,
                        'all_category_list': all_category_list,
                       }
            return render(request, 'bookcity/changePassword.html', context)
    else:
        return redirect('/bookcity/')


def search(request, searchWord):
    all_category_list = Category.objects.all()
    author = Author.objects.filter(name__icontains=searchWord)
    book = Book.objects.filter(name__icontains=searchWord)
    category = Category.objects.filter(name__icontains=searchWord)
    context = {'all_category_list': all_category_list,
               'author':author,
               'book':book,
               'category':category,
               }
    return render(request, 'bookcity/search.html', context)

