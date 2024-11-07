'''racine carré'''
from math import sqrt
#### Fonction secondaire
def isprime(x):
    '''fonction permettant de trouver des nombres premiers'''
    e=round(sqrt(x))+1
    if x in (0,1):
        return False
    for i in range(2,e):
        if x%i==0:
            return False
    return True
#### Fonction principale
def main():
    '''function'''
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
