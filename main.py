import random 

class Pokemon:
    def __init__(self, nom, attaque, pa, niveau=1, defense=0, pv=100):
        self.nom = nom
        self.pv = pv
        self.niveau = niveau
        self.pa = pa
        self.defense = defense
        self.attaque = attaque
        self.nom_pokemon = ["Bulbizarre", "Carapuce", "Salameche"]
        self.nom_attaque = ["Attaque Rapide","Attaque Spéciale","Regen"]

    def Choose_Pokemon(self):
        self.nom = random.choice(self.nom_pokemon)
        return self.nom
    
    def Choose_Attaque(self):
         self.attaque = random.choice(self.nom_attaque)
         return self.attaque

    def Show_Information(self):
        print(self.nom)
        print(self.pv)

class Bulbizarre(Pokemon):
    def __init__(self, pa, attaque, niveau=1, defense=0, pv=100, nom="Bulbizarre", element="Plante"):
        super().__init__(nom, pa, attaque, niveau, defense, pv)
        self.element = element
        self.pa = 49
        self.defense = 49

    def Affiche_Bulbizarre(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)
        print("Son élément est :", self.element)

    def Attaque_Spe_Pika(self):
            self.Attaque_Spe_Pika = False
            if self.Attaque_Spe_Pika == False :
                self.pv -= 65
            else :
                 print("Attaque spéciale déjà utilisé")
    
    def Attaque_Rapide_Pika(self):
            self.pv -= 55

class Carapuce(Pokemon):
    def __init__(self, pa, attaque, niveau=1, defense=0, pv=100, nom="Carapuce",element="Eau"):
        super().__init__(nom, pa, attaque, niveau, defense, pv)
        self.pa = 48
        self.defense = 65
        self.element = element

    def Affiche_Carapuce(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)
        print("Son élément est :", self.element)

    def Attaque_Spe_Pika(self):
            self.Attaque_Spe_Pika = False
            if self.Attaque_Spe_Pika == False :
                self.pv -= 65
            else :
                 print("Attaque spéciale déjà utilisé")
    
    def Attaque_Rapide_Pika(self):
            self.pv -= 55

class Salameche(Pokemon):
    def __init__(self, pa, attaque, nom="Salameche", niveau=1, defense=0, pv=100, element="Feu"):
        super().__init__(nom, pa, attaque, niveau, defense, pv)
        self.pa = 52
        self.defense = 43
        self.element = element

    def Affiche_Salameche(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)
        print("Son élément est :", self.element)

    def Attaque_Spe_Pika(self):
            self.Attaque_Spe_Pika = False
            if self.Attaque_Spe_Pika == False :
                self.pv -= 65
            else :
                 print("Attaque spéciale déjà utilisé")
    
    def Attaque_Rapide_Pika(self):
            self.pv -= 55

class Pikachu(Pokemon):
    def __init__(self, pa, attaque, nom="Pikachu", niveau=1, defense=0, pv=100, element="Electrique"):
        super().__init__(nom, pa, attaque, niveau, defense, pv)
        self.pa = 55
        self.defense = 40
        self.element = element

    def Affiche_Pikachu(self):
        print("Sa Puissance d'attaque est de :", self.pa)
        print("Sa défense est de :", self.defense)
        print("Son niveau est de :", self.niveau)
        print("Ses Points de vie sont de :", self.pv)
        print("Son élément est :", self.element)

    def Attaque_Rapide_Bulbi(self):
            self.pv -= 48
    
    def Attaque_Rapide_Carapuce(self):
            self.pv -= 49

    def Attaque_Rapide_Salam(self):
            self.pv -= 52

p = Pokemon("",10,10)
b = Bulbizarre("", 10)
c = Carapuce("", 10)
s = Salameche("", 10)
pika = Pikachu("",10)

class Joueur1(Pikachu):
    def __init__(self, nom, pa, attaque, niveau=1, defense=0, pv=100):
        super().__init__(nom, pa, attaque, niveau, defense, pv)
    print("------------")
    print("Tu à obtenu Pikachu")
    pika.Affiche_Pikachu()
    print("------------")

class Joueur2(Bulbizarre, Carapuce, Salameche):
    def __init__(self, nom, pa, attaque, niveau=1, defense=0, pv=100):
        super().__init__(nom, pa, attaque, niveau, defense, pv)
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

j1 = Joueur1
j2 = Joueur2

