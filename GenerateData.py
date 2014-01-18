#!/usr/bin/env python3

from random import shuffle
from LibCorpusEncoding import encode_corpus
from Config import train_portion, valid_portion, test_portion

def main():
    
    lines = encode_corpus('./data/purified_corpus.txt')
    shuffle(lines)

    all_size = sum( map(lambda l:len(l.split(' ')),lines ) )
    train_size = all_size * train_portion
    valid_size = all_size * valid_portion
    test_size = all_size * test_portion
 
    ftrain = open('./data/purified_corpus.rnnlm.train.txt','w')
    fvalid = open('./data/purified_corpus.rnnlm.valid.txt','w')
    ftest  = open('./data/purified_corpus.rnnlm.test.txt','w')
    ftest_human = open('./data/purified_corpus.rnnlm.test.human.txt','w')
    fword2vec = open('./data/purified_corpus.word2vec.train.txt','w')

    c = 0
    for line in lines:
        cout = len(line.split(' '))
        if c + cout <= train_size:
            print(line,file=ftrain)
            print(line,file=fword2vec)
            #print(' '+line,file=fword2vec,end='')
        elif c + cout <= train_size + valid_size:
            print(line,file=fvalid)
            print(line,file=fword2vec)
            #print(' '+line,file=fword2vec,end='')
        elif c + cout <= train_size + valid_size + test_size:
            print(line,file=ftest)
            print( ''.join(map(lambda _:chr(int(_)),line.split())) ,file=ftest_human )
        else:
            break
        c += cout
    

if __name__ == '__main__':
    main()
