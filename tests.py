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

    def test_add_new_book_add_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_add_book_longer_41_letters(self):
        collector = BooksCollector()
        collector.add_new_book('Алиса в Стране Чудес, Или Странствие в Странную Страну по страницам престранной пространной истории')
        assert len(collector.get_books_genre()) == 0

    def test_get_book_genre_for_book_without_genre(self):
        collector = BooksCollector()
        collector.get_book_genre('Что делать, если ваш кот хочет вас убить')
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') is None

    def test_get_books_with_specific_no_horror_books(self):
        collector = BooksCollector()
        books_with_specific_genre = collector.get_books_with_specific_genre('Ужасы')
        assert len(books_with_specific_genre) == 0

    def test_get_books_genre_get_genre_for_all_books(self):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter')
        collector.set_book_genre('Harry Potter', 'Фантастика')
        collector.add_new_book('It')
        collector.set_book_genre('It', 'Ужасы')
        collector.add_new_book('Winnie the Pooh')
        collector.set_book_genre('Winnie the Pooh', 'Мультфильмы')
        book_genre = collector.get_books_genre()
        assert book_genre['Harry Potter'] == 'Фантастика'
        assert book_genre['It'] == 'Ужасы'
        assert book_genre['Winnie the Pooh'] == 'Мультфильмы'


    def test_get_books_for_children_get_0_books(self):
        collector = BooksCollector()
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 0

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_book_in_favorites("Harry Potter")
        assert "Harry Potter" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_book_in_favorites("Harry Potter")
        collector.add_book_in_favorites("Harry Potter")
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_book_not_from_list(self):
        collector = BooksCollector()
        favorite_book = collector.delete_book_from_favorites('Винни-Пух и все все все')
        assert favorite_book == None

    def test_get_list_of_favorites_books_get_all_books(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_book_in_favorites("Harry Potter")
        collector.get_list_of_favorites_books()
        assert len(collector.get_list_of_favorites_books()) == 1

