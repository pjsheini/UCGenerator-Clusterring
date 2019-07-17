import io
#from gensim.models import Word2Vec
#from sklearn.decomposition import PCA, KernelPCA
from matplotlib import pyplot
import itertools
import collections
from load import load_words
import vectors as v
from vectors import Vector
from word import Word
#import matplotlib.pyplot as plt
#from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN, OPTICS, cluster_optics_dbscan
import json
import random
import numpy as np
from sklearn import svm  
#import graphlab as gl
from sklearn.cluster import AgglomerativeClustering
if __name__ == "__main__":

	words = load_words("wiki-100k.vec")
	wv = []
	ww= []
	#pca = PCA(n_components=2)
	#pca = KernelPCA(kernel="cosine", fit_inverse_transform=True)
	wv=[w.vector for w in words[500:10500]]
	ww=[w.text for w in words[500:10500]]
	#print(wv)
	#XX = pca.fit_transform(wv)
	#print(XX)
	X = np.array(wv)
	#model = DBSCAN(eps=0.5, min_samples=3).fit(wv)
	#cluster = AgglomerativeClustering(n_clusters= 10000, affinity='cosine', linkage='average')  
	#0.477 - 10000
	#cluster = AgglomerativeClustering(n_clusters= None, distance_threshold = 0.577, affinity='cosine', linkage='average',compute_full_tree = True)

	cluster= OPTICS(min_samples=3 , xi=.04, min_cluster_size=2)  
	cluster.fit_predict(X) 
	#print(model.labels_)
	#print(model.core_sample_indices_)
	##with open("output-labels10kV02.txt",'w') as fout:
		#model.
		##cluster.labels_.tofile(fout,sep=" ",format="%s")
	#with open("output3-cores2.txt",'w') as foutc:
		#model.
		#cluster.core_sample_indices_.tofile(foutc,sep=" ",format="%s")
	ucDic = dict()
	#labels = model.labels_.tolist()
	labels = cluster.labels_.tolist()
	templist = list()
	#with open("wiki-100k-classification5.txt",'w') as fwicls:
	for i in range(1,len(labels)):
		#print(ww[i])
		clss= labels[i]
		if clss == -1 :
			continue
		#print (clss)
		initItem=list()

		if clss not in ucDic or ucDic[clss]== None:
			ucDic[clss] = ww[i]
			#fwicls.write()
			#print (ucDic.items())

		elif ucDic[clss]!= None:
			#print(ucDic[clss])
			print(ww[i]) 
			ucDic[clss] += '; ' + ww[i]
			#print (ucDic[clss])
		else:
			continue
	with open("Computed-UniversalConceptsOptV02.txt",'w') as outuc:
		outuc.write(json.dumps(ucDic))
	Finaldic=dict()

	for key,value in ucDic.items():
		templist = value.split(';')
		Finaldic[key]= random.choice(templist)
	with open("Final-Computed-UniversalConceptsOptV02.txt",'w') as foutuc:
		foutuc.write(json.dumps(Finaldic))
#######################################################################


				#print(ucDic[i])
	#for key, value in ucDic:
		#print (ucDic)
	#sf = sf.unpack('X1')
	#model2 = gl.dbscan.create(sf, radius=0.25, min_core_neighbors=10)
	#print(model2.summary())
	# create a scatter plot of the projection
	#pyplot.scatter(result[:, 0], result[:, 1])
	#ww=[w.text for w in words[:1000000]]
	#words = ww
	#for i, word in enumerate(words):
		#pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
	#pyplot.show()