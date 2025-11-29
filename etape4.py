note_classe=[
    ["Maryam", 20, 15.5],
    ["Aya", 18, 14.0],
    ["Amine", 21,13.5]
]
print(note_classe)
note_classe.append(["Ahmed",18,14.5])
print(note_classe)
for index, (nom, age, note) in enumerate(note_classe, start=1):
    print(f"Étudiant {index} : {nom} ({age} ans) – note {note}")
age_Amine = note_classe[2][1]
print(age_Amine)
note_classe[2][2] = 17.0
print(note_classe)