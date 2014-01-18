#!/usr/bin/env python3

import os
import math

from LibCorpusEncoding import encode_corpus
from LibTrainTest import rnnlm_test
from Config import *


def load_test_sets(filename):
    test_set = []
    for line in open(filename):
        l = line.strip('\r\n')
        
        p = l.find('#')
        if p != -1:
            l = l[:p]

        l = l.replace('　',' ')
        l = l.replace('？','?')
        tokens = l.split(' ')

        if len(tokens)<2:
            continue
    
        template = tokens[0]
        template = template.replace('?','%s')
        options = tokens[1:]

        test_set.append( ( template, options ) )

    return test_set

def main():
    test_set = load_test_sets('test.txt')

    # retrive data
    for test in test_set:
        test_score = []

        template = test[0]
        for option in test[1]:
            fout = open('./data/test.raw.txt','w')
            line = template % option
            print(line,file=fout)
            fout.close()

            # encode
            lines = encode_corpus('./data/test.raw.txt')
            with open('./data/test.rnnlm.txt','w') as fout:
                for line in lines:
                    print(line,file=fout)

            # call rnnlm
            #os.system('./TestSingle.sh >/dev/null')
            #score = list(map(float,open('./temp/rnnlm_test_score').readlines()))[0]
            score = rnnlm_test(srilmpath,rnnpath,temp,trainfile,'./data/test.rnnlm.txt',rnnmodel,word2vecmodel,lambda_value,nbest=True)[0]
            test_score += [score]
            #print(template,option,score)
        
        #print(test_score)

        max_score = max(test_score)
        best_id = test_score.index( max_score )

        template = test[0].replace('_','%s')
        best_option = test[1][best_id]
        best_option = '['+best_option+']'
        print(template%best_option)

        for id,option in enumerate(test[1]):
            a = math.exp(test_score[id])
            b = sum( map(lambda v:math.exp(v),test_score ))
            prob = a/b
            print('  %s(%.0f%%)'%(option,prob*100),end='')
        print()
   
    """
    for test in test_set:
        # generate raw file
        with open('./data/test.raw.txt','w') as fout:
            template = test[0]
            for option in test[1]:
                line = template % option
                print(line,file=fout)
        
        # encode
        lines = encode_corpus('./data/test.raw.txt')
        with open('./data/test.rnnlm.txt','w') as fout:
            for line in lines:
                print(line,file=fout)

        # call rnnlm
        os.system('./TestSingle.sh >/dev/null')
        
        # get score
        scores = list(map(float,open('./temp/rnnlm_test_score').readlines()))
        # print(scores)
        min_score = min(scores)
        best_id = scores.index( min_score )

        template = test[0].replace('_','%s')
        best_option = test[1][best_id]
        best_option = '['+best_option+']'
        print(template%best_option)

        for id,option in enumerate(test[1]):
            a = math.exp(-scores[id])
            b = sum( map(lambda v:math.exp(-v),scores ))
            prob = a/b
            print('  %s(%.0f%%)'%(option,prob*100),end='')
        print()
    """

if __name__ == '__main__':
    main()
