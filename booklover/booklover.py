
# Course:  DS 5100
# Module:  08 Python Testing
# Topic:   HW Unit Testing a Book Lover Class
# Author:  R.C. Alvarado (adapted)
# Date:    7 July 2023
#---------------------------------------------------------

# Name: Zachary Holland
# Net UD: nms9dg
# URL of this files in GitHub:https://github.com/zhollandUVA/DS5100-nms9dg/tree/main/lessons/M08
#------------------------------------------------------------------------------------------------

# booklover.py

import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):
        if not self.has_read(book_name):
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print(f"{book_name} is already in your book list.")

    def has_read(self, book_name):
        return any(self.book_list['book_name'] == book_name)

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    print(test_object.has_read("War of the Worlds"))
    print(test_object.num_books_read())
    print(test_object.fav_books())
    
    
    
    
#-------------------------------------------------------------------------------------------------------------------------------    
