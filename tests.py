import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_book_add_two_books(self): # Проверка добавления книг.
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_get_book_rating(self): # Проверка установка рейтинга книги
        book_honor = 'Гордость и предубеждение и зомби'
        raitingBook = BooksCollector()
        raitingBook.add_new_book(book_honor)
        raitingBook.set_book_rating(book_honor, 8)

        assert raitingBook.get_book_rating(book_honor) == 8


    def test_set_book_rating_more_10_true(self): #Нельзя выставить рейтинг больше 10.
        book_cat = 'Что делать, если ваш кот хочет вас убить'
        raitingBook = BooksCollector()
        raitingBook.add_new_book(book_cat)
        raitingBook.set_book_rating(book_cat, 12)

        assert raitingBook.get_book_rating(book_cat) == 1


    def test_set_book_rating_less_1_true(self): # Нельзя выставить рейтинг меньше 1.
        book_cat = 'Что делать, если ваш кот хочет вас убить'
        raitingBook = BooksCollector()
        raitingBook.add_new_book(book_cat)
        raitingBook.set_book_rating(book_cat, 0)

        assert raitingBook.get_book_rating(book_cat) == 1


    def test_set_rating_to_none_book_true(self): #Нельзя выставить рейтинг книге, которой нет в списке.
        book_cat = 'Что делать, если ваш кот хочет вас убить'
        raitingBook = BooksCollector()
        raitingBook.set_book_rating(book_cat, 5)

        assert raitingBook.get_book_rating(book_cat) is None

    def test_add_double_book_false(self): # Нельзя добавить одну и ту же книгу дважды.
        book_cat = 'Что делать, если ваш кот хочет вас убить'
        doubleBook = BooksCollector()
        doubleBook.add_new_book(book_cat)
        doubleBook.add_new_book(book_cat)
        books = list(doubleBook.get_books_rating())
        count_of_book_cat = 0

        for i in books:
            if i == book_cat:
                count_of_book_cat += 1

        assert count_of_book_cat == 1

    def test_add_book_to_favour_true(self):  # Добавление книг в Избранное
        book_cat = 'Что делать, если ваш кот хочет вас убить'
        book_honor = 'Гордость и предубеждение и зомби'
        favouriteBook = BooksCollector()
        favouriteBook.add_new_book(book_cat)
        favouriteBook.add_new_book(book_honor)
        favouriteBook.add_book_in_favorites(book_cat)

        assert book_cat in favouriteBook.get_list_of_favorites_books()
        assert book_honor not in favouriteBook.get_list_of_favorites_books()

    def test_delete_book_from_favour_true(self):  # Удаление книги из Избранного
        book_cat = 'Что делать, если ваш кот хочет вас убить'
        book_honor = 'Гордость и предубеждение и зомби'
        favouriteBook = BooksCollector()
        favouriteBook.add_new_book(book_cat)
        favouriteBook.add_new_book(book_honor)
        favouriteBook.add_book_in_favorites(book_cat)
        favouriteBook.add_book_in_favorites(book_honor)

        favouriteBook.delete_book_from_favorites(book_honor)

        assert book_cat in favouriteBook.get_list_of_favorites_books()
        assert book_honor not in favouriteBook.get_list_of_favorites_books()

    def test_get_books_with_specific_rating_true(self):  # Выборка книг по рейтингу
        books_list = ['Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби',
                      'Питон за 15 минут для чайников и кружек', 'Инфоцыганство как оно есть без прикрас',
                      'Как жить полной жизнью имея двойной подбородок', 'Менистр Културы - сценарий - BadComedian']

        ratings_list = [9, 5, 3, 5, 7, 7]
        ratingBook = BooksCollector()
        for i in range(len(books_list)):
            ratingBook.add_new_book(books_list[i])
            ratingBook.set_book_rating(books_list[i], ratings_list[i])
        spec_rating_5 = ratingBook.get_books_with_specific_rating(5)
        spec_rating_7 = ratingBook.get_books_with_specific_rating(7)

        assert len(spec_rating_5) == 2
        assert books_list[1] in spec_rating_5 and books_list[3] in spec_rating_5

        assert len(spec_rating_7) == 2
        assert books_list[4] in spec_rating_7 and books_list[5] in spec_rating_7

        assert ratingBook.get_books_with_specific_rating(2) == []
