def hash():
    hashset = set()
    nums = input("enter your numbers:")

    for n in nums:
        if n in hashset:
            print("True")
        hashset.add(n)
    print("False") 

hash()
