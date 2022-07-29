from enum import IntEnum
import nltk  # Reference: https://qiita.com/m__k/items/ffd3b7774f2fde1083fa

class KindCronerThing(IntEnum):
  Space=0
  NoOutsideSpace=1
  SmallThing=2
  SurfaceThing=3

  @staticmethod
  def GetThings(num):
    lists=[['building', 'bank', 'room', 'box', 'house', 'window', 'classroom'],
     ['room', 'classroom', 'window'],
     ['tofu', 'eraser', 'block'],
     ['intersection', 'square', 'street']
    ]
    return lists[num]

# Determine what the corner is.
def AnalysisOfWhatCorner(text):
  words=nltk.word_tokenize(text)  # Separate sentences into words.
  tags=nltk.pos_tag(words)  # Attach a POS tag to each word.
  if '_' not in words:
    return ['?']
  n=words.index('_')  # Find the number of in/on/at position in a word.

  # Check for "the corner" after the underscore.
  if tags[n+1][0]!='the' or tags[n+2][0]!='corner':
    return None

  # Ignore the words between "corner" and "of".
  n+=3
  l=len(tags)
  while n<l and tags[n][0] not in ['of','.','?']:
    n+=1
  
  # If program don't know what corner it is, return ''.
  if n>=l or tags[n][0] in ['.','?']:
    return ''
  n+=1

  # Ignore modifiers between "of" and "what the corners point to".
  while n<l and tags[n][1] in ['JJ','JJR','JJS','DT']:
    n+=1
  while n+1<l and tags[n+1][1]=='NN':
    n+=1
  return tags[n][0]

# Determine if what goes into _ is in, or, or on.
def AnalyzeCorner(sentence):
  cornerThing=AnalysisOfWhatCorner(sentence)

  if cornerThing==None:
    print("Text is not match!")
    return ["?"]

  if cornerThing=='': # When there is nothing behind "_ the corner"
    print("It is not clearly stated what the corner is.")
    return ["at"]

  spaces=KindCronerThing.GetThings(KindCronerThing.Space)
  noOutsideSpaces=KindCronerThing.GetThings(KindCronerThing.NoOutsideSpace)
  smallThings=KindCronerThing.GetThings(KindCronerThing.SmallThing)
  surfaceThings=KindCronerThing.GetThings(KindCronerThing.SurfaceThing)

  if cornerThing in spaces: # When the corner thing has space
    if cornerThing in noOutsideSpaces: # When the corner thing has no outside
        return ["in"]
    return ["in","at"]
  if cornerThing in smallThings: # When the corner thing is small
    return ["on"]
  if cornerThing in surfaceThings: # When the corner thing is a surface
    return ["on"]
  return ["at"]

if __name__=="__main__":
  text=input()
  print(AnalyzeCorner(text))