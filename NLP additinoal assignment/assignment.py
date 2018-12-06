from textblob import TextBlob
from textblob import Word
import pandas as pd
import random

noun = pd.read_csv('noun.txt', header = None)
print("TYPE 'exit' ANY TIME TO EXIT THE GAME")

ar = []
for i in range(0, len(noun.iloc[:,0])):
    ar.append(noun.iloc[i,0])

while(True):
    r = random.randint(0, len(noun.iloc[:,0]))
    print('--------------------------------')

    x = noun.iloc[r,0]
    s = raw_input('Enter the PLURAL of ' + x + ' ')

    theWord = Word(x)

    if (s == theWord.pluralize()):
        print('Well Done! You did a good job.')
    elif(s == 'exit'):
        break
    else:
        print('Sorry! Your answer was incorrect.')
        print('The correct answer is: ' + '"' + theWord.pluralize() + '"')

    r = random.randint(0, len(noun.iloc[:,0]))
    print('--------------------------------')
    x = noun.iloc[r,0]
    theWord = Word(x)
    y = theWord.pluralize()
    s = raw_input('Enter the SINGULAR of ' + y + ' ')

    if (s == x):
        print('Well Done! You did a good job.')
    elif(s == 'exit'):
        break
    else:
        print('Sorry! Your answer was incorrect.')
        print('The correct answer is: ' + '"' + x + '"')
