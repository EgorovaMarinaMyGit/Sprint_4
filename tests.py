from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

# 1. add_new_book
    # п.1.1
    def test_add_new_book_add_two_books(self):
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
    
    # п.1.2
    def test_add_new_book_with_genre(self):
        collector = BooksCollector()
        book_name_with_genre = 'Дети капитана Гранта: Приключения'
        collector.add_new_book(book_name_with_genre)
        assert book_name_with_genre in collector.books_genre
        assert collector.books_genre[book_name_with_genre] == ''


# 2. set_book_genre
    # 2.1
    @pytest.mark.parametrize("name, genre", [
        ('Зловещие мертвецы', 'Ужасы'),
        ('Винни Пух', 'Мультфильмы')
    ])
    def test_set_book_genre_of_added_book_valid(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert self.books_genre[name] == genre


# 3. get_book_genre
    # 3.1
    @pytest.mark.parametrize("name, genre", [
        ('Зловещие мертвецы', 'Ужасы'),
        ('Винни Пух', 'Мультфильмы')
    ])
    def test_get_book_genre_valid(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert self.get_book_genre(name) == genre


# 4. get_books_with_specific_genre
    # 4.1. 
    def test_get_books_with_specific_genre_detectiv_genre(self):
        collector = BooksCollector()

        books = ['Детектив1', 'Детектив2', 'Комедия1', 'Мультфильм1']
        for book in books:
            collector.add_new_book(book)

        collector.set_book_genre('Детектив1', 'Детективы')
        collector.set_book_genre('Детектив2', 'Детективы')
        collector.set_book_genre('Комедия1', 'Комедии')
        collector.set_book_genre('Мультфильм1', 'Мультфильмы')

        expected_result = ['Детектив1', 'Детектив2']
        result_of_method = collector.get_books_with_specific_genre('Детективы')
        assert sorted(expected_result) == sorted(result_of_method)


# 5. get_books_genre
    # 5.1 
    def test_get_books_genre(self):
        collector = BooksCollector()

        books = ['Ужасы1', 'Детектив1', 'Комедия1', 'Мультфильм1']
        for book in books:
            collector.add_new_book(book)

        collector.set_book_genre('Ужасы1', 'Ужасы')
        collector.set_book_genre('Детектив1', 'Детективы')
        collector.set_book_genre('Комедия1', 'Комедии')
        collector.set_book_genre('Мультфильм1', 'Мультфильмы')
        assert collector.get_books_genre() == ['Ужасы', 'Детективы', 'Комедии', 'Мультфильмы']


# 6. get_books_for_children
    # 6.1
    def test_get_books_for_children(self):
        collector = BooksCollector()
        
        books = ['Ужасы1', 'Детектив1', 'Комедия1', 'Сказка', 'Детская книга', 'Фантастика1']
        for book in books:
            collector.add_new_book(book)

        collector.set_book_genre('Ужасы1', 'Ужасы')
        collector.set_book_genre('Детектив1', 'Детективы')
        collector.set_book_genre('Комедия1', 'Комедии')
        collector.set_book_genre('Сказка', 'Мультфильмы')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.set_book_genre('Фантастика1', 'Фантастика')
        assert sorted(collector.get_books_for_children()) == sorted(['Комедия1', 'Сказка', 'Детская книга', 'Фантастика1'])


# 7. add_book_in_favorites
    # 7.1 
    @pytest.mark.parametrize("name", [
        ('Одиссея'),
        ('Капитана Блада')
    ])
    def test_add_book_in_favorites_at_once(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        expected_favorites = [name]
        assert sorted(collector.get_list_of_favorites_books()) == sorted(expected_favorites)


    # 7.2
    @pytest.mark.parametrize("name", [
        ('Тестирование'),
        ('Автотесты')
    ])
    def test_add_book_in_favorites_twice(self, name):
        collector = BooksCollector()
    
        collector.add_new_book(name)
        self.favorites = []
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1


# 8. delete_book_from_favorites
    # 8.1 
    @pytest.mark.parametrize("name", [
        ('Сказка'),
        ('Для детей')
    ])
    def test_delete_book_from_favorites_existing(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 0

    # 8.2
    @pytest.mark.parametrize("name", [
        ('Рим'),
        ('Барселона')
    ])
    def test_delete_book_from_favorites_not_existing(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites('Книга, которой нет')
        assert len(collector.get_list_of_favorites_books()) == 1

# 9. get_list_of_favorites_books
    # 9.1 
    @pytest.mark.parametrize("name", [
        ('Дикая роза'),
        ('Санта Барбара')
    ])
    def test_get_list_of_favorites_books(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        expected_result = [name]
        assert sorted(collector.get_list_of_favorites_books()) == sorted(expected_result)
        






