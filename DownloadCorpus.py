#!/usr/bin/env python3

import os.path
from Config import books
from LibWikisource import *

def main():
    for book in books:
        file_name = './corpus/'+book+'.txt'
        if not os.path.exists(file_name):
            content = get_book(book)
            with open(file_name,'w') as f:
                for p in content:
                    print(p,file=f)

if __name__ == '__main__':
    main()
