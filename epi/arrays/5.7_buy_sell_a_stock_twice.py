def profit(array):
    min_price_seen = float('inf')
    max_profit = 0

    first_buy_array = [0] * len(array)

    for i, price in enumerate(array):
        min_price_seen = min(min_price_seen, price)
        max_profit = max(max_profit, price - min_price_seen)
        first_buy_array[i] = max_profit
    print(first_buy_array)
    
    max_price_seen = float('-inf')
    for i, price in reversed(list(enumerate(array[1:], 1))):
        max_price_seen = max(max_price_seen, price)
        max_profit  = max(max_profit, max_price_seen - price + first_buy_array[i-1])
    
    return max_profit


x = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
y = [300,200,100]
z = [12, 11, 13, 9, 12, 8, 14, 13, 15]
first = [0, 0, 2, 2, 3, 3, 6, 6, 7]
second = [7, 7, 7, 7, 7, 7, 2, 2, 0]
fin = [7,7,9,9,10,5,8,6]
print(profit(x))