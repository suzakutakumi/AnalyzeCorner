import re,sys # Regular Expression Operation https://docs.python.org/ja/3/library/re.html
from enum import IntEnum

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
def AnalysisOfWhatCorner(s):
  m=re.search(r'_ (?:the|a|an|The|A|An) ([a-zA-Z]+) corner',s)
  if m!=None:
    return m
  m=re.search(r'_ (?:the|The) corner of(?: the| a| an|) ([a-zA-Z]+)',s)
  if m!=None:
    return m
  m=re.search(r'_ (?:the|The) corner',s)
  return m

# Determine if what goes into _ is in, or, or on.
def AnalyzeCorner(sentence):
  cornerThings=AnalysisOfWhatCorner(sentence)

  if cornerThings==None:
    print("Text is not match!")
    return []

  if len(cornerThings.groups())<1: # When there is nothing behind "_ the corner"
    print("It is not clearly stated what the corner is.")
    return ["at"]
  cornerThing=cornerThings.group(1)
  print(cornerThing)

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
