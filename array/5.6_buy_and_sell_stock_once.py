"""
Given an array of daily stock price find the maximum profit. You can only buy and sell once, and you can only buy first.

[310, 315, 275, 298, 230, 255, 205, 210, 333]

To do this, you just need buy low and sell. However, the lowest price might come after the hightest. 
Thus, you want to find the largest profit for every single price. 

As you can given this array of price:
[310, 315, 275, 298, 230, 255, 205, 210, 333]

If you would have buy at 310, the largest you can get is to sell at 333 and get 23 profit.
Again if you instance buy at 315, and sell at 333 you will get a profit 18.
And continue this for the rest of the array.

Design:
minimum_price = inf, this vairable is to record the lowest price as you iterate the array
profit = 0, record the hightest price as you iterate

for price in the array:
    current_profit = price - minimum_price 
    profit = max(current_profit, profit) 
    minimum_price = min(minimum_price, price) this is why I set minimum_price to inf initially, this way the first minimum_price will be price


"""
import math

def maximum_profit(nums):
    minimum_price = math.inf
    profit = 0

    for i in range(len(nums)):
        current_profit = nums[i] - minimum_price
        profit = max(profit, current_profit)
        minimum_price = min(minimum_price, nums[i])

    return profit

print(maximum_profit([310, 315, 275, 298, 230, 255, 205, 210, 333]))