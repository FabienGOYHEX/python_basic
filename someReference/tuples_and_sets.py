# LE TUPLE EST IMUTABLE
my_tuple = (1, 2, 3)
# print(my_tuple[0])


# DESEMPACQUETAGE
var1, var2, var3 = my_tuple  # => var1= value1 |  var2= value2 | var3= value3

a, *reste = (1, 2, 3)  # ValueError: too many values to unpack
# print(a)  # 1
# print(reste)  # [2, 3]

# /////////////////////////////////// SET ////////////////////////
# une seule valeur unique
my_set = {1, 2, 3}
my_set.add(100)
# => remove supprime l'élément | erreur retournée si la valeur n'est pas dans le set
my_set.remove(3)
# => discard supprime l'élément pas d'erreur si la valeur n'est pas dans le set
my_set.update((6, 7))
my_set.discard(3)

print(my_set)
