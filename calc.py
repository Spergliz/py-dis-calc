import math
# input
numA2 = float(input("enter X2 "))
numA1 = float(input("enter X1 "))
numB2 = float(input("enter Y2 "))
numB1 = float(input("enter Y1 "))

# process
NumA= numA2 - numA1
NumB= numB2 - numB1
if NumA or NumB < 0:
 NumA or NumB* -1

 AFNumA = NumA * NumA
 AFNumB = NumB * NumB
 NFNum = AFNumA + AFNumB
 print("the distance between is " + str(math.sqrt(NFNum)))