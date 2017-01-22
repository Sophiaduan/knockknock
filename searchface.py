import csv
import microface
 
def isInCSV(faceID):
	arr = []
	with open('facesave.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		# print type(faceID), " type of faceid"
		for row in spamreader:
			# print row
			# print type(row)	
			# print len(row)
			if len(row) != 0 and microface.compareall(faceID, row[0]):
				arr.append(row)
	return arr
    
