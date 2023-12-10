
import pytest
from main import BooksCollector
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name', ['This is a book with more than 41 symbol that more the maximum length allowed',
                                      'This string has 41 characters in it......'])
    def test_add_new_book_add_book_longer_name_than_allowed(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_set_book_genre_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Фантастика")
        assert collector.books_genre["Книга"] == "Фантастика"

    def test_get_book_genre_get_genre_of_one_book(self):
        collector = BooksCollector()
        collector.books_genre = {"Book1": "Фантастика", "Book2": "Ужасы", "Book3": "Ужасы", "Book4": "Мультфильмы",
                                 "Book5": "Комедии"}
        genre1 = collector.get_book_genre('Book1')
        assert genre1 == 'Фантастика'

    def test_get_books_with_specific_genre_get_horror_books(self):
        collector = BooksCollector()
        collector.books_genre = {"Book1": "Фантастика", "Book2": "Ужасы", "Book3": "Ужасы", "Book4": "Мультфильмы",
                                 "Book5": "Комедии"}
        assert collector.get_books_with_specific_genre("Ужасы") == ["Book2", "Book3"]

    def test_get_books_genre_positive_result(self):
        collector = BooksCollector()
        collector.books_genre = {"Book1": "Фантастика", "Book2": "Ужасы", "Book3": "Ужасы", "Book4": "Мультфильмы",
                                 "Book5": "Комедии"}
        assert len(collector.get_books_genre()) == 5

    def test_get_books_for_children_positive_result(self):
        collector = BooksCollector()
        collector.books_genre = {"Book1": "Фантастика", "Book2": "Ужасы", "Book3": "Ужасы", "Book4": "Мультфильмы",
                                 "Book5": "Комедии"}
        assert len(collector.get_books_for_children()) == 3

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book("NewBook")
        collector.add_book_in_favorites("NewBook")
        assert collector.favorites[0] == "NewBook"

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.favorites = ["Book1", "Book2", "Book3", "Book4", "Book5"]
        collector.delete_book_from_favorites("Book2")
        assert len(collector.favorites) == 4

    def test_get_list_of_favorites_books_positive_result(self):
        collector = BooksCollector()
        collector.favorites = ["Book1", "Book2", "Book3", "Book4", "Book5"]
        assert len(collector.favorites) == 5