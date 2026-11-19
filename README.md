# qa_python


1. метод add_new_book

    позитивные:
        1.1. test_add_new_book_add_two_books (метод добавляет две книги)
        1.2. test_add_new_book_adds_book_with_valid_name_length (книга с длиной названия больше 0 и меньше 41 добавляется в books_genre)
        1.3. test_add_new_book_initial_genre_is_empty_string (после добавления книги значение жанра - пустая строка)

    негативные:
        1.3. test_add_new_book_duplicate_not_added (при повторном добавлении книги количество книг в словаре не увеличивается)
        1.4. test_add_new_book_duplicate_genre_not_overwritten (при повторном добавлении книги её жанр не перезаписывается)
        1.5. test_add_new_book_invalid_name_length_not_added (книги с некорректной длиной имени не добавляются; тест параметризован)

2. метод set_book_genre

    позитивный:
        2.1. test_set_book_genre_for_existing_book (существующей книге устанавливается допустимый жанр)

    негативный:
        2.2. test_set_book_genre_with_invalid_data_does_not_change_books (при указании несуществующей книги или недопустимого жанра словарь книг не изменяется; тест параметризован)

3. метод get_book_genre
    
    позитивный:
        3.1. test_get_book_genre_returns_genre_for_existing_book (для существующей книги возвращается её жанр)
 
    негативный:
        3.2. test_get_book_genre_returns_none_for_nonexistent_book (для книги, которой нет в словаре, возвращается None)

4. метод get_books_with_specific_genre
    
    позитивный:
        4.1. test_get_books_with_specific_genre_returns_matching_books (возвращаются только книги указанного жанра)
        
    негативный:
        4.2. test_get_books_with_specific_genre_returns_empty_list (для жанра без книг или недопустимого жанра возвращается пустой список; тест параметризован)

5. метод get_books_genre
    
    позитивный:
        5.1. test_get_books_genre_returns_books_and_genres (возвращается словарь с добавленными книгами и их жанрами)

6. метод get_books_for_children
    позитивные: 
        6.1. test_get_books_for_children_returns_books_without_age_rating (возвращаются книги с жанрами без возрастного рейтинга; книги с возрастным рейтингом и без жанра не попадают в список)
        6.2. test_get_books_for_children_returns_empty_list_when_no_suitable_books (если подходящих книг нет, возвращается пустой список)

7. метод add_book_in_favorites
 
    позитивный:
        7.1. test_add_book_in_favorites_adds_existing_book (книга из словаря добавляется в избранное)
    
    негативный:
        7.2. test_add_book_in_favorites_does_not_add_duplicate_or_nonexistent_book (повторное добавление книги и добавление книги, которой нет в словаре, не изменяют список избранного; тест параметризован)

8. метод delete_book_from_favorites
    
    позитивный:
        8.1. test_delete_book_from_favorites_removes_existing_book (книга удаляется из избранного)
    
    негативный:
        8.2. test_delete_book_from_favorites_does_not_change_list_for_missing_book (если книги нет в избранном, список не изменяется)

9. метод get_list_of_favorites_books
    
    позитивный:
        9.1. test_get_list_of_favorites_books_returns_favorites (возвращается текущий список избранных книг, в том числе когда он пуст; тест параметризован)
