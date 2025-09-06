import pytest
from main import BooksCollector


class TestBooksCollector:

    # Тесты для метода add_new_book   

    def test_new_book_init_no_genre(self):
        collector = BooksCollector()
        book_name = 'Идиот'
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize('book_name, expected_result', [
        ('A', True),
        ('Moby Dick', True),
        ('', False),
        ('B' * 40, True),
        ('Z' * 41, False)
    ])
    def test_add_new_book_name_validation(self, book_name, expected_result):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        book_added = book_name in collector.get_books_genre()
        assert book_added == expected_result

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        book_name = 'Moby Dick'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('genre', ['Фантастика', 'Комедии', 'Мультфильмы'])
    def test_set_book_genre_in_genres(self, genre):
        collector = BooksCollector()
        book_name = 'Moby Dick 2'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        book_name = 'Moby Dick 3'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Шутки за 300')
        assert collector.get_book_genre(book_name) == ''

    def test_set_book_genre_nonexistent_book_ignored(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.get_books_genre()

    def test_get_books_with_specific_genre_invalid_returns_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        result = collector.get_books_with_specific_genre('Несуществующий жанр')
        assert result == []

    def test_get_books_with_specific_genre_no_books_returns_empty_list(self):
        collector = BooksCollector()
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == []

    def test_get_books_for_children_excludes_adult(self):
        collector = BooksCollector()
        child_books = ['Книга 1', 'Книга 2']
        for book in child_books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Фантастика')
        
        adult_books = ['Нига 3', 'Нига 4']
        for book in adult_books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Ужасы')
        
        result = collector.get_books_for_children()
        assert len(result) == len(child_books)
        assert all(book in result for book in child_books)

    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()
        book_name = 'Книга 5'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Книга 6')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_duplicate_not_added(self):
        collector = BooksCollector()
        book_name = 'Книга 7'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        book_name = 'Книга 8'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_nonexistent_book_ignored(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Книга 9')
        assert collector.get_list_of_favorites_books() == []