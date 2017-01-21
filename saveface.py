import pandas as pd
import numpy as np 
import math
import csv
node2 = dict()

data = ["I am the best"]
indentify = False
##if node2 == None:
##	new_node = pd.DataFrame.from_dict(node2, orient = 'index')
##	new_node.to_csv('facesave.csv')

with open (r'facesave.csv', 'a') as f:
	if indentify == False:
		writer = csv.writer(f)
		writer.writerow(data+["Sophia"])
		#writer.writerow(["Sophia"])

