import random 

class Pokemon:
    def __init__(self, nom, pa, niveau=1, defense=0, pv=100):
        self.nom = nom
        self.pv = pv
        self.niveau = niveau
        self.pa = pa
        self.defense = defense
        self.nom_pokemon = ["Bulbizarre", "Carapuce", "Salamèche"]

    def Choose_Pokemon(self):
        self.nom = random.choice(self.nom_pokemon)
        return self.nom

class Bulbizarre(Pokemon):
    def __init__(self, nom, pa, niveau=1, defense=0, pv=100):
        super().__init__(nom, pa, niveau, defense, pv)
        self.pa = 49
        self.defense = 49


    def Affiche_Bulbizarre(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)

class Carapuce(Pokemon):
    def __init__(self, nom, pa, niveau=1, defense=0, pv=100):
        super().__init__(nom, pa, niveau, defense, pv)
        self.pa = 48
        self.defense = 65


    def Affiche_Carapuce(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)

class Salameche(Pokemon):
    def __init__(self, nom, pa, niveau=1, defense=0, pv=100):
        super().__init__(nom, pa, niveau, defense, pv)
        self.pa = 52
        self.defense = 43


    def Affiche_Salameche(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)

p=Pokemon("",10)
b = Bulbizarre("", 10)
c = Carapuce("", 10)
s = Salameche("", 10)
p.Choose_Pokemon()
print("Vous avez obtenu :", p.nom)
if p.Choose_Pokemon() == "Bulbizarre":
    b.Affiche_Bulbizarre()
elif p.Choose_Pokemon() == "Carapuce":
    c.Affiche_Carapuce()
elif p.Choose_Pokemon() == "Salameche":
    s.Affiche_Salameche()
else:
    print("Non, méchant")
