class_supplies = ['books', 'pens', 'rulers', 'markers', 'tapes']
quantity_bought = [104, 8675, 207, 64]
unit_prize = [5.00, 0.49, 1.09, 3.47]
for list_of_items in zip(class_supplies, quantity_bought, unit_prize):
    print(list_of_items)

for supply in class_supplies:
    cost= int(quantity_bought) * int(unit_prize)
    print(cost)


