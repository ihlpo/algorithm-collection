def profit(array):
    minimum_price_seen = array[0]
    max_difference = 0

    for price in array:
        minimum_price_seen = min(price, minimum_price_seen)
        max_difference = max(max_difference, (price - minimum_price_seen))

    return max_difference

x = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
y = [300,200,100]

print(profit(y))