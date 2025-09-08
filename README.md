# Sprint_4

Спиок тестов:

test_get_book_genre_existing_book_without_genre_returns_empty_string
 Проверяет, что книга без жанра возвращает пустую строку

test_get_book_genre_after_setting_returns_genre
 Проверяет, что после установки жанра возвращается корректное значение жанра

test_get_book_genre_nonexistent_book_returns_none
 Проверяет, что для несуществующей книги возвращается None

test_get_books_genre_initially_empty_dict
 Проверяет, что словарь со списком жанров пуст после инициализации

test_get_books_genre_contains_added_books
 Проверяет,жанр у двух книг, одна из книг без жанра, жанр второй соответствует заданному
 
test_new_book_init_no_genre
 Проверяет, что у новой добавленной книги изначально нет жанра

test_add_new_book_name_validation['A']
 Проверяет добавление книги с названием с минимальной длиной названия

test_add_new_book_name_validation['Moby Dick']
 Проверяет добавление книги с названием из нескольких слов

test_add_new_book_name_validation['']
 Проверяет, что книга с пустым названием не добавляется

test_add_new_book_name_validation['N'x40]
 Проверяет добавление книги с максимально допустимой длиной названия (40 символов)

test_add_new_book_name_validation['N'x41]
 Проверяет, что книга с названием длиннее 40 символов не добавляется

test_add_new_book_duplicate_not_added
 Проверяет, что дубликаты книг не добавляются повторно

test_set_book_genre_in_genres['Фантастика']
 Проверяет установку жанра 'Фантастика'

test_set_book_genre_in_genres[Комедии]
 Проверяет установку жанра 'Комедии'

test_set_book_genre_in_genres[Мультфильмы]
 Проверяет установку жанра 'Мультфильмы'

test_set_book_genre_invalid_genre_not_set
 Проверяет, что недопустимый жанр не присваивается книге

test_set_book_genre_nonexistent_book_ignored
 Проверяет, что попытка установить жанр несуществующей книге игнорируется

test_get_books_with_specific_genre_invalid_returns_empty_list
 Проверяет, что при запросе по недопустимому жанру возвращается пустой список

test_get_books_with_specific_genre_returns_books
 Проверяет возврат только книг заданного жанра

test_get_books_with_specific_genre_no_books_returns_empty_list
 Проверяет, что при отсутствии книг возвращается пустой список

test_get_books_for_children_excludes_adult
 Проверяет, что из списка "для детей" исключаются книги с возрастными жанрами

test_add_book_in_favorites_adds_book
 Проверяет добавление книги в список избранного

test_add_book_in_favorites_nonexistent_book_not_added
 Проверяет, что несуществующая книгу не добавляется в избранное

test_add_book_in_favorites_duplicate_not_added
 Проверяет, что книга не добавляется в избранное повторно

test_delete_book_from_favorites_removes_book
 Проверяет удаление книги из списка избранного

test_delete_book_from_favorites_nonexistent_book_ignored
 Проверяет, что удаление несуществующей книги игнорируется и список избранного не изменяется.