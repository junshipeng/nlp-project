#!/usr/bin/env python

import os

def word2vec_train(word2vecpath,word2vectrainfile,word2vecmodel):
    dim = 50
    cmd = [ word2vecpath+'/word2vec',
        '-train',word2vectrainfile,
        '-output',word2vecmodel,
        '-cbow','0',
        '-size',str(dim),
        '-window 5 -negative 0 -hs 1 -sample 1e-3 -threads 4 -binary 0',]

    os.system( ' '.join(cmd) )

    os.system( 'mv '+word2vecmodel+' '+word2vecmodel+'.tmp' )
    os.system( 'tail -n +2 '+word2vecmodel+'.tmp > '+word2vecmodel )
    extraline = '</s>'+' 0'*dim
    os.system( 'echo "'+extraline+'" >> '+word2vecmodel )

    

def rnnlm_train(rnnpath,trainfile,validfile,rnnmodel,word2vecmodel,hidden_size,class_size,bptt_steps):
    if os.path.exists(rnnmodel):
        os.remove(rnnmodel)

    cmd = [rnnpath+'/rnnlm',
        '-train',trainfile,
        '-valid',validfile,
        '-rnnlm',rnnmodel,
        '-hidden',str(hidden_size),
        '-rand-sed 1',
        '-debug 2',
        '-class',str(class_size),
        '-bppt',str(bptt_steps),
        '-bptt-block 10',
#        '-binary',
#        '-feature-matrix',word2vecmodel,
#        '-feature-gamma','0.00',
#        '-min-improvement','1.0005',
        ]

    os.system( ' '.join(cmd) )

def rnnlm_test(srilmpath,rnnpath,temp,trainfile,testfile,rnnmodel,word2vecmodel,lambda_value,nbest):
    cmd = srilmpath+'/ngram-count -text '+trainfile+' -order 5 -lm '+temp+'/templm -gt3min 1 -gt4min 1 -kndiscount -interpolate -unk 2>/dev/null'
    os.system( cmd )

    cmd = srilmpath+'/ngram -lm '+temp+'/templm -order 5 -ppl '+testfile+' -debug 2 > '+temp+'/temp.ppl -unk 2>/dev/null'
    os.system( cmd )

    cmd = rnnpath+'/convert <'+temp+'/temp.ppl >'+temp+'/ngram.txt 2>/dev/null'
    os.system( cmd )

    cmd = [ rnnpath + '/rnnlm',
            '-rnnlm', rnnmodel,
            '-test', testfile,
            '-lm-prob', temp+'/ngram.txt',
            '-lambda', str(lambda_value),
    #        '-feature-matrix',word2vecmodel,
    #        '-feature-gamma','0.1',
     
            ]
    if nbest:
        cmd += [ '-nbest' ]
    cmd += [ '> ',temp+'/rnnlm_out' ]
    os.system( ' '.join(cmd) )
    
    out = list(map(lambda _:_.strip('\r\n'),open(temp+'/rnnlm_out').readlines()))

    #print(out)

    if nbest:
        res = []
        for e in out:
            try:
                fe = float(e)
                res.append(fe)
            except ValueError:
                pass
    else:
        res = float( out[-1].split(' ')[-1] )

    #print(res)

    return res
