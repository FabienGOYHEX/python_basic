number = 1550 

if number < 500 : 
    print('petit nombre')
elif number > 1000 :
    print('atteint des sommets')
elif number == 500 :
    print('yesssss')
else :
    print('nope')

    # Opérateurs logique :  and, or, not

is_adult =  True
is_rich = True

if is_adult and is_rich :
    print('Bienvenue à bord de space X')
else : print('Nope')

#Match
error = 404
#
match error:
    case 500:
        print('erreur serveur')
    case 400:
        print('Mauvaise requête')
    case 404:
        print('ressource nontrouvée')
    case _ : 
        print('error iconnue ')
        
