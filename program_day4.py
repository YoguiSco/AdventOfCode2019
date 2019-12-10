MAX_DIGIT = 9
MIN_DIGIT = 0
NUMBER_DIGIT = 6

def notDecrease(value):
  prev_i = str(MIN_DIGIT)
  for i in str(value):
    if (i < prev_i):
      return False
    else:
      prev_i = i
  return True

def sizeDigitNumber(value,numberToHave=NUMBER_DIGIT):
  return((len(str(value))==numberToHave))

def twoSameDigit(value):
  prev_i = str(MIN_DIGIT)
  positionInValue = 0
  for i in str(value):
    positionInValue += 1
    if (i == prev_i):
      return True,i,positionInValue
    else:
      prev_i = i
  return False,0,0

def onlyTwoSameDigit(value):
  prev_i = str(MIN_DIGIT)
  for i in str(value):
    if (i == prev_i):
      if(str(value).count(i)==2):
        return True
    else:
      prev_i = i
  return False

def moreThanTwoSameDigit(value):
  prev_i = str(MIN_DIGIT)
  memorized_i = str(MIN_DIGIT)
  for i in str(value):
    if(i==memorized_i):
      return True
    if(i==prev_i):
      memorized_i = i
    prev_i = i
  return False

####DAY4 part1####
# valuesInputs = 168630
# result = 0
# while(valuesInputs<718098):
#   #need double
#   haveTwoDigit, twoDigitNumber, twoDigitPosition = twoSameDigit(valuesInputs)
#   if( (haveTwoDigit == True) and (notDecrease(valuesInputs))):
#     #if double is 1 the following never notDecrease
#     if( (twoDigitNumber == '1')):
#       if(notDecrease(valuesInputs[twoDigitPosition:])):
#         result += 1
#     else:
#       result +=1
#   valuesInputs+=1
# print(result)

####DAY4 part2####
valuesInputs = 168630
result = 0
while(valuesInputs<718098):
  if( (onlyTwoSameDigit(valuesInputs) == True) and (notDecrease(valuesInputs))):
    #if they are more than two following digit 
    result +=1
  valuesInputs+=1
print(result)
