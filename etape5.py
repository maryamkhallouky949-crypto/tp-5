classe=[
    ["Maryam", 20, 15.5],
    ["Aya", 18, 16.0],
    ["Amine", 21,17.5]
]
classe.sort(key=lambda ligne: ligne[2], reverse=True)
print("Tri par note décroissante :")
print(classe)

moyenne = sum(ligne[2] for ligne in classe) / len(classe)
print("Moyenne des notes :", moyenne)

nom_recherche = input("Nom ? ")
resultat = next(
    (ligne for ligne in classe if ligne[0].lower() == nom_recherche.lower()),
    None
)
print(resultat or "Étudiant introuvable.")

classe_copie = classe[:]   
classe_copie[0][1] = 19    
print("Original :", classe)
print("Copie    :", classe_copie)



import copy
classe_copie = copy.deepcopy(classe)
classe_copie[0][1] = 19
print("Original :", classe)
print("Copie    :", classe_copie)

classe_dict = [
    {"nom": nom, "age": age, "note": note}
    for nom, age, note in classe
]

print(classe_dict)