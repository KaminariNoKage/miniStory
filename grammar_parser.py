import random, math

class GrammarNode(object):
	def __init__(self,name,values=[]):
		self.name = name
		self.values = values
	'''def __str__(self):
		endStr = ''
		for val in self.values:
			for v in val:
				endStr += ' '+ str(v)
			endStr += '.'	#Breaks different blocks
		return self.name+ '('+endStr+')'
		'''

	def get_sub(self):
		#TO DO: make non-random
		endStr = ''
		rand = math.floor(len(self.values) * random.random())
		random_selection = self.values[int(rand)]
		for s in random_selection:
			#If a grammar node, then pass down the tree
			if type(s) is GrammarNode:
				endStr += s.get_sub()
			else:
				endStr += s+' '
		return endStr


class Grammar(object):
	def __init__(self,fname='sentence.txt'):
		'''
			fname = file name
			Initializes grammar object
		'''
		self.data = {}
		self.grammar_get(fname)	#Extract the tree variables
		self.map_tree()	#Set up the tree structure

	def __str__(self):
		nuStr = ''
		for key in sentence.data:
			nuStr += str(sentence.data[key]) +'\n'
		return nuStr

	def grammar_get(self,fname):
		'''
			fname = file name
			Parses out the structure of a grammar tree based on input file
		'''
		fopen = open(fname,'r')	#Open grammar file and get lines
		ftext = fopen.read().replace('\n','').replace('\t','')	#Compress to one line if not already
		startNu = True	#Keeps track of whether to start new tree
		curBlock = ''	#Name of the current block
		curString = ''	#Keeps track of current string
		subBlock = []

		for char in ftext:
			if char == '{':
				curBlock = curString.strip(' ') #Store in block (to be used as key later)
				curString = ''
			elif char == '}':
				self.data[curBlock] = GrammarNode(curBlock, subBlock) #plug in data
				startNu = True	#Start a new block
				curBlock = ''	#Set the new block name to fill in
				subBlock = []	#Set new data for block
			elif char == ';':
				subBlock.append(curString)	#Save the last string
				curString = ''
				startNu = False
			else:
				#Default, add siggy to curString and continue
				curString += char

	def map_tree(self):
		'''
			key = String indicating what key to map
			Replaces things
		'''
		tree = []
		for k in self.data:
			obj = self.data[k]	#Get the object
			for val in range(len(obj.values)):
				#Split the phrase
				phrase = obj.values[val].split(' ')
				for p in range(len(phrase)):
					#If the phrase word is a key
					if '[' in phrase[p] and ']' in phrase[p]:
						#Point it to the object in the main data
						phrase[p] = self.data[phrase[p].replace('[','').replace(']','')]
				#Update the object
				obj.values[val] = phrase


sentence = Grammar()
for r in range(10):
	print sentence.data['S'].get_sub()