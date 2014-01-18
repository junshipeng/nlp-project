nlp-project
===========

This is a language model for Classical Chinese, a project for my course on Chinese NLP.

## 使用方法

1. 編譯 RNNLM： `cd ./bin/rnnlm/ && make`
1. 編譯 Word2vec： `cd ./bin/word2vec/ && make`
1. 下載、編譯 SRILM，並在`Config.py`中設置`srilmpath`。默認配置爲`srilmpath=./bin/srilm/bin/i686-m64`
1. 下載語料： `./DownloadCorpus.py`
1. 處理語料： `./PurifyCorpus.py`
1. 生成數據： `./GenerateData.py`
1. 訓練： `./Train.py`
1. 測試可以有兩種：
    * 一種是對着測試集求語言模型的PPL： `./Test.py`
    * 一種是測試若干制定填空題： `./TestExamples`
        輸入文件是 `./test.txt`，格式爲「題目　選項１　選項２　等等」，其中題目中的空用全角問號「？」表示，題目和選項、選項和選項之間的空格也是全角的。

## 語料之來源

* [維基文庫] (https://zh.wikisource.org/wiki/)

## 所使用之工具

* [rnnlm] (http://www.fit.vutbr.cz/~imikolov/rnnlm/) 
* [srilm] (http://www.speech.sri.com/projects/srilm/)
* [word2vec] (https://code.google.com/p/word2vec/) 
