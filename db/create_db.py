import sqlite3
import os


def create_db(name_db: str):
    return sqlite3.connect(os.getcwd() + '\\db\\' + name_db + '.db')


def get_cursor(name_db='test'):
    return create_db(name_db).cursor()


if __name__ == '__main__':
    pass