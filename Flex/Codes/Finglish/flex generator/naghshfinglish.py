# -*- coding: utf-8 -*-
from openpyxl import *
from hazm import *

entries=load_workbook(filename='Entries.xlsx')
entriesrange =entries['Entries']

inp = open("flexout.txt", 'r').read()
tokenize = unicode(inp, "utf-8")
normalizer = Normalizer()
tokenize = normalizer.normalize(tokenize)
tokenize = word_tokenize(tokenize)

outp = open("naghshfinglish.txt", 'w')

for token in tokenize:
    found=False
    finglish = u""
    word = u""
    match = u""
    if ((token[0]<=u'z'and token[0]>=u'a') or (token[0]>=u'A'and token[0]<=u'Z')):
#{yylval.v_pp = strdup(yytext); return V_PP; }
        outp.write("{yylval." + token.lower() + u" = strdup(yytext); return " + token + u"; }\n")
        continue
    else:
        for row in range(41, 38385):
            match=entriesrange['B'+str(row)].value
            if  (match==token):
                found=True
                match=entriesrange['A'+str(row)].value
                word = entriesrange['A'+str(row)].value
                break
        if (found == False):
            word = token
  #          outp.write((u"/" + word + u"/ ").encode('utf-8'))

        counter=0
        while counter<len(word):
         #   print(counter)
            if (word[counter]==u'@'):
                finglish+=u'a'
            if ((word[counter]<=u'z'and word[counter]>=u'a') or (word[counter]>=u'A'and word[counter]<=u'Z')):
                finglish+=word[counter]
            if (word[counter]==u'و'):
                if(counter >= 1 and counter < (len(word)-1) and word[counter-1]!=u'o' and word[counter+1]!=u'o' and word[counter-1]!=u'u' and word[counter+1]!=u'u' ):
                    finglish+=u'v'
            if (word[counter]==u'ت' or word[counter]==u'ط'):
                finglish+=u't'
            if (word[counter]==u'ز' or word[counter]==u'ظ' or word[counter]==u'ض' or word[counter]==u'ذ'):
                finglish+=u'z'
            if (word[counter]==u'س' or word[counter]==u'ث'or word[counter]==u'ص'):
                finglish+=u's'
            if (word[counter]==u'ش'):
                finglish+=u'sh'
            if (word[counter]==u'ق' or word[counter]==u'غ'):
                finglish+=u'gh'
            if (word[counter]==u'پ'):
                finglish+=u'p'
            if (word[counter]==u'ف'):
                finglish+=u'f'
            if (word[counter]==u'ی' ):
                finglish+=u'i'
            if (word[counter]==u'ه' or word[counter]==u'ح'):
                finglish+=u'h'
            if (word[counter]==u'خ'):
                finglish+=u'kh'
            if (word[counter] == u'ج'):
                finglish+=u'j'
            if (word[counter] == u'ب'):
                finglish+=u'b'
            if (word[counter] == u'ل'):
                finglish+=u'l'
            if (word[counter]==u'ن'):
                finglish+=u'n'
            if (word[counter] == u'م'):
                finglish+=u'm'
            if (word[counter] == u'ک'):
                finglish+=u'k'
            if (word[counter] == u'گ'):
                finglish+=u'g'
            if (word[counter] == u'ر'):
                finglish+=u'r'
            if (word[counter] == u'د'):
                finglish+=u'd'
            if (word[counter] == u'چ'):
                finglish+=u'ch'
            if (word[counter] == u'ژ'):
                finglish+=u'zh'
            if(word[counter]==u'آ'):
                finglish+=u'A'
            if(word[counter]==u'ا' and len(finglish)>=1 and finglish[len(finglish)-1]!=u'a' ):
                finglish+=u'a'
            if(word[counter]<=u'?' and word[counter]>=u'!'):
                finglish+=word[counter]
            if(word[counter]==u'،'):
                finglish+=u'،'
            counter+=1


        outp.write((finglish + u" ").encode('utf-8'))

outp.close()


   






