# You’re making a shopping cart program.
# The shopping cart is declared as a list of prices, and you need to add functionality to apply a discount and output the total price.
# Take the discount percentage as input, calculate and output the total price for the shopping cart.
cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0
for item in cart:
    total+=item-(item*(discount/100))
else:
    print(total)