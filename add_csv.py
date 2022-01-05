# imports
import psycopg2

# db global variables
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'Master/99'
DATABASE = 'booklist'

# db connection
conn = psycopg2.connect(host=HOST, database=DATABASE,
                        user=USER, password=PASSWORD)

# import from csv


def import_from_csv(table, columns, path):
    """
    Takes a previous csv and adds it to a table

    table (string): name for the sql table
    columns (string): names of the columns in the table
        format: 'col_0, col_1, col_2, col_3, col_4'
        note: skip uuid column
    path (string): path to the csv
    """
    query = f'''COPY {table}({columns})
                FROM '{path}'
                DELIMITER ','
                CSV HEADER'''

    with conn.cursor() as c:
        c.execute(query)

    conn.commit()


if __name__ == '__main__':
    table = input('Enter the table name.\n-> ')
    columns = input(
        'Enter the columns of the table as a string. delim = ",".\n-> ')
    path = input('Enter the absolute path to the csv.\n-> ')

    import_from_csv(table, columns, path)
