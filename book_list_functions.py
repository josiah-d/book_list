"""
Created on Thu Feb 27 19:07:24 2020.

@author: josiah
@title: book_list_functions.py
@summary: Back bone of program. Stores key functionality of book list program.
******************************************************************************
* To-Do:
*   - Identify if two books exist that are the same but one is marked read
*     and the other is not marked
*       - Done: Removing duplicates
*   - Make other options:
*       - Browse for books
*       - Search
*       - Suggestions
*       - GoodReads or Amazon summary
*   - Means of updating a book
*   - Access to df
*   - Update categories if new category entered
*   - When df updates, all go to title() and are sorted
*   - Add book reports into Book() class
*       - Enable being able to retrieve the book report
*   - 
******************************************************************************
"""
import os
import pandas as pd

categories = ['action_adventure', 'anthropology', 'biography', 'business',
              'christianity', 'engineering_maths', 'fantasy', 'farming',
              'finance', 'health', 'history', 'horror', 'leadership',
              'literary_fiction', 'medicine', 'meditation', 'mystery',
              'neuroscience', 'philosophy', 'politics', 'productivity',
              'psychology_sociology', 'religion_other', 'sailing', 'sci_fi',
              'science', 'self_improvement', 'strategy', 'technology',
              'writing']

truthy_values = ['y', 'yes']
falsey_values = ['n', 'no', '']


class Book():
    """Creates a book object."""

    def __init__(self):
        self.l_name = input('Enter the author\'s last name.\n> ').title()
        self.f_name = input('Enter the author\'s first name.\n> ').title()
        self.title = input('Enter the book\'s title.\n> ').title()
        self.read_status = input('Have you read the book? None, Paper, or '
                                 'Audio\n> ')
        print(categories)
        self.category = input('Enter a category.\n> ')


def open_help():
    """Open the help page."""
    with open('/Users/josiah/python_projects/personal/book_list_proj/'
              'help.txt', 'r') as f_obj:
        help_file = f_obj.read()
        print(help_file)


def book_list_exists(path):
    """Determine if the book list exists. Create or returns it."""
    columns = ['l_name', 'f_name', 'title', 'read_status', 'category']

    if os.path.isfile(path):
        book_df = pd.read_csv(path)
    else:
        book_df = pd.DataFrame(columns=columns)
    book_df.drop_duplicates(inplace=True)

    return book_df, columns


def new_book_question(path):
    """Determine whether a new book should be added to the list."""
    new_book_input = input('Do you want to add a new book?\n'
                           'Enter y/n.\n'
                           'Enter h or help for the Help File\n> ').lower()

    if new_book_input in ['h', 'help']:
        open_help()
    else:
        if new_book_input in truthy_values:
            add_new_book(path)
        elif new_book_input in falsey_values:
            pass
        else:
            new_book_question(path)

        return add_new_book


def add_new_book(path):
    """Add a new book to the current book list."""
    book = Book()

    # Add the new book to the list
    add_changes(book_list_exists(path)[0], book, path)

    # Save the new book to the book list
    question = input('Do you want to save the changes?\n> ')
    if question in truthy_values:
        save_book_list(book_list_exists(path)[0])

    # Send prompt for another book
    print('-' * 80)
    new_book_question(path)


def add_changes(book_df, change, path):
    """Add changes to the book list.."""
    if isinstance(change, Book):
        book_df = book_df.append(dict(change.__dict__.items()),
                                 ignore_index=True)
        book_already_exists(dict(change.__dict__.items()), book_df, path)
    else:
        book_df = book_df.append(change, ignore_index=True)
    save_book_list(book_df)


def save_book_list(book_df):
    """Save the book list."""
    book_df.sort_values(by=['category', 'l_name', 'f_name', 'title'],
                        inplace=True)
    book_df.to_csv('test_book_list.csv', index=False)


def duplicated_books(path):
    """Remove duplicated books."""
    book_df = book_list_exists(path)[0]
    book_df.drop_duplicates(subset=['l_name', 'f_name', 'title'],
                            keep='last', inplace=True, ignore_index=True)
    print('dropped book')
    save_book_list(book_df)


def book_already_exists(book, book_df, path):
    """Determine whether the book is already in the book list."""
    if book.values() in book_df:
        print('The book is already in the book list.')
