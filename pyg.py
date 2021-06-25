original = input('Enter a sentance to translate: ')

def isallcaps(word):
  if (word[0].isupper() or not word[0].isalpha()) and len(word[1:]) > 0:
    return isallcaps(word[1:])
  if (word[0].isupper() or not word[0].isalpha()) and len(word[1:]) == 0:
    return True
  return False

def hasnoletters(word):
  if not word[0].isalpha() and len(word[1:]) == 0:
    return True
  if word[0].isalpha():
    return False
  return hasnoletters(word[1:])

def getpunc(word, acc):
  if word[0].isalnum():
    return acc
  else:
    return getpunc(word[1:], acc + word[0])

def makeallcaps(word):
  if len(word[1:]) > 0:
    return word[0].upper() + makeallcaps(word[1:])
  return word[0].upper()

def pygize(word, acc):
  vowels = 'aeiou'
  if len(acc) > 0:
    vowels = vowels + 'y'
  if word[0] not in vowels:
    return pygize(word[1:], acc + word[0])
  return word + acc + 'ay'

def handlepygization(original):
  if hasnoletters(original):
    return original
  word = original.lower()
  
  start_punc = getpunc(word, '')
  end_punc = getpunc(word[::-1], '')[::-1]
  word = word[len(start_punc):len(word) - len(end_punc)]
  
  pygd = pygize(word, '')
  
  if original[len(start_punc)].isupper():
    pygd = pygd[0].upper() + pygd[1:]
   
  final_word = start_punc + pygd + end_punc

  if isallcaps(original) and len(original) > 1:
    return makeallcaps(final_word)

  return final_word

if len(original) > 0:
  words = original.split()
  piglatin_words = map(handlepygization, words)
  print(' '.join(piglatin_words))
else:
  print('invalid')
