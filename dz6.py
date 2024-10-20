class Book:
    def __init__(self, title, author, year, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = "Прочитана" if self.read else "Непрочитана"
        return f"{self.title} - {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def find_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results

    def find_by_author(self, author):
        results = [book for book in self.books if author.lower() in book.author.lower()]
        return results

    def mark_book_as_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_read()
                print(f"Книга '{title}' отмечена как прочитанная.")
                return
        print(f"Книга '{title}' не найдена.")

    def delete_book(self, title):
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        print(f"Книга '{title}' удалена из библиотеки.")

    def filter_by_read_status(self, read=True):
        results = [book for book in self.books if book.read == read]
        return results

    def sort_by_year(self):
        self.books.sort(key=lambda book: book.year)


def main():
    library = Library()

    while True:
        print("\nДоступные команды:")
        print("1. Добавить книгу")
        print("2. Просмотреть список книг")
        print("3. Найти книгу по названию")
        print("4. Найти книги по автору")
        print("5. Отметить книгу как прочитанную")
        print("6. Удалить книгу")
        print("7. Просмотреть прочитанные книги")
        print("8. Просмотреть непрочитанные книги")
        print("9. Сортировать книги по году публикации")
        print("0. Выйти")

        command = input("Введите номер команды: ")

        if command == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год публикации: "))
            library.add_book(Book(title, author, year))
            print("Книга добавлена.")
        elif command == "2":
            library.list_books()
        elif command == "3":
            title = input("Введите название книги для поиска: ")
            results = library.find_by_title(title)
            if results:
                for book in results:
                    print(book)
            else:
                print("Книги не найдены.")
        elif command == "4":
            author = input("Введите автора для поиска: ")
            results = library.find_by_author(author)
            if results:
                for book in results:
                    print(book)
            else:
                print("Книги не найдены.")
        elif command == "5":
            title = input("Введите название книги для отметки как прочитанную: ")
            library.mark_book_as_read(title)
        elif command == "6":
            title = input("Введите название книги для удаления: ")
            library.delete_book(title)
        elif command == "7":
            read_books = library.filter_by_read_status(True)
            if read_books:
                for book in read_books:
                    print(book)
            else:
                print("Нет прочитанных книг.")
        elif command == "8":
            unread_books = library.filter_by_read_status(False)
            if unread_books:
                for book in unread_books:
                    print(book)
            else:
                print("Нет непрочитанных книг.")
        elif command == "9":
            library.sort_by_year()
            print("Книги отсортированы по году публикации.")
        elif command == "0":
            break
        else:
            print("Неверная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
