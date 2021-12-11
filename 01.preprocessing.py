import re
from pprint import pprint
import math
from helper import *
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