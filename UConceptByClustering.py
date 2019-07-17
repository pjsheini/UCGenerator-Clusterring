import itertools
import copy
import pandas as pd
import matplotlib.pyplot as plt
import random
import uuid
import json
import randomcolor

def genUniversalConcepts(graph,rem):
	

	with open('UniConceptClusteringENES50k.txt', 'w',encoding='utf8') as outfile:

		while rem:
			output={}
			#rin = random.randint(0,len(rem))
			output['UC_Nodelist'] = []
			output['UC_edgelist']=[]
			output['GUID'] = []
			output['color']= []

			rinp = random.choice(rem)
			bfsList = list(nx.bfs_tree(graph,rinp))
			bfsEdges = list(nx.bfs_edges(graph,rinp))

			output['UC_Nodelist'].append(bfsList)
			output['UC_edgelist'].append(bfsEdges)
			output['GUID'].append(uuid.uuid4().hex)
			output['color'].append(rand_color.generate())
			print (rand_color.generate())
			for j in bfsList:
				rem.remove(j)

			print("the tree constructed from of a breadth-first-search is:\n")
			print(bfsList)
			json.dump(output, outfile, ensure_ascii=False)
			outfile.write('\n')



if __name__ == '__main__':


	rand_color = randomcolor.RandomColor()
	rem = nl
	genUniversalConcepts(gr,rem)

	#infoGraph(gr);
	#drawgraph(gr,"UC-NwpV01.txt")
	








