# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 * 1024 * 1024
count_of_pages = 100
count_of_lines_on_one_page = 50
count_of_symbols_in_one_line = 25
symbol_size = 4
count_of_books = round(disk_size // (count_of_pages * count_of_lines_on_one_page * count_of_symbols_in_one_line * symbol_size))

print("Количество книг, помещающихся на дискету:", count_of_books)
