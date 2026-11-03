pizza_size = input("What size pizza do you want? (small or large): ")
toppings = int(input("How many extra toppings do you want? "))
miles = float(input("How many miles away is the delivery? "))

if pizza_size.lower() == "small":
    pizza_cost = 8
elif pizza_size.lower() == "large":
    pizza_cost = 12
else:
    print("Sorry, that pizza size is not valid.")
    pizza_cost = 0

topping_cost = toppings * 1

if miles <= 0:
    delivery_cost = 0
elif miles <= 5:
    delivery_cost = 2
else:
    delivery_cost = 2 + (miles - 5) * 1

total_cost = pizza_cost + topping_cost + delivery_cost


if pizza_size.lower() == "small" or pizza_size.lower() == "large":
    print(f"Your total pizza order costs: ${total_cost:.2f}")
