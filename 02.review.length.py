import math

from matplotlib.pyplot import xlabel
from helper import *
import seaborn as sns
#calculate mean
mean = sum(sample_documents_size) / len(sample_documents_size)

#calculate variance
distance = [(x - mean)**2 for x in sample_documents_size]
variance = sum(distance) / len(sample_documents_size)

#calculate standardeviation

std = math.sqrt(variance)
bin_size = 100
print(sample_documents_size)
_min = min(sample_documents_size)
_max = max(sample_documents_size)
pdf = [0] * int((_max - _min + bin_size)/bin_size)
for x in sample_documents_size:
    index = int((x-_min) / bin_size)
    pdf[index] += 1
print(pdf)
x = [i*bin_size for i in range(int((_max-_min+bin_size)/bin_size))]
sns_plot = sns.lineplot(x=x,y=pdf)#,x='Document size',y='counts')
fig = sns_plot.get_figure()
fig.savefig("02.review.length1.png")