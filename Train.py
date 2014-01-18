#!/usr/bin/env python3

from Config import *
from LibTrainTest import *

def main():
    word2vec_train(word2vecpath,word2vectrainfile,word2vecmodel)
    rnnlm_train(rnnpath,trainfile,validfile,rnnmodel,word2vecmodel,hidden_size,class_size,bptt_steps)

if __name__ == '__main__':
    main()
