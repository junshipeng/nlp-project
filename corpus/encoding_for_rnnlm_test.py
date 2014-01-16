#!/usr/bin/env python3

import sys

def main():
    topk_chars = int(sys.argv[1])

    d = []
    with open('dict.txt') as f:
        for line in f:
            if len(d) > topk_chars:
                break
            d.append( ord(line.strip('\n\r').split()[-1]) )
    d = set(d)
    
    ftest = open('purified.rnnlm.test.txt','w')

    with open('test.txt') as f:
        for line in f:
            out = map(lambda _:ord(_),line.strip('\r\n'))
            outline = ' '.join(map(lambda _:str(_) if _ in d else '<unk>',out))
            print(outline,file=ftest)

if __name__ == '__main__':
    main()
