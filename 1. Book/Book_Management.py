class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def print_info(self):
        print('Title: ', self.title)
        print('Author: ', self.author)
        print('Publication year: ', self.publication_year)
    
book1 = Book('English Made Easy: A Comprehensive Guide to Learning English', 'Emily Williams', '2022')

book1.print_info()
