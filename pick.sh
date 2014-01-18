
#pool="以 和 而 故 之 不 也 其 者 為"
pool="以"

mkdir -p pick

cat data/purified_corpus.rnnlm.test.human.txt | awk '{ print length($1) " " $0; }' | sort -n | uniq | grep '以' > ./pick/以.txt
cat data/purified_corpus.rnnlm.test.human.txt | awk '{ print length($1) " " $0; }' | sort -n | uniq | grep '和' > ./pick/和.txt
cat data/purified_corpus.rnnlm.test.human.txt | awk '{ print length($1) " " $0; }' | sort -n | uniq | grep '而' > ./pick/而.txt
cat data/purified_corpus.rnnlm.test.human.txt | awk '{ print length($1) " " $0; }' | sort -n | uniq | grep '故' > ./pick/故.txt
cat data/purified_corpus.rnnlm.test.human.txt | awk '{ print length($1) " " $0; }' | sort -n | uniq | grep '之' > ./pick/之.txt
cat data/purified_corpus.rnnlm.test.human.txt | awk '{ print length($1) " " $0; }' | sort -n | uniq | grep '不' > ./pick/不.txt
cat data/purified_corpus.rnnlm.test.human.txt | awk '{ print length($1) " " $0; }' | sort -n | uniq | grep '也' > ./pick/也.txt
cat data/purified_corpus.rnnlm.test.human.txt | awk '{ print length($1) " " $0; }' | sort -n | uniq | grep '其' > ./pick/其.txt
cat data/purified_corpus.rnnlm.test.human.txt | awk '{ print length($1) " " $0; }' | sort -n | uniq | grep '者' > ./pick/者.txt
