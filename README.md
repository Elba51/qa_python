# qa_python

test_add_new_book_add_same_book - добавляем 2 одинаковые книги и смотрим, что нет повторов в списке

test_add_new_book_add_book_longer_41_letters - добавляем книги длиннее 41 символа (не должна добавиться)

test_get_book_genre_for_book_without_genre - пытаемся определить жанр книги, которой нет в списке и получаем None

test_get_books_with_specific_no_horror_books - ищем в пустом списке книги с жанром "Ужасы" и конечно ничего не получаем

test_get_books_genre_get_genre_for_all_books: Ищем жанр для 3 книг в словаре

test_get_books_for_children_get_0_books - ищем количество книг, подходящих для детей, их нет

test_add_book_in_favorites -  проверяем, что книга в списке избранного

test_add_book_in_favorites_existing_book - добавляем 2 одинаковые книги в список и проверяем, что добавилась одна

test_delete_book_from_favorites_delete_book_not_from_list - пытаемся удалить книгу, которой нет в списке избранного - метод не сломался, книг осталось ноль

test_get_list_of_favorites_books_get_all_books - получаем список избранных книг