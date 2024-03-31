# booklover_test.py

import unittest
import pandas as pd
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        lover = BookLover("Test User", "test@example.com", "Fantasy")
        lover.add_book("The Hobbit", 4)
        self.assertTrue(lover.has_read("The Hobbit"))

    def test_2_add_book(self):
        lover = BookLover("Test User", "test@example.com", "Fantasy")
        lover.add_book("The Hobbit", 4)
        lover.add_book("The Hobbit", 4)
        self.assertEqual(lover.book_list[lover.book_list['book_name'] == "The Hobbit"].shape[0], 1)

    def test_3_has_read(self):
        lover = BookLover("Test User", "test@example.com", "Fantasy")
        lover.add_book("The Hobbit", 4)
        self.assertTrue(lover.has_read("The Hobbit"))

    def test_4_has_read(self):
        lover = BookLover("Test User", "test@example.com", "Fantasy")
        lover.add_book("The Hobbit", 4)
        self.assertFalse(lover.has_read("1984"))

    def test_5_num_books_read(self):
        lover = BookLover("Test User", "test@example.com", "Fantasy")
        lover.add_book("The Hobbit", 4)
        lover.add_book("1984", 5)
        self.assertEqual(lover.num_books_read(), 2)

    def test_6_fav_books(self):
        lover = BookLover("Test User", "test@example.com", "Fantasy")
        lover.add_book("The Hobbit", 4)
        lover.add_book("1984", 2)
        fav_books = lover.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)

   

