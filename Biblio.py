class Book:
    
    def __init__(self, authorlast, authorfirst, title, place, publisher, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year
        
    def write_bib_enter(self):
        self.author = self.authorfirst+" "+self.authorlast
        print('Auther = ', self.author)
        print("Title = ", self.title)
        print("Place = ",self.place)
        print("Publisher = ", self.publisher)
        print("Year = ", self.year)

beauty = Book('Dubay', 'Thomas', 'The Evidential Power of Beauty', 'San Francisco', 'Ignatius Press', 1990)
pynut = Book('Martelli', 'Alex', 'Python in a Nutshell', 'Sebastopol, CA', "O'Reilly Media, Inc.", 2003)
             
print(Book.write_bib_enter(pynut))

print(beauty.write_bib_enter())

beauty.year = 2021        