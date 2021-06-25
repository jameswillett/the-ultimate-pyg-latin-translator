original = input('Enter a sentance to translate: ')

def is_all_caps(word):
  if (word[0].isupper() or not word[0].isalpha()) and len(word[1:]) > 0:
    return is_all_caps(word[1:])
  if (word[0].isupper() or not word[0].isalpha()) and len(word[1:]) == 0:
    return True
  return False

def has_no_letters(word):
  if not word[0].isalpha() and len(word[1:]) == 0:
    return True
  if word[0].isalpha():
    return False
  return has_no_letters(word[1:])

def get_punctuation(word, acc):
  if word[0].isalnum():
    return acc
  else:
    return get_punctuation(word[1:], acc + word[0])

def make_all_caps(word):
  if len(word[1:]) > 0:
    return word[0].upper() + make_all_caps(word[1:])
  return word[0].upper()

def pygize(word, acc):
  vowels = 'aeiou'
  if len(acc) > 0:
    vowels = vowels + 'y'
  if word[0] not in vowels:
    return pygize(word[1:], acc + word[0])
  return word + acc + 'ay'

def handle_pygization(raw):
  if has_no_letters(raw):
    return raw
  word = raw.lower()
  
  start_punc = get_punctuation(word, '')
  end_punc = get_punctuation(word[::-1], '')[::-1]
  word = word[len(start_punc):len(word) - len(end_punc)]
  
  pygd = pygize(word, '')
  
  if raw[len(start_punc)].isupper():
    pygd = pygd[0].upper() + pygd[1:]
   
  final_word = start_punc + pygd + end_punc

  if is_all_caps(raw) and len(raw) > 1:
    return make_all_caps(final_word)

  return final_word

if len(original) > 0:
  words = original.split()
  piglatin_words = map(handle_pygization, words)
  print(' '.join(piglatin_words))
else:
  print('invalid')
