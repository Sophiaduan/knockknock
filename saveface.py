import pandas as pd
import numpy as np 
import math
import csv

def saveface(name, id):
        node2 = dict()
        data = [str(name)]
        
        with open (r'facesave.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(data+[str(id)])

