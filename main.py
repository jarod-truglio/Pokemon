import random 

class Pokemon:
    def __init__(self, nom, element, pa, niveau=1, defense=0, pv=100):
        self.element = element
        self.nom = nom
        self.pv = pv
        self.niveau = niveau
        self.pa = pa
        self.defense = defense
        self.nom_pokemon = ["Bulbizarre", "Carapuce", "Salameche"]

    def Choose_Pokemon(self):
        self.nom = random.choice(self.nom_pokemon)
        return self.nom

class Bulbizarre(Pokemon):
    def __init__(self, pa, niveau=1, defense=0, pv=100, nom="Bulbizarre", element="Plante"):
        super().__init__(nom,  element, pa, niveau, defense, pv)
        self.pa = 49
        self.defense = 49


    def Affiche_Bulbizarre(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)

class Carapuce(Pokemon):
    def __init__(self, pa, niveau=1, defense=0, pv=100, nom="Carapuce", element="Eau"):
        super().__init__(nom, element,  pa, niveau, defense, pv)
        self.pa = 48
        self.defense = 65


    def Affiche_Carapuce(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)

class Salameche(Pokemon):
    def __init__(self,  pa,nom="Salameche", niveau=1, defense=0, pv=100, element="Feu"):
        super().__init__(nom, element,  pa, niveau, defense, pv)
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
if p.nom == "Bulbizarre":
    b.Affiche_Bulbizarre()
elif p.nom == "Salameche":
    s.Affiche_Salameche()
elif p.nom == "Carapuce":
    c.Affiche_Carapuce()
else:
    print("Erreur")

