import sys
import os

def printTheFinalResult():
	for p in range(max1-min1 + 1):
		if (max1-p>=0):
			print(" "+ str(max1-p) + ":\t" , end = "")
		else:
			print(str(max1-p) + ":\t", end = "")
		for q in range(len(list2)-2):
			if list2[q]!=(max1 - p):
				if (list2[q-1]< max1 - p <list2[q]) or (list2[q]< max1 - p <list2[q-1]):
					print(character, end = "")
				else:
					print(" ", end = "")
			else:
				print(character, end = "")
		print()
# check the length of argument
if len(sys.argv)<2:
	print("No score file specified.")
	quit()

#check the file name is valid
if(sys.argv[1][0]=="-"):
	print("No score file specified.")
	quit()

#check path to score file
if(os.path.exists(sys.argv[1])==False):
	print("Invalid path to score file.")
	quit()

list=[]#create an empty list
#start to read the file
with open(sys.argv[1], 'r') as score:#open the first element of the score file
	lines = score.readlines()#read each line of score file
	instrument=lines[0]#the first element in lines is instrument
	list.append(instrument)#assign the instrument to the list
	#print(list)#print list

	isFirstInstrument = True
	list2 = []
	for line in lines:
		# read every line of the score file
		# piano
		# |*****---*****|
		index1=0
		index2=0
		if (line[0].isalpha() == False):#if the firt element is not alphabat
			for line1 in line.strip("|"):
				if index2 > len(list2) - 1:
					list2.append(0)
				if '*' in line1:
					list2[index2] = list2[index2] + list1[index1]
					index1 = index1 + 1
					if index1 > len(list1) - 1:
						index1 = 0
				if '-'  in line1:
					index1 = 0
				index2 =index2 + 1
		else:
			# it is the name of an instrument - 'piano'
			a_dictionary = {}#create a dictionary
			if os.path.exists('./instruments/{}'.format(line.strip("\n"))):
				with open('./instruments/{}'.format(line.strip("\n")), 'r') as myfile:#open the instrument file
					file = []
					for line2 in myfile:
						file.append(line2)#append line in the instrument file
			else:
				print("Unknown source.")
				quit()
			list1=[0]
			for i in file:
				a,b = i.strip("\n").split("\t")
				for j in range(len(b)):
					if j > len(list1) - 1:
						list1.append(0)
					c = b[j]
					if (c!='/') & (c!='-') & (c!='\\'):
						pass
					else:
						list1[j] = int(a)
			#print(list1)
			flags=True
			for h in range(len(sys.argv)):
				if sys.argv[h]=='--total':
					flags=False

			if flags==True:
				if isFirstInstrument == False:
					min1=min(list2)
					max1=max(list2)
					printTheFinalResult()
				list2=[]
				isFirstInstrument = False
				print(line.strip("\n") + ":")
			character="*"
			for d in range(len(sys.argv)):
				if sys.argv[d].startswith("--character="):
					character=sys.argv[d].split("=")[1][0]

	#print(list2)
	if flags==False:
		print("Total:")
	min1=min(list2)
	max1=max(list2)
	printTheFinalResult()
