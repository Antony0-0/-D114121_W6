number = input("x = ")
if number[0] == '-':
    print("False")
else:
    if number == number[::-1]:
        print("True")
    else:
        print("False")