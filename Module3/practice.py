# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

# 強制結束 Ctrl + C

# 報錯時 提示使用者「請輸入數字 而不是文字」

import random

# 隨機取得指定範圍的數字
answer = random.randint(1, 100)
print(answer)
# answer = 60

# 猜錯三次 就不繼續
# 猜對了 可以詢問使用者要不要再玩一次 (y/n)
while True:
    answer = random.randint(1, 100)
    print(answer)
    count = 0

    while True:
        try:
            user_input = int(input("請輸入1~100數字: "))
        except Exception:
            print('請輸入數字 而不是文字')
            continue

        if user_input < 1 or user_input > 100:
            print("超出範圍請重新輸入\n")
        elif user_input > answer:
            # 在第二行print() = 在字串內\n = 換行
            print("請輸入更小的數字")
            count += 1
            print(f'輸入錯誤 {count} 次囉!')
            print()
        elif user_input < answer:
            print("請輸入更大的數字")
            count += 1
            print(f'輸入錯誤 {count} 次囉!')
            print()
        elif count == 3:
            print("你猜錯3次了，嫩啦")
            break
        elif user_input == answer:
            again = input("恭喜中獎，是否再玩一次(y/n)").lower()
            if again == 'y':

            elif again == 'n':
                break
