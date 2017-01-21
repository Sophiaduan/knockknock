import csv
import microface
 
def isInCSV(faceID):
    with open('facesave.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if microface.compareall(faceID, row[1]):
                return row
    return None
    
