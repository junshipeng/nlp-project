#!/usr/bin/env python3

import sys

from Config import dict_size

def encode_corpus(corpus_file):
    d = []
    with open('./data/dict.txt') as f:
        for line in f:
            if len(d) > dict_size:
                break
            d.append( ord(line.strip('\n\r').split()[-1]) )
    d = set(d)
    
    res = []
#    print(corpus_file)
#    print(open(corpus_file).read())
    with open(corpus_file) as f:
        for line in f:
            out = map(lambda _:ord(_),line.strip('\r\n'))
            outline = ' '.join(map(lambda _:str(_) if _ in d else '<unk>',out))
            res.append(outline)

    return res

