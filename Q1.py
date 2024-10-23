total = 0
count = 0
while True :
    x = input("請輸⼊成績：")
    if x == "-1" :
        if count == 0:
            print("沒有輸⼊任何成績")
            break
        else :
            print("平均成績為：", total/count )
            break
    if int(x) < 0 and int(x)  != -1 :
        print("成績不能為負數，請重新輸⼊。")
    elif int(x) > 0 :
        x = int(x)
        total += x
        count += 1
    else:
        print("請輸⼊有效的數字。")