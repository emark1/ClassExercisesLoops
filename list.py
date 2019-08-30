numberList = [1,2,3,4,15,1,4,5] 

# Sum
listSum = sum(numberList)
print(listSum)

#Largest number

#Easy:
listLargest = max(numberList)
print(listLargest)

#Hardway:
largestNumber = 0
for i in numberList:
    if i > largestNumber:
        largestNumber = i
print(largestNumber)

#Even numbers:
for i in numberList:
    if i % 2 == 0:
        print(i)

#Postiive numbers:
for i in numberList:
    if i > 0:
        print(i)

#Positive Numbers 2:
positiveList = []
for i in numberList:
    if i > 0:
        positiveList.append(i)
print(positiveList)

#Multiply list
multiplyList = []
for i in numberList:
    multiplyList.append(i*5)
print(multiplyList)

#Multiplyvectors
vector1 = [0, 4, 10]
vector2 = [7, 6, 5]
# newVectorList = []
# for i in vector1:
#     i = i * vector2[]
#     newVectorList.append(i)
# print(newVectorList)

def MultiplyVectors(vector1, vector2):
    newVectorList = []
    for i in range(0, len(vector1)):
        num = vector1[i] * vector2[i]
        newVectorList.append(num)
    print(newVectorList)
MultiplyVectors(vector1, vector2)


#Fizzbuzz
# for i in numberList:
#     if i % 3 == 0 and i % 5 == 0:
#         print("FIZZBUZZ BABY")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


