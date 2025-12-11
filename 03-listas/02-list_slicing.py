shopping_cart = [
    'Camisas',
    'Tenis',
    'Calcetas',
    'Pantalones',
]

# new_list = shopping_cart[1:3]
# print(new_list)
# print(shopping_cart)
#
# new_list[0] = 'Zapatos'
# new_list[1] = 'Colla'
# print(new_list)
# print(shopping_cart)

#new_cart = shopping_cart.copy()
new_cart = shopping_cart[:]
new_cart[0] = 'Playeras'
print(shopping_cart)
print(new_cart)