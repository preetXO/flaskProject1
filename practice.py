class Book:
    TYPES = ('hardcover', 'paperback')
    def __init__(self, name, booktype, weight):
        self.name = name
        self  .booktype = booktype
        self.weight = weight

    def __repr__(self):
        return f'<{self.name!r}, ({self.booktype}), weighing {self.weight}'

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight + 100)

    @classmethod
    def softcover(cls, name, weight):
        return cls(name, cls.TYPES[1], weight)


if __name__ == '__main__':
    book = Book('Harry Potter', 'Hard cover', 100)
    book1 = Book.hardcover('Harry Potter', 100)
    book2 = Book.softcover('Harry Potter', 100)
    print(book)
    print(book1)
    print(book2)
