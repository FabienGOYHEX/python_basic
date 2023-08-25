my_dictionnary = {
    'age': 18,
    'sexe': 'M',
    'firstName': 'Jean',
    'LastName': 'BON',
    'adress': {
        'city': 'Paris'
    }
}
my_new_dictinnary = dict(deco='vintage', tapis="blue", tYpe="house")
# Retourne une erreur si la key n'hexiste pas !!

print(my_dictionnary['adress']['city'])
print(my_new_dictinnary)

print(my_dictionnary.get('age'))
#fucking_dictionnary = my_dictinnary.copy()


# PARCOURIR LES VALEURS

# for i in my_dictionnary.values():
# print(i)
# => .keys() => age sexe firstName LastName adress
# => .value() => 18 M Jean BON {'city': 'Paris'}
# => .items() => ('age', 18) ('sexe', 'M') ('firstName', 'Jean') ('LastName', 'BON') ('adress', {'city': 'Paris'})

# DECONSTRUCTION DE LA PAIRE CLE VALEUR D'UN DICTIONNAIRE

for key, value in my_dictionnary.items():
    print(key)
    print(value)
# => age
# 18
# sexe
# M
# firstName
# Jean
# LastName
# BON
# adress
#{'city': 'Paris'}
