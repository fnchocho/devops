class_supplies = ['books', 'pens', 'rulers', 'markers', 'tapes']
quantity_bought = [104, 8675, 207, 64]
unit_prize = [5.00, 0.49, 1.09, 3.47]
for list_of_items in zip(class_supplies, quantity_bought, unit_prize):
    print(list_of_items)

x = list(quantity_bought)
y = list(unit_prize)
i = quantity_bought.count()
print(i)

'''
amount_spent = x[i]*y[i]
for i in amount_spent:
    print(amount_spent)
    i += 1
'''






