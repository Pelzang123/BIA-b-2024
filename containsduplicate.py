input_arr = [1,2,3,4]

def containsDuplicate(nums):
    #solution code here
    for element in nums:
        for i in nums:
            print('elemnt:',element)
            print('i',i)
            print('==============')

    return True
    #either return True or False

result = containsDuplicate(input_arr)

print(result)