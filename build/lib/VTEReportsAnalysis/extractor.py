import nltk
import nltk.data
from nltk.tokenize import sent_tokenize
from .findMatch import horspool_match
from .negex import *
import pkg_resources

#initilazation for config files
resource_package = 'VTEReportsAnalysis'
resource_path = '/'.join(('config','negex_triggers.txt'))
path = pkg_resources.resource_filename(resource_package, resource_path)


# initilazation for negex.py
rfile = open(path)
irules = sortRules(rfile.readlines())


#------NLTK sentence split start-----#
'''
def splitSentence(paragraph):
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	sentences = tokenizer.tokenize(paragraph)
	return sentences 
'''
# NLTK not fully supported by iCARE
#------NLTK sentence split end-----#


#------naive sentence split start-----#
def splitSentence(paragraph):
	sentences = []
	for sentence in paragraph.split('.'):
		if '!' in sentence:
			sentences.extend(sentence.split('!'))
		elif ':' in sentence:
			sentences.extend(sentence.split(':'))
		else:
			sentences.append(sentence)
	return sentences

#------word tokeniztion function-----#
def tokenize(sentence):
	word = (re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", sentence))
	return word


#------Main Function-----#
class reExtractor:
	def __init__(self, target, skip, absolute_negative, absolute_positive, start):
		self.target = target
		self.skip = skip
		self.absolute_positive = absolute_positive
		self.absolute_negative = absolute_negative
		self.start = start
	'''
	def test(self):
		print(self.target)
	'''
	def processing(self,text1):
		text = text1
		for phrase in self.start:
			temp = horspool_match(phrase,text)
			if temp != -1:
				text = text[temp:]

		#------preprocessing-----#
		text = text.lower()
		text = text.replace('-',' ')
		text = text.replace('?DVT',' ')
		text = text.replace('? DVT',' ')

		'''
		#------abondoned from v2.01-----#
		for phrase in self.absolute_negative:
			temp = horspool_match(phrase,text)
			if temp != -1:
				#print(phrase,text)
				return -99,-99
		'''		
		sentences = splitSentence(text)
		sentenceTagged = []   #  list of tagged sentences
		presentCount = 0   #  positive VTE sentences 
		absentCount = 0	   #  negative VTE sentences 
		doubleNegFlag = 0    #  doulbe negations flag

		for sentence in sentences:

			present = 0   #  temporary positive sentence count

			mark = 0    # temporary status flag

			'''
			#------skip function-----#
			#------abondoned from v2.02-----#
			for phrase in self.skip:
				temp = horspool_match(phrase,sentence)
				if temp != -1:  # -1 is 404 not found
					mark = 1
			if mark == 1:		# 'skip' found, so skip this sentence
				continue
			mark = 0
			'''

			markW = ''   # temporary words memory

			words = tokenize(sentence)
			for phrase in self.target:      #  word tokeniztion
				if phrase in words:
					mark = 1
					markW = phrase  # temporary words = target pharse
					break

			if mark == 0:		# 'target' not found, skip this sentence
				phrase = 'filling defects'
				temp = horspool_match(phrase,sentence)
				if temp != -1:
					mark = 1
					markW = phrase  # temporary words = target pharse
				else:
					phrase = 'filling defect'
					temp = horspool_match(phrase,sentence)
					if temp != -1:
						mark = 1
						markW = phrase  # temporary words = target pharse
						
			if mark == 1:		# 'target' found, so check negation
				tagger = negTagger(sentence, phrases = [markW], rules = irules, negP=False) 
				sentenceTagged.append(tagger.getNegTaggedSentence())   #  add returned tagged sentence into list
				negexResult = tagger.getNegationFlag()
				doubleNegFlag = tagger.getDouble()
				if negexResult == 'affirmed':     # negation not found
					present = 1
				elif negexResult == 'negated':    # negation found
					present = -1           
			if present == 1:
				presentCount += 1
			elif present ==-1:
				absentCount += 1
			else:
				pass
		return presentCount, absentCount,sentenceTagged,doubleNegFlag
