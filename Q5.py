while True:
    number = input("請輸入一個正整數：")
    if number.isdigit():
        n = int(number)
        break
    else:
        print("請輸入一個有效的正整數。")
factorial = 1
if n == 0:
    factorial = 1
else:
    for i in range(1, n + 1):
        factorial *= i
print(f"{n}! = {factorial}")