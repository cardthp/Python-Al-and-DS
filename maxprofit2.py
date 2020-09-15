def maxprofit2(price):
    ans = 0
    for i in range (1,len(price)):
        if price[i] - price[i-1] > 0:
            ans += price[i] - price[i-1]
    return ans


a = [int(item) for item in input("Enter the list items : ").split()] 
print(maxprofit2(a))

#print(maxprofit2([7,1,5,3,6,4]))