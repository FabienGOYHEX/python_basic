a = [1, 2, 'hello', True, 5, ['a', 2]]
b = [1, 2, 34, 5, 32, 543, 67, 82, 2, 70]
#a[1] = 3
# => [1, 3, 'hello', True, 5, ['a', 2]]

#b = list("hello")
# DECOMPACTAGE

variable1, variable2, varaible3, *listedureste = a
# => 1 2 hello [True, 5, ['a', 2]]

# INSERT
# append insèrera toujours la valeur ne dernier dans la liste
a.append('InsertedValueWithHappendMethod')
a.insert(0, -1)  # arg1 = index arg2= Valeur à insérer
a.extend(['chien', 'chat'])

# REMOVE
a.remove('chat')  # on passe la valeur à suprimer
a.pop(0)  # on passe l'index de la valeur à suprimer
# a.clear()  # on suprime toutes les valeurs contnues dans a

# FIND A VALUE
# a.index(value*, startIndex,endIndex)
print(a)

# SORT THE LIST

# b.sort()# => [1, 2, 2, 5, 32, 34, 67, 70, 82, 543] !!! NE MODIFIE PAS LA LISTE
c = sorted(b)
print(b)
print(c)
