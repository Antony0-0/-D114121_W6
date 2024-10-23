rotate = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
number = input("x =")
rotated_number = ""
valid = True
for digit in number:
    if digit not in rotate:
        valid = False
        break
    rotated_number = rotate[digit] + rotated_number
if valid and rotated_number == number:
    print("true")
else:
    print("false")