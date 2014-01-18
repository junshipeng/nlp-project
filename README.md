nlp-project
===========

复旦大学《中文信息处理》一课之期末Project

作者：田应涛

## 使用方法

1. 建立以下文件夹：　`./data/` `./corpus/` `./models`　
1. 编译 RNNLM： `cd ./bin/rnnlm/ && make`
1. 编译 Word2vec： `cd ./bin/word2vec/ && make`
1. 下载、编译 SRILM，并在`Config.py`中设置`srilmpath`。默认配置为`srilmpath=./bin/srilm/bin/i686-m64`
1. 下载语料： `./DownloadCorpus.py`
1. 处理语料： `./PurifyCorpus.py`
1. 生成数据： `./GenerateData.py`
1. 训练： `./Train.py`
1. 测试可以有两种：
    * 一种是对着测试集求语言模型的PPL： `./Test.py`
    * 一种是测试若干制定填空题： `./TestExamples`
        输入文件是 `./test.txt`，格式为「题目　选项１　选项２　等等」，其中题目中的空用全角问号「？」表示，题目和选项、选项和选项之间的空格也是全角的。

## 语料之来源

* [维基文库] (https://zh.wikisource.org/wiki/)

## 所使用之工具

* [rnnlm] (http://www.fit.vutbr.cz/~imikolov/rnnlm/) 
* [srilm] (http://www.speech.sri.com/projects/srilm/)
* [word2vec] (https://code.google.com/p/word2vec/)
