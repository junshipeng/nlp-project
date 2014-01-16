#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request, urllib.parse
from multiprocessing import Process, Queue
import queue
import time

from books_list import books

def all_tag(url,tag):
    #print('url: %s'%url)
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    soup = BeautifulSoup(html)
    s = soup.find_all(tag)
    return s

host='https://zh.wikisource.org'
prefix_first='/zh-hant/'

def get_chapter(out_q,url):
    for e in map(lambda _:_.text, all_tag(url,'p')):
        out_q.put( e )
    print('DONE : %s'%urllib.parse.unquote(url))

def get_book(name):
    prefix = prefix_first + urllib.parse.quote(name)

    process_queue = []
    out_q = Queue()

    for a in all_tag(host+prefix,'a'):
        ref = a.get('href')
        if ref:
            ref = ref.replace('/wiki/','/zh-hant/') # require Traditional Chinese
            if ref.startswith(prefix+'/'):
                process_queue.append( Process(target=get_chapter,args=(out_q,host+ref,)) )
    
    print("Totally %d for %s"%(len(process_queue),name))

    for p in process_queue:
        p.start()
        time.sleep(0.1)

    res = []
    while True:
        try:
            e = out_q.get(timeout=4)
            res.append( e )
        except queue.Empty:
            break

    for p in process_queue:
        p.join()

    return res

def main():
    for book in books:
        content = get_book(book)
        with open(book+'.txt','w') as f:
            for p in content:
                print(p,file=f)

if __name__ == '__main__':
    main()
