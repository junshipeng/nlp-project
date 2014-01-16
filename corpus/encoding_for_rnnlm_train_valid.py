#!/usr/bin/env python3

import sys

def main():
    topk_chars = int(sys.argv[1])
    size_train = int(sys.argv[2])
    size_valid = int(sys.argv[3])

    d = []
    with open('dict.txt') as f:
        for line in f:
            if len(d) > topk_chars:
                break
            d.append( ord(line.strip('\n\r').split()[-1]) )
    d = set(d)
    
    ftrain = open('purified.rnnlm.train.txt','w')
    fvalid = open('purified.rnnlm.valid.txt','w')

    c = 0
    with open('purified.txt') as f:
        for line in f:
            out = map(lambda _:ord(_),line.strip('\r\n'))
            outline = ' '.join(map(lambda _:str(_) if _ in d else '<unk>',out))
            cout = len(outline.split(' '))
            if c + cout <= size_train:
                print(outline,file=ftrain)
            elif c + cout <= size_train + size_valid:
                print(outline,file=fvalid)
            else:
                break
            c += cout

if __name__ == '__main__':
    main()
