# -*- coding: utf-8 -*-
from hazm import *
import random

def next_word(text, N, counts):
    token_seq = space.join(text.split()[-(N-1):])
    choices = counts[token_seq].items()


    total = sum(weight for choice, weight in choices)
    r = random.uniform(0, total)
    upto = 0
    for choice, weight in choices:
        prob = open("prob.txt", 'a+').write(choice.encode('utf-8')+"#  " + str(weight) + "\n" ) 
        upto += weight
        if upto > r:
            return choice
    assert False


inp = open("Deltora.txt", 'r').read()
tokens = unicode(inp, "utf-8")
normalizer = Normalizer()
tokens = normalizer.normalize(tokens)
tokens = word_tokenize(tokens)

#print (tokens)

space = ' '

N = 5

ngrams = []

for i in range(len(tokens)-N+1):
    ngrams.append(tokens[i:i+N])

counts = {}
for ngram in ngrams:
    token_seq = space.join(ngram[:-1])
    last_token = ngram[-1]

    if token_seq not in counts:
        counts[token_seq] = {}

    if last_token not in counts[token_seq]:
        counts[token_seq][last_token] = 0

    counts[token_seq][last_token] += 1

text = random.choice(counts.keys())
i = 0

while i < 100:
    text += space + next_word(text, N, counts);
    i += 1


text += ' .'

outp = open("story.txt", 'w+').write(text.encode('utf-8'))

