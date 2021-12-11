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

sns_plot = sns.histplot(data=sample_documents_size,kde=True)#,x='Document size',y='counts')
fig = sns_plot.get_figure()
fig.savefig("02.review.length.png")