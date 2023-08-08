# 121. Best Time to Buy and Sell Stock (Easy)
# Input: prices = [7,1,5,3,6,4] Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# >>ตั้ง variable global ขึ้นมาก่อน เพื่อวนค่าหา profit และทำให้ค่า min/max เปลี่ยนเป็นค่าใหม่ตาม i ได้

def maxProfit(prices):
    minprice = prices[0]
    maxprice = prices[0]
    profit = 0
    for i in prices:
        if i < minprice:
            minprice = i
            maxprice = i
        elif i > maxprice:
            maxprice = i
            if profit < maxprice-minprice:
                profit = maxprice-minprice
    return profit


print(maxProfit([7,1,5,3,6,4]))