# //////////////////////////////FUNCTIONS/////////////////////////////
def my_funtion(a, b=2):  # valeur par défaut  de b =2 di non spécifié
    return a + b


print(my_funtion(1, 6))
# ///////// scope des fonctions //////////////
# read the python doc

a = 1

# Pour pouvoir modifier une variable globale dans une fonction, il faut obligatoirement utiliser le mot clé global qui permet d'assurer à Python que nous modifions intentionnellement une variable globale :


def fonction():
    global a
    a += 1


fonction()
# L'instruction nonlocal permet d'indiquer qu'une variable doit être cherchée dans la portée de la fonction parente.
