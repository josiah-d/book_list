"""
Created on Sat Feb 29 23:19:13 2020.

@author: josiah
@title: book_list_run
@summary: Runs the book list program.
"""
import book_list_functions as blf

path = '/Users/josiah/python_projects/personal/book_list_proj/'\
       'test_book_list.csv'

if __name__ == '__main__':
    # Book functions
    blf.new_book_question(path)
    book_df = blf.book_list_exists(path)[0]
