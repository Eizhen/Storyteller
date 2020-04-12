# -*- coding: utf-8 -*-
from hazm import *


inp = open("story.txt", 'r').read()
tokenize = unicode(inp, "utf-8")
normalizer = Normalizer()
tokenize = normalizer.normalize(tokenize)
tokenize = word_tokenize(tokenize)


naghshinp = open("persian.txt", 'r').read()
ntokenize = unicode(naghshinp, "utf-8")
nnormalizer = Normalizer()
ntokenize = nnormalizer.normalize(ntokenize)
ntokenize = word_tokenize(ntokenize)


outp = open("flexout.txt", 'w')

counter = 0

tokenize = set(tokenize)

for token in tokenize:
    counter = 0
    while counter < len(ntokenize):
        if (ntokenize[counter] == token and counter+1 < len(ntokenize)):
            outp.write((ntokenize[counter] + u" " + ntokenize[counter+1] + u"\n").encode('utf-8'))
            break
        counter += 1




outp.close()


   






