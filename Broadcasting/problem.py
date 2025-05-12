prices = [100,200,300]
discount = 10
final_price = []
for price in prices:
    discounted_price = price - (price * discount/100)
    final_price.append(discounted_price)
print(final_price)