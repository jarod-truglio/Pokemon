import random 

class Pokemon:
    def __init__(self, nom, pa, niveau=1, defense=0, pv=100):
        self.nom = nom
        self.pv = pv
        self.niveau = niveau
        self.pa = pa
        self.defense = defense
        self.nom_pokemon = ["Bulbizarre", "Carapuce", "Salameche"]

    def Choose_Pokemon(self):
        self.nom = random.choice(self.nom_pokemon)
        return self.nom
    
    def Attaque_Rapide(self):
        self.pv -= self.pa

    def Show_Information(self):
        print(self.nom)
        print(self.pv)


class Bulbizarre(Pokemon):
    def __init__(self, pa, niveau=1, defense=0, pv=100, nom="Bulbizarre", element="Plante"):
        super().__init__(nom, pa, niveau, defense, pv)
        self.element = element
        self.pa = 49
        self.defense = 49

    def Affiche_Bulbizarre(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)
        print("Son élément est :", self.element)

    def Attaque_Rapide(self):
        if self.element == "Feu":
            self.pv -= 24
        if self.element == "Eau":
            self.pv -= 98
        if self.element == "Plante":
            self.pv -= 49

class Carapuce(Pokemon):
    def __init__(self, pa, niveau=1, defense=0, pv=100, nom="Carapuce",element="Eau"):
        super().__init__(nom, pa, niveau, defense, pv)
        self.pa = 48
        self.defense = 65
        self.element = element

    def Affiche_Carapuce(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)
        print("Son élément est :", self.element)

    def Attaque_Rapide(self):
        if self.element == "Feu":
            self.pv -= 96
        if self.element == "Eau":
            self.pv -= 48
        if self.element == "Plante":
            self.pv -= 24

class Salameche(Pokemon):
    def __init__(self, pa,nom="Salameche", niveau=1, defense=0, pv=100, element="Feu"):
        super().__init__(nom, pa, niveau, defense, pv)
        self.pa = 52
        self.defense = 43
        self.element = element

    def Affiche_Salameche(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)
        print("Son élément est :", self.element)

    def Attaque_Rapide(self):
        if self.element == "Feu":
            self.pv -= 52
        if self.element == "Eau":
            self.pv -= 26
        if self.element == "Plante":
            self.pv -= 104

p=Pokemon("",10)
b = Bulbizarre("", 10)
c = Carapuce("", 10)
s = Salameche("", 10)

class Joueur1(Pokemon):
    def __init__(self, nom, pa, niveau=1, defense=0, pv=100):
        super().__init__(nom, pa, niveau, defense, pv)
    p.Choose_Pokemon()
    print("------------")
    print(f"Joueur1 à obtenu : {p.nom}")
    if p.nom == "Bulbizarre":
        b.Affiche_Bulbizarre()
    elif p.nom == "Salameche":
        s.Affiche_Salameche()
    elif p.nom == "Carapuce":
        c.Affiche_Carapuce()
    else:
        print("Erreur")
    print("------------")

class Joueur2(Pokemon):
    def __init__(self, nom, pa, niveau=1, defense=0, pv=100):
        super().__init__(nom, pa, niveau, defense, pv)
    p.Choose_Pokemon()
    print("------------")
    print(f"Joueur2 à obtenu : {p.nom}")
    if p.nom == "Bulbizarre":
        b.Affiche_Bulbizarre()
    elif p.nom == "Salameche":
        s.Affiche_Salameche()
    elif p.nom == "Carapuce":
        c.Affiche_Carapuce()
    else:
        print("Erreur")
    print("------------")

j1 = Joueur1() 
j2 = Joueur2()