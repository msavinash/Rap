import pickle
from pprint import pprint

inputFile = "phoneticsData.txt"
# inputFile = "phoneticsDataSample.txt"

outputFile = "phoneticsData.pkl"
# d = {}

def buildData(inputFile, outputFile):
	d = {}
	with open(inputFile) as f:
		data = f.readlines()
		for i in data:
			word, phonetic = i.split("  ")
			phonetic = phonetic.split(" ")[::-1]
			# print(phonetic, word)
			tmpData = d
			for j in phonetic:	
				if j not in tmpData:
					tmpData[j] = {}
				tmpData = tmpData[j]
			if "leavesList" in tmpData:
				tmpData["leavesList"].append(word)
			else:
				tmpData["leavesList"] = [word]
		with open(outputFile, "wb") as f:
			pickle.dump(d, f)


def getData():
	d = None
	with open("phoneticsData.pkl", "rb") as f:
		d = pickle.load(f)
	return d


d = getData()
pprint(d)

# buildData(inputFile, outputFile)


# key = list(d.keys())[0]
# tmpD = d
# while 1:
# 	print(key)
# 	if "leavesList" in tmpD:
# 		break
# 	print(key)
# 	# print("\n"*3)
# 	key = list(tmpD.keys())[0]
# print(tmpD[key])

# buildData(inputFile, outputFile)
