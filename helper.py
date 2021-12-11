from json import loads
sample_documents = []
sample_documents_size = []
stop_words = None
common_words = None
with open('samples.json','r') as f:
    for line in f.readlines():
        data = loads(line)
        sample_documents.append(data['text'])
        sample_documents_size.append(len(data['text']))
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