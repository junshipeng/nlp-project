
# Corpus : books from Wikisource (Tranditional Chinese)
# commented out are these downloaded

# books = [ '史記', '漢書', '後漢書' , '三國志' , '晉書', '宋書', '魏書', '隋書', '舊唐書', '新唐書', ]
books = [
####儒家
'論語',
'孟子',
'禮記',
'荀子',
'說苑',
'春秋繁露',
'韓詩外傳',
'大戴禮記',
'新書',
'新序',
'孔子家語',
'潛夫論',
'論衡',
'風俗通義',
'孔叢子',
'申鑒',
'新語',
'蔡中郎集',
####墨家
'墨子',
####道家
'莊子',
'列子',
'文子',
'鬻子',
'老子河上公章句',
####法家
'韓非子',
'商君書',
'管子',
####名家
'公孫龍子',
####史書
'史記',
'逸周書',
'國語',
'吳越春秋',
'越絕書',
'戰國策',
'鹽鐵論',
'列女傳',
'春秋穀梁傳',
'春秋公羊傳',
'漢書',
'前漢紀',
'東觀漢記',
'後漢書',
'竹書紀年',
'穆天子傳',
'西京雜記',
]

# Maximum number of chars
dict_size = 10000

# data partition
train_portion = 0.8
valid_portion = 0.1
test_portion = 0.1
#train_size = 1200000
#valid_size =  200000
#test_size  =  200000

# bin path
word2vecpath='./bin/word2vec'
srilmpath='./bin/srilm/bin/i686-m64'
rnnpath='./bin/rnnlm'
temp='./temp'

# data
word2vectrainfile='./data/purified_corpus.word2vec.train.txt'
trainfile='./data/purified_corpus.rnnlm.train.txt'
validfile='./data/purified_corpus.rnnlm.valid.txt'
testfile='./data/purified_corpus.rnnlm.test.txt'

# model
word2vecmodel='./models/purified_corpus.model.word2vec.txt'
rnnmodel='./models/purified_corpus.model.hidden100.class100.txt'

# rnn parameters
hidden_size=100
class_size=100
bptt_steps=4
lambda_value=0.8

