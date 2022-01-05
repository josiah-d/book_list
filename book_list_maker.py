"""
Created on Sun Mar  1 20:00:03 2020.

@author: josiah
@title: book_list_maker
@summary: Runs the book list to book lst program
"""

import book_list_to_book_list as bl2bl

path = '/Users/josiah/python_projects/personal/book_list_proj/'\
       'test_book_list.csv'

if __name__ == '__main__':
    # Book list maker
    bl2bl.text_to_buckets(bl2bl.all_else, bl2bl.l_name, bl2bl.f_name,
                          bl2bl.title)
    try:
        for i in range(1150):
            bl2bl.add_new_book(bl2bl.agg_book_info(
                i, bl2bl.l_name, bl2bl.f_name, bl2bl.title), path)
    except IndexError:
        print('index error')
        pass
    bl2bl.print_l_name(bl2bl.l_name)
    bl2bl.print_len(bl2bl.all_else, bl2bl.l_name, bl2bl.f_name, bl2bl.title)
