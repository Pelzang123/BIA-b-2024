#searching 
#sorting

#Problem 1
#?input
user_input = [1,2,3,4,5,6,7,8,9,11]
n = 10

#check to see if a certain number exist in the user input array
result = False #a variable to keep track pf your answer
for e in user_input:
    if  e == n :
        result = True   

if result == True:     
    print('found')
else:   
    print('not found')


#for e in user_input:
 #   if e == n:
  #      print("Found")
   # else:
    #    print("Not found")


