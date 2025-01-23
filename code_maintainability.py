def calculate_total(cart, discounts):
    totals = []
    for discount in discounts:
        if discount == '3 for 2':
            totals.append((discount, three_for_two(cart)))
        elif discount == 'Christmas Discount':
            totals.append((discount, christmas_discount(cart)))
        elif discount == 'Cheapest Free':
            totals.append((discount, cheapest_free(cart)))
    # Sort totals and return the lowest one
    totals_sorted = sorted(totals, key=lambda x: x[1])
    return totals_sorted[0][1] if totals_sorted else sum(item.price * item.quantity for item in cart)

def three_for_two(items):
    total = 0
    for item in items:
        total += item.price * (item.quantity - item.quantity // 3)
    return total

def christmas_discount(items):
    total = 0
    for item in items:
        total += item.price * item.quantity * 0.5
    return total

def cheapest_free(items):
    items_sorted = sorted(items, key=lambda x: x.price)
    total = 0
    for item in items_sorted[1:]:
        total += item.price * item.quantity
    return total   

# Define discounts
discounts = ['3 for 2', 'Christmas Discount', 'Cheapest Free']
# Define cart
cart = [
    {'name': 'item1', 'price': 10, 'quantity': 3},
    {'name': 'item2', 'price': 20, 'quantity': 1},
    {'name': 'item3', 'price': 30, 'quantity': 1}
    ]
# Calculate total
total = calculate_total(cart, discounts)
print(f'Total: {total}')