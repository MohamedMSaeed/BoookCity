from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    aid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=50)
    DOB = models.DateField()
    DOD = models.DateField(blank=True, null=True)
    bio = models.TextField()
    pic = models.ImageField(upload_to='static/images/')
    followAuthor = models.ManyToManyField(User, related_name="FollowAuthor")

    def __str__(self):
        return self.name


class Book(models.Model):
    bid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    desc = models.TextField()
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'static/images/')
    readBooks = models.ManyToManyField(User, related_name="ReadBook")
    wishListBoos = models.ManyToManyField(User, related_name="Wishlist")

    def __str__(self):
        return self.name


class Category(models.Model):
    cid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    bookCategory = models.ManyToManyField(Book, related_name="BookCategory")
    likeCategory = models.ManyToManyField(User, related_name="UserCategory")

    def __str__(self):
        return self.name


class Rates(models.Model):
    rate = models.IntegerField()
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.ForeignKey(Book, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.uid," rated ",self.bid," with ",self.rate