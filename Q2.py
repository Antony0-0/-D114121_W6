while True:
    op =  input("選擇運算符號（+，-，*，/） :")
    x = int(input("請輸⼊第⼀個數字："))
    if x == -999:
         print("程式結束。")
         break
    y = int(input("請輸⼊第二個數字："))
    if y == -999 : 
        print("程式結束。")
        break
    if op == "+":
        print("結果:" , x , op , y , "=",x+y)
    elif op == "-":
        print("結果:" , x , op , y , "=",x-y)
    elif op == "*":
        print("結果:" , x , op , y , "=",x*y)
    elif op == "/":
        if x==0 or y==0:
            print("不能除以 0，請重新輸⼊。")
        else: 
            print("結果:" , x , op , y , "=",x/y)