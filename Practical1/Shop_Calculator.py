total = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item: "))
    total += price

# apply 10% discount
if total > 100:
    total *= 0.9

print("Total price for ", number, " items is $", total, sep='')

