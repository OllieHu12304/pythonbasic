import random

while True:
    # 每次開始新遊戲都重新產生答案
    answer = random.randint(1, 100)
    count = 0

    # 一場遊戲
    while True:
        try:
            user_input = int(input("請輸入 1~100 的數字："))
        except ValueError:
            print("請輸入數字，而不是文字！")
            continue

        if user_input < 1 or user_input > 100:
            print("超出範圍，請重新輸入！")
            continue

        if user_input > answer:
            print("請輸入更小的數字")
            count += 1

        elif user_input < answer:
            print("請輸入更大的數字")
            count += 1

        else:
            print("🎉 恭喜答對！")
            break

        print(f"目前已猜錯 {count} 次")

        if count == 3:
            print(f"你已經猜錯 3 次了！答案是 {answer}")
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