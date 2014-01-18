#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from multiprocessing import Process, Queue
import queue
import time

def all_tag(url,tag):
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode()
        soup = BeautifulSoup(html)
        s = soup.find_all(tag)
        return s
    except urllib.error.HTTPError:
        return []


def get_chapter(out_q,url):
    for e in map(lambda _:_.text, all_tag(url,'p')):
        out_q.put( e )
    print('DONE : %s'%urllib.parse.unquote(url))

def get_book(name):
    host='https://zh.wikisource.org'
    prefix_first='/zh-hant/'
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
        time.sleep(0.5)

    res = []
    while True:
        try:
            e = out_q.get(timeout=5)
            res.append( e )
        except queue.Empty:
            break

    for p in process_queue:
        p.join()

    return res

