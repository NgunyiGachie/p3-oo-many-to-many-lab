class Author:
    all = []
    
    def __init__(self, name=""):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"Author(name='{self.name}')"


class Book:
    all = []

    def __init__(self, title, authors=None):
        self.title = title
        self.authors = set()  
        self._contracts = set() 
        if authors:
            for author in authors:
                self.add_author(author)  

    def add_author(self, author):
        """Add an author to the book"""
        self.authors.add(author)

    def add_contract(self, contract):
        """Add a contract to the book"""
        self._contracts.add(contract)

    @property
    def contracts(self):
        """Return a list of contracts associated with this book"""
        return list(self._contracts)

    def authors(self):
        """Return a list of authors associated with this book"""
        return list(self.authors)

    def __repr__(self):
        return f'Book({self.title})'


   

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of the Author class")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of the Book class")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return (f"Contract(author={self.author.name}, book={self.book.title}, "
                f"date='{self.date}', royalties={self.royalties})")
