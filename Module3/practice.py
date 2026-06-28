# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

# 強制結束 Ctrl + C

answer = 60

print(type(answer))
while True:
    user_input = int(input("請輸入1~100數字: "))
    if user_input < 1 or user_input > 100:
        print("超出範圍請重新輸入\n")
    elif user_input > answer:
        # 在第二行print() = 在字串內\n = 換行
        print("請輸入更小的數字")
        print()
    elif user_input < answer:
        print("請輸入更大的數字")
        print()
    elif user_input == 60:
        print("恭喜中獎")
        break











