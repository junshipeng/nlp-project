#!/usr/bin/python3

from collections import defaultdict
from functools import reduce

from Config import books

punc_sep = '。？！'
punc_ignore = '，；：、（）()\'　[]＜＞「」『』《》【】〔〕［］“”"\'〈〉'

def purify(line):
    l = line
    l = l.strip('\r\n')

    
    l = l.replace(' ','')
        
    for p in punc_sep:
        l = l.replace(p,' ')

    for p in punc_ignore:
        l = l.replace(p,'')
    
    # only keep space (' ') or CJK Unified Ideographs
    l = ''.join(filter(lambda _:_==' ' or (ord(_)>=0x4e00 and ord(_)<=0x9fff) ,l))
    
    l = l.split(' ')
    l = list(filter(lambda _:_!='',l))

    return l

def main():
    parts = [ purify(line) for book in books for line in open('./corpus/'+book+'.txt').readlines()]
    lst = []
    for part in parts:
        lst.extend( part )

    with open('./data/purified_corpus.txt','w') as f:
        for e in lst:
            print(e,file=f)

    count = defaultdict(int)
    all_sent = ''.join(lst)
    for c in all_sent:
        count[c] += 1

    words = set(all_sent)
    words_id = [ (count[word], ord(word), word) for word in words ]
    words_id.sort(reverse=True)
    with open('./data/dict.txt','w') as f:
        for (c,id,word) in words_id:
            print(c,id,word,file=f)

if __name__ == '__main__':
    main()
