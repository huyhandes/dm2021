import re
from pprint import pprint
import math
from json import loads
sample_documents = []
with open('samples.json','r') as f:
    for line in f.readlines():
        data = loads(line)
        sample_documents.append(data['text'])
    f.close()
with open('stop_words.txt','r') as f:
    stop_words = f.readlines()
    for i,word in enumerate(stop_words):
        stop_words[i] = word.strip()
    stop_words = set(stop_words)
    f.close()
with open('common_words.txt','r') as f:
    common_words = f.readlines()
    for i,word in enumerate(common_words):
        common_words[i] = word.strip()
    common_words = set(common_words)
    f.close()
for i,document in enumerate(sample_documents):
    #remove punctuations
    document = re.sub(r'[^\w\s]', '', document)
    # lower case
    document = document.lower()
    #remove all redundance space, remove stop and common words.
    document = ' '.join( [x for x in document.split() if (x not in stop_words) and (x not in common_words)])
    sample_documents[i] = document

#calculate word_count and tf
word_counts_total = {}
tf = {}
for index,document in enumerate(sample_documents):
    tf[index] = {}
    for word in document.split():
        tf[index][word] = 1 if word not in tf[index] else (tf[index][word] + 1)
        word_counts_total[word] = 1 if word not in word_counts_total else (word_counts_total[word]+1)
#calculate idf
idf = {}
for word in word_counts_total:
    count = 0
    for index,document in enumerate(sample_documents):
        if word in tf[index]:
            count += 1
    idf[word] = math.log(len(sample_documents)/count)
#calculate tf_idf, tf-idf = tf(w,d) * idf(w)
tf_idf = {}
for index,document in enumerate(sample_documents):
    tf_idf[index] = {}
    for word in word_counts_total:
        if word not in tf[index]:
            continue
        tf_idf[index][word] = tf[index][word] * idf[word]
pprint(tf_idf)