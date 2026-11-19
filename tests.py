from main import BooksCollector
import pytest

class TestBooksCollector:
    @pytest.fixture
    def empty_books_collector(self):
        return BooksCollector()

    @pytest.fixture
    def filled_books_collector(self):
        filled_books_collector = BooksCollector()
        filled_books_collector.books_genre = {'Шерлок Холмс': 'Детективы'} 
        
        return filled_books_collector
    
    def test_add_new_book_add_two_books(self, empty_books_collector):
        empty_books_collector.add_new_book('Гордость и предубеждение и зомби')
        empty_books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        
        assert len(empty_books_collector.books_genre) == 2

    @pytest.mark.parametrize('name', ['Черновик', 'a', 'aa', 'a' * 39, 'a' * 40])
    def test_add_new_book_adds_book_with_valid_name_length(self, empty_books_collector, name):
        empty_books_collector.add_new_book(name)

        assert name in empty_books_collector.books_genre

    def test_add_new_book_initial_genre_is_empty_string(self, empty_books_collector):
        name = '12 стульев'

        empty_books_collector.add_new_book(name)

        assert empty_books_collector.books_genre[name] == ''

    def test_add_new_book_duplicate_not_added(self, filled_books_collector):
        name = 'Шерлок Холмс'
        initial_dict_length = len(filled_books_collector.books_genre)

        filled_books_collector.add_new_book(name)

        assert len(filled_books_collector.books_genre) == initial_dict_length


    def test_add_new_book_duplicate_genre_not_overwritten(self, filled_books_collector):
        name = 'Шерлок Холмс'
        initial_genre = filled_books_collector.books_genre[name]

        filled_books_collector.add_new_book(name)

        assert filled_books_collector.books_genre[name] == initial_genre

    @pytest.mark.parametrize('name', ['', 'a' * 41, 'a' * 42])
    def test_add_new_book_invalid_name_length_not_added(self, empty_books_collector, name):
        empty_books_collector.add_new_book(name)

        assert name not in empty_books_collector.books_genre

    def test_set_book_genre_for_existing_book(self, filled_books_collector):
        name = 'Шерлок Холмс'
        genre = 'Фантастика'

        filled_books_collector.set_book_genre(name, genre)

        assert filled_books_collector.books_genre[name] == genre


    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Шерлок Холмс', 'Несуществующий жанр'),
            ('Несуществующая книга', 'Фантастика'),
        ]
    )
    def test_set_book_genre_with_invalid_data_does_not_change_books(self, filled_books_collector, name, genre):
        initial_books = filled_books_collector.books_genre.copy()

        filled_books_collector.set_book_genre(name, genre)

        assert filled_books_collector.books_genre == initial_books 

    def test_get_book_genre_returns_genre_for_existing_book(self, filled_books_collector):
        name = 'Шерлок Холмс'

        genre = filled_books_collector.get_book_genre(name)

        assert genre == 'Детективы'


    def test_get_book_genre_returns_none_for_nonexistent_book(self, filled_books_collector):
        name = 'Несуществующая книга'

        genre = filled_books_collector.get_book_genre(name)

        assert genre is None

    def test_get_books_with_specific_genre_returns_matching_books(self, filled_books_collector):
        filled_books_collector.books_genre['Дюна'] = 'Фантастика'
        filled_books_collector.books_genre['1984'] = 'Фантастика'

        books = filled_books_collector.get_books_with_specific_genre('Фантастика')

        assert books == ['Дюна', '1984']


    @pytest.mark.parametrize('genre', ['Ужасы', 'Несуществующий жанр'])
    def test_get_books_with_specific_genre_returns_empty_list(self, filled_books_collector, genre):
        books = filled_books_collector.get_books_with_specific_genre(genre)

        assert books == []

    def test_get_books_genre_returns_books_and_genres(self, filled_books_collector):
        books = filled_books_collector.get_books_genre()

        assert books == {'Шерлок Холмс': 'Детективы'}

    def test_get_books_for_children_returns_books_without_age_rating(self, filled_books_collector):
        filled_books_collector.books_genre['Дюна'] = 'Фантастика'
        filled_books_collector.books_genre['Книга без жанра'] = ''

        books = filled_books_collector.get_books_for_children()

        assert books == ['Дюна']


    def test_get_books_for_children_returns_empty_list_when_no_suitable_books(self, filled_books_collector):
        books = filled_books_collector.get_books_for_children()

        assert books == []

    def test_add_book_in_favorites_adds_existing_book(self, filled_books_collector):
        name = 'Шерлок Холмс'

        filled_books_collector.add_book_in_favorites(name)

        assert filled_books_collector.favorites == [name]


    @pytest.mark.parametrize('name', ['Шерлок Холмс', 'Несуществующая книга'])
    def test_add_book_in_favorites_does_not_add_duplicate_or_nonexistent_book(self, filled_books_collector, name):
        filled_books_collector.favorites = ['Шерлок Холмс']

        filled_books_collector.add_book_in_favorites(name)

        assert filled_books_collector.favorites == ['Шерлок Холмс']
        
        
    def test_delete_book_from_favorites_removes_existing_book(self, filled_books_collector):
        name = 'Шерлок Холмс'
        filled_books_collector.favorites = [name]
    
        filled_books_collector.delete_book_from_favorites(name)
    
        assert filled_books_collector.favorites == []
    
    
    def test_delete_book_from_favorites_does_not_change_list_for_missing_book(self, filled_books_collector):
        filled_books_collector.favorites = ['Шерлок Холмс']
    
        filled_books_collector.delete_book_from_favorites('Несуществующая книга')
    
        assert filled_books_collector.favorites == ['Шерлок Холмс']

    @pytest.mark.parametrize('favorites', [[], ['Шерлок Холмс']])
    def test_get_list_of_favorites_books_returns_favorites(self, empty_books_collector, favorites):
        empty_books_collector.favorites = favorites

        result = empty_books_collector.get_list_of_favorites_books()

        assert result == favorites