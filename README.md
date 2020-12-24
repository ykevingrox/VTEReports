# VTEReports

Rewrite Perl code from [Int J Med Inform. 2017 May;101:93-99. doi: 10.1016/j.ijmedinf.2017.02.011. Epub 2017 Feb 21.][http://iturrate.com/simpleNLP/] in Python 3. 

1.simpleNLP.pl --> simpleNLP.py
2.Lingua: DxExtractor --> extractor.py
3.Lingua: Negex --> negex.py

Changes has been made.

The implementation of Negex is taken from [chapmanbe][https://github.com/chapmanbe/negex/tree/master/negex.python]

#Usage

'''
pip install VTEReportsAnalysis
'''


'''
from VTEReportsAnalysis import extraction

extracion('not found')
'''


*Version 1.02
	-Remove NLTK dependency
*version 1.03
	-bugs fixed
*Version 1.04
	-bugs fixed
*Version 1.05
	-Add 60 more “absolute negative” expressions
*Version 1.06
	-bug fixed
*Version 1.07
	-Add word tokenization function
	-Use text.find() instead of the horsepool algorithm
*Version 1.08
	-Move text.lower() function to the start of the extractor, change “start phrase” to lower case
*Version 1.09
	-Change “start” phrase back to capital case
*Version 2.1
	-Remove “absolute negative” phrases, remove “finding” from start phrase 
*Version 2.02
	-Remove “skip” phrases