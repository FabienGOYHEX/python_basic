# int
a = 1
# float
b = -2, 4
# str
c = 'hello world'
# bool
d = True
# list // les valeurs d'une liste sont modifiables
e = [1, 'hello', False]
# tuple // les valeurs dun tuple ne sont plus modifiables une fois assignés (imutable)
f = (2, 'world', True)
# set //similaire à la liste, les valeurs dun set sont modifiables, IL NE PEUT Y AVOIR DE DOUBLONS
g = {3, 'Bonjour', 2.2}
# dic //similaire au set (valeurs modifiables pas de doublons)avec clés : valeurs
h = {
    'fr_bonjour ': 'Bonjour',
    'en_bonjour ': 'hello',
    'es_bonjour ': 'Hola'
}
# none
i = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))