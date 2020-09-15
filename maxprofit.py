def maxprofit(price):
    if len(price) == 0:
        return 0
    max_profit = 0
    min_price = price[0]
    for i in price[1:]:
        if i < min_price:
            min_price = i
        elif max_profit < i - min_price:
            max_profit = i - min_price
    return max_profit

print(maxprofit([7,1,5,3,6,4]))
print(maxprofit([7,6,4,3,1]))