my_str = "je suis une chaine de caractère"
print(my_str[0])  # => J
print(my_str[0:7])  # => Je suis

# Exercice affichez la phrase contenue dans my_str en sens inverse
print(my_str[-1::-1])  # => Je suis

name = "Jean"
age = 12

print("Bonjour " + name + " vous avez " + str(age) + " ans.")

print(f"Bonjour {name} vous avez {age}  ans.")
# old version pyton2
print('Bonjour {} vous avez {}  ans.'.format(name, age))

# METHOD
# LEN
len(my_str)  # => 31 my_str à 31 caractères
# CAPITALIZE
my_str.capitalize()  # =>Je suis une chaine de caractère
# TITLE
my_str.title()  # =>Je Suis Une Chaine De Caractère
# UPPER
my_str.upper()  # => JE SUIS UNE CHAINE DE CARACTERE
# LOWER
my_str.lower()  # =>je suis une chaine de caractère
# COUNT
# => 3/ retourne le nombre de a contenu dans ma chaine de caractère
my_str.count('a')
# FIND
# => 3/ retourne l'index à partir duquel la valeur a été trouvée
my_str.find('suis')
# INDEX
# => 3/ retourne l'index à partir duquel la valeur a été trouvée ERREUR EN CAS DE VALUER NON TROUVEE
print(my_str.index('suis'))
# ENDSWIDTH
print(my_str.endswith('suis'))  # => False / ne finis pas par suis
# STARTSWITH
print(my_str.startswith('je'))  # => True / commence bien par je

# SPLIT
# => ['je', 'suis', 'une', 'chaine', 'de', 'caractère'] split la chaine au niveau des espaces | peut recevoir une valeur ex: ,
print(my_str.split())
