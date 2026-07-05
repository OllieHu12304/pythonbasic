# 計算幾次方
def pow(x, y):
    print(f"{x} 的 {y} 次方: {x**y}")

def get_discount(total, discount = 200):
    if total >= 2000:
        cnt = total // 2000 # 折幾個 discount
        total -= discount * cnt

        return total
    
print(f"myModule.py 的 __name__: {__name__}")

# 這一句有加比較安全
if __name__ == "__main__":

    # 測試模組
    pow(2, 4)
    result = get_discount(5000)
    print(f"折扣後金額: {result} 元")
