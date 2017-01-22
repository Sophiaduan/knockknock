import csv

def saveface(name, id):
	node2 = dict()
	data = [str(id)]
	with open (r'facesave.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(data+[str(name)])

