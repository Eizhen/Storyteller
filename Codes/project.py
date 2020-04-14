# -*- coding: utf-8 -*-
from hazm import *
import random
import json
import urllib2
import requests
from subprocess import call


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


inp = open("InputStory.txt", 'r').read()
tokens = unicode(inp, "utf-8")
normalizer = Normalizer()
tokens = normalizer.normalize(tokens)
tokens = word_tokenize(tokens)

#print (tokens)

space = ' '

N = 4

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

startngram = []

# or tokens[i-1] == ':' or tokens[i-1] == '"' or  or tokens[i-1] == u'»' or tokens[i-1] == u'«'

for i in range(len(tokens)-N+1):
    if (i-1 >= 0 and (tokens[i-1] == '.' or tokens[i-1] == '!' or tokens[i-1] == u'،' or tokens[i-1] == '.' or tokens[i-1] == u'!' or tokens[i-1] == ',' or tokens[i-1] == u'؟')):
        startngram.append(space.join(tokens[i:i+N]))


text = random.choice(startngram)
#text = random.choice(counts.keys())
i = 0

while i < 30:
    text += space + next_word(text, N, counts);
    i += 1


text += ' .'

outp = open("story.txt", 'w+').write(text.encode('utf-8'))

data = {
    "Text": text,
    "Speaker":"Female1",
    "PitchLevel":"0",
    "PunctuationLevel":"0",
    "SpeechSpeedLevel":"0",
    "ToneLevel":"0",
    "GainLevel":"0",
    "BeginningSilence":"5",
    "EndingSilence":"0",
    "Format":"mp3/32/m",
    "APIKey":"CSHTMX03HCT7JJ7"
}

headers = {'Content-Type': 'application/json'}

sent = ""

for a in text:
    if (a != '.' and a != u'،' and a != u':' and a!= u'؟' and a != u'!'):
        sent += a
    else:
        response = requests.post('http://api.farsireader.com/ArianaCloudService/ReadText', data=json.dumps(data), headers=headers, timeout=120)
        with open('story.wav', 'wb') as output:
            output.write(bytearray(response.content))
        call(["mpg123", "story.wav"])
        sent = ""
