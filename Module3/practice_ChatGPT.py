# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

# 強制結束 Ctrl + C

# 報錯時 提示使用者「請輸入數字 而不是文字」
import random

while True:
    # 每次開始新遊戲都重新產生答案
    answer = random.randint(1, 100)
    print(answer)
    count = 0
    
    while True:
        try:
            user_input = int(input("請輸入 1~100 的數字："))
        except ValueError:
            print("請輸入數字，而不是文字！")
            continue
            # 先讓`except`處理資料型別，正確才 continue

        if user_input < 1 or user_input > 100:
            print("超出範圍，請重新輸入！")
            continue
            # 第一層處理資料範圍

        if user_input > answer:
            print("請輸入更小的數字")
            count += 1 # 錯誤計數器放在這裡
            # 此時才正式進入遊戲，注意這裡還是 if

        elif user_input < answer:
            print("請輸入更大的數字")
            count += 1

        else:
            print("🎉 恭喜答對！")
            break

        print(f"目前已猜錯 {count} 次")

        if count == 3:
            print(f"你已經猜錯 3 次了！答案是 {answer} ，嫩啦！")
            break

        print()

    # 是否再玩一次
    while True:
        again = input("是否再玩一次？(y/n)：").lower()

        if again == "y":
            print()
            break      # 跳出詢問，再開始新的一局

        elif again == "n":
            print("遊戲結束，掰掰！")
            exit()     # 結束整個程式

        else:
            print("請輸入 y 或 n")