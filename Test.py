#!/usr/bin/env python3


from LibTrainTest import *
from Config import *

def main():
    score = rnnlm_test(srilmpath,rnnpath,temp,trainfile,testfile,rnnmodel,word2vecmodel,lambda_value,nbest=False)
    print('Test Scare = %.10lf'%score)


if __name__ == '__main__':
    main()
