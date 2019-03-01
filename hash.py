import numpy as np
import itertools
import random


class HashCode(object):
    def __init__(self, option):
        self.slides = 0
        self.raw_input = []
        self.workingArea = []
        self.parsedInput = []

        if option == "a":
            self.open_file("a_example.txt")
        elif option == "b":
            self.open_file("b_lovely_landscapes.txt")
        elif option == "c":
            self.open_file("c_memorable_moments.txt")
        elif option == "d":
            self.open_file("d_pet_pictures.txt")
	elif option == "e":
            self.open_file("e_shiny_selfies.txt")

        self.slides = self.raw_input[0].split(" ")
        self.workingArea = self.raw_input[1:]
        for i in range(len(self.workingArea)):
            self.parsedInput.append(self.workingArea[i].split(" ")[0:2])
            self.parsedInput[i].append(self.workingArea[i].split(" ")[2:])

        self.workingArea = np.array(self.workingArea) 

    def open_file(self, filename):
        file = open(filename, "r")
        for line in file:
            self.raw_input.append(line.split("\n")[0])
	
		
    def run(self):
	
	outputH = []
	outputV = []
        data = self.raw_input[1:]
	#print data
	for line in data:
		if "H" in line:
			outputH.append(data.index(line))
		else:
			outputV.append(data.index(line))
			
	#print(outputH)
	#print(outputV)
	
	vGrouped = []
	for i in range(0, len(outputV),2):
            vGrouped.append([outputV[i], outputV[i+1]])

	size = len(vGrouped) + len(outputH)
	print(size)

	random.shuffle(outputH)
	random.shuffle(vGrouped)

    #Change text file per desired test
	with open("e.txt", 'w') as f:
		f.write("%s\n" % size)
		for item in vGrouped:
			f.write("%s " % item[0])
			f.write("%s\n" % item[1])
		for item in outputH:
			f.write("%s\n" % item)
	f.close()
	
			
		


if __name__ == "__main__":
    #Change what text file will be read in
    sess = HashCode("e")
    sess.run()

# End File

