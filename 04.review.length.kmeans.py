from helper import *
from random import randint
sample_documents_size = list(set(sample_documents_size))
cluster_centroids = [randint(min(sample_documents_size),max(sample_documents_size)),randint(min(sample_documents_size),max(sample_documents_size)),randint(min(sample_documents_size),max(sample_documents_size))]
def get_mean(cluster,old_centroids):
    if len(cluster) == 0:
        return old_centroids
    return int(sum(cluster)/len(cluster))
clusters = [(),(),()]
while True:
    cache_centrold = cluster_centroids
    #find group
    clusters = [(),(),()]
    for x in sample_documents_size:
        _dis = float('inf')
        pos = 3
        for i in range(0,3):
            if abs(x-cluster_centroids[i]) < _dis:
                _dis = abs(x-cluster_centroids[i])
                pos = i
        clusters[pos] += (x,)
    #calculate new centroids
    for i in range(0,3):
        cluster_centroids[i] = get_mean(clusters[i],cache_centrold[i])
    if cache_centrold == cluster_centroids:
        break
for cluster in clusters:
    print(cluster)
    