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

# ///////////////////////SUPPRESSION D'ELEMENTS ///////////

# crée une nouvelle paire clé valeur si la clé n'existe pas et update la value si elle existe
my_dictionnary.update({'gender': 'male'})
# pop() permet de supprimer la paire clé / valeur dont la clé est passée en argument.
# popItem() permet de supprimer la dernière paire clé / valeur ajouté au dictionnaire.
# update() prend en argument un itérable contenant des paires clé / valeur (dictionnaire, ou liste avec des tuples de deux éléments notamment) et met à jour le dictionnaire avec ces paires.
# setDefault() permet d'insérer une paire clé / valeur si la clé n'existe pas, sinon elle renvoie simplement la valeur.
print(my_dictionnary)
