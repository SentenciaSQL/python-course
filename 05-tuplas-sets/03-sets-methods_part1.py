# Conjuntos

#. add()
my_set = {1,2,4}
my_set.add(5)
my_set.add(6)
my_set.add(3)
print(my_set)

# .remove() elimina elemento pero marca error si no existe
my_set.remove(2)
print(my_set)

# .discard()
my_set.discard(3)
my_set.discard(7)
print(my_set)

# .pop()
print(my_set.pop())
print(my_set)