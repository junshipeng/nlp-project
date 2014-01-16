#!/bin/bash

srilmpath=./srilm/bin/i686-m64
rnnpath=./rnnlm
trainfile=./corpus/purified.rnnlm.train.txt
validfile=./corpus/purified.rnnlm.valid.txt
testfile=./corpus/purified.rnnlm.test.txt
rnnmodel=./models/ptb.model.hidden100.class100.txt
temp=./temp

if [ ! -e $rnnmodel ]; then
    echo "model file not found... run first train.sh"
    exit
fi

#################################################
# N-GRAM MODEL IS TRAINED HERE, USING SRILM TOOLS
#################################################

$srilmpath/ngram-count -text $trainfile -order 5 -lm $temp/templm -gt3min 1 -gt4min 1 -kndiscount -interpolate -unk
$srilmpath/ngram -lm $temp/templm -order 5 -ppl $testfile -debug 2 > $temp/temp.ppl -unk

$rnnpath/convert <$temp/temp.ppl >$temp/ngram.txt

##################################################
# MODELS ARE COMBINED HERE, PERPLEXITY IS REPORTED
##################################################

lambda=0.8

time $rnnpath/rnnlm -rnnlm $rnnmodel \
                    -test $testfile \
                    -lm-prob $temp/ngram.txt \
                    -lambda $lambda \
                    -nbest\
                    > $temp/rnnlm_out

cat $temp/rnnlm_out | head -n -8 | tail -n +6 > $temp/rnnlm_test_score
