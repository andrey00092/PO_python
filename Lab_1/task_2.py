# TODO Найдите количество книг, которое можно разместить на дискете

dick_capacity = 1.44  # MB
sym_capacity = 4      # B

Num_papers_per_book = 100
Num_rows_per_paper = 50
Num_sym_per_row = 25

Num_sym_per_book = Num_sym_per_row * Num_rows_per_paper * Num_papers_per_book

book_capacity = Num_sym_per_book * sym_capacity  # B
book_capacity = book_capacity/(1024**2)          # MB

Num_of_books = int(dick_capacity//book_capacity)

print("Количество книг, помещающихся на дискету:", Num_of_books)
