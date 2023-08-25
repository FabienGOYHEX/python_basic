a = [1, 2, 'hello', True, 5, ['a', 2]]

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
a.clear()  # on suprime toutes les valeurs
print(a)
