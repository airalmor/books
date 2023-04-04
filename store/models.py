from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                              related_name='my_books')
    readers = models.ManyToManyField(User, through='UserBookRelation', related_name='books')

    def __str__(self):
        return f'ID:{self.id} Название: {self.name} Цена: {self.price}-Автор :{self.author_name}'


class UserBookRelation(models.Model):
    RATE_CHOISES = (
        (1, 'OK'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amaizing'),
        (5, 'Incredible'),

    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.SmallIntegerField(choices=RATE_CHOISES,null=True)

    def __str__(self):
        return f'{self.user.username} : {self.book.name} : Оценка {self.rate}'