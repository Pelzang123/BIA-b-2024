def flooratthgeend(input_string):
    floor_at_end = 0
    for i in input_string:
        if i == '(':
            floor_at_end += 1
        elif i ==')':
            floor_at_end -= 1
    print('The floor you are in is', floor_at_end)


flooratthgeend(input('enter the brackets:'))


input_str ="(((((((((((((((((())))))))))))))))))"

stack = []

for i in input_str:
    if i == "(":
        stack.append(i)
    if i == ")":
        stack.pop(i)

    length = len(stack)
    if length != 0:
        print("True")
    else:
        print("False")

