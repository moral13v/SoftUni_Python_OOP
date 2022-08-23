from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # {author: [book1, book2, ... BookN]}
        self.rented_books = {}  # {usernames: {book names: days to return}}

    def get_book(self, author, book_name, days_to_return, user: User):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                self.rented_books[user.username][book_name] = days_to_return
                return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, user: User):
        pass