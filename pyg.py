pyg = 'ay'

original = input('Enter a sentance to translate: ')

def isallcaps(w):
  if (w[0].isupper() or not w[0].isalpha()) and len(w[1:]) > 0:
    return isallcaps(w[1:])
  if (w[0].isupper() or not w[0].isalpha()) and len(w[1:]) == 0:
    return True
  return False

def hasnoletters(w):
  if not w[0].isalpha() and len(w[1:]) == 0:
    return True
  if w[0].isalpha():
    return False
  return hasnoletters(w[1:])

def getpunc(w, a):
  if w[0].isalnum():
    return a
  else:
    return getpunc(w[1:], a + w[0])

def makeallcaps(w):
  if len(w[1:]) > 0:
    return w[0].upper() + makeallcaps(w[1:])
  return w[0].upper()

def piglatinize(o):
  if hasnoletters(o):
    return o
  word = o.lower()
  first= ''
  vowels = ['a', 'e', 'i', 'o', 'u']
  
  start_punc = getpunc(word, '')
  end_punc = getpunc(word[::-1], '')[::-1]
  word = word[len(start_punc):len(word) - len(end_punc)]

  for x in word:
    if len(first) > 0:
      vowels.append('y')
    if x not in vowels:
      first = first + x
      word = word[1:]
    else:
      break

  word = word + first
  
  if o[len(start_punc)].isupper():
    word = word[0].upper() + word[1:]
   
  final_word = start_punc + word + pyg + end_punc

  if isallcaps(o) and len(o) > 1:
    final_word = makeallcaps(final_word)

  return final_word

if len(original) > 0:
  words = original.split()
  piglatin_words = map(piglatinize, words)
  print(' '.join(piglatin_words))
else:
  print('invalid')
