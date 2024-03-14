#creation of array
array1 = [1,2,3,"Dorji",2.3]

#print(array1)

#Retrieving 
element1 = array1[0]
element2 = array1[4]
last_element = array1[-1]


#modifying element
array1[0]=10


#getting number of elements in an array
no_of_elements = len(array1)
#print (no_of_elements)

#slicing
elements = array1[0:2]
#print(elements)

#combining list
arr1 = [1,10]
arr2 = ['thimphu','wangdi']
arr3 = arr1 + arr2
#print(arr3)

#adding elements
arrVAriables = [1,2,3]
arrVAriables.append(4)
#print(arrVAriables)

#insert at a specific index
arrVAriables.insert(1,10)
print(arrVAriables)

#sorting 
arrVAriables.sort()
print(arrVAriables)

#adding to stack
stackVar = []
stackVar.append(4)
stackVar.append(2)
stackVar.append(9)
stackVar.append(1)
print('After appending', stackVar)
element = stackVar.pop()
print("after popping", stackVar)
print('removed element:', element)

