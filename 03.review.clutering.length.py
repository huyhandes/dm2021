from helper import *
from concurrent.futures import ThreadPoolExecutor

def distance(a,b,func):
    if isinstance(a,int) and isinstance(b,int):
        return abs(a-b)
    if not isinstance(a,int) and not isinstance(b,int):
        dis = 0
        for x in a:
            for y in b:
                dis = func(dis,abs(x-y))
        return dis
    if isinstance(b,int):
        a,b = b,a
    dis = 0
    for x in b:
        dis = func(dis, abs(a-x))
    return dis
def calculate_distances(cluster_arr):
    for i in range(0,len(cluster_arr)):
        for j in range(0,len(cluster_arr)):
            if i == j:
                yield 0
            else:
                yield distance(cluster_arr[i],cluster_arr[j],max) # change max to min then we got the solution for min mode
sample_documents_size = list(set(sample_documents_size))
while len(sample_documents_size) > 3:
    # calculate all distance
    all_distances = calculate_distances(sample_documents_size)
    # get min distance
    _min = 1e9
    i,j = 0,0
    for id,x in enumerate(all_distances):
        if x < _min:
            if int(id/len(sample_documents_size)) == id%len(sample_documents_size):
                continue
            _min = x
            i = int(id/len(sample_documents_size))
            j = id%len(sample_documents_size)
    #merge 2 cluster i,j
    if isinstance(sample_documents_size[i],int) and isinstance(sample_documents_size[j],int):
        temp = (sample_documents_size[i],sample_documents_size[j])
        sample_documents_size.pop(max(i,j))
        sample_documents_size.pop(min(j,i))
        sample_documents_size.append(temp)
    elif not isinstance(sample_documents_size[i],int) and not isinstance(sample_documents_size[j],int):
        sample_documents_size[i] += sample_documents_size[j]
        sample_documents_size.pop(j)
    else:
        if isinstance(sample_documents_size[i],int):
            sample_documents_size[i], sample_documents_size[j] = sample_documents_size[j], sample_documents_size[i]
        sample_documents_size[i] += (sample_documents_size[j],)
        sample_documents_size.pop(j)
       
for x in sample_documents_size:
    print(x)