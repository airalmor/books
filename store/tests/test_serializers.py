from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_3 = Book.objects.create(name='Test book 3', price=25, author_name='Author 1', owner=None)
        book_4 = Book.objects.create(name='Test book 4', price=55, author_name='Author 2', owner=None)

        data = BooksSerializer([book_3, book_4], many=True).data

        expected_data = [
            {
                'id': book_3.id,
                'name': 'Test book 3',
                'price': '25.00',
                'author_name': 'Author 1',
                'owner': None,
                'readers': []


            },
            {
                'id': book_4.id,
                'name': 'Test book 4',
                'price': '55.00',
                'author_name': 'Author 2',
                'owner': None,
                'readers': []

            }
        ]
        self.assertEqual(expected_data, data)


