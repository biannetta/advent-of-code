puzzleInput="52-75,71615244-71792700,89451761-89562523,594077-672686,31503-39016,733-976,1-20,400309-479672,458-635,836793365-836858811,3395595155-3395672258,290-391,5168-7482,4545413413-4545538932,65590172-65702074,25-42,221412-256187,873499-1078482,118-154,68597355-68768392,102907-146478,4251706-4487069,64895-87330,8664371543-8664413195,4091-5065,537300-565631,77-115,83892238-83982935,6631446-6694349,1112-1649,7725-9776,1453397-1493799,10240-12328,15873-20410,1925-2744,4362535948-4362554186,3078725-3256936,710512-853550,279817-346202,45515-60928,3240-3952"

def createTuple(text):
  lowEnd,highEnd = text.split('-')
  return [int(lowEnd),int(highEnd)]

def isInvalidID(id):
  textId = str(id)
  if len(textId) % 2 == 0:
    midPoint = len(textId) // 2
    if textId[0:midPoint] == textId[midPoint:]:
      print(id)
      return id
    else:
      return 0
  else:
    return 0
    
ranges = map(createTuple, puzzleInput.split(','))

sumOfIDs = 0
for tuple in ranges:
  for id in range(tuple[0],tuple[1]+1):
    sumOfIDs += isInvalidID(id)

print(sumOfIDs)