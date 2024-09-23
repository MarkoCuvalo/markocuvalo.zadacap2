import random

imena = [
    "Vedran", "Andrea", "Ana", "Marta", "Martina", "Iva", "Mirko", "Jakov", "Marko", "Mihaela",
    "Petar", "David", "Ivan", "Ivan", "Ana", "Dinko", "Petar", "Sanja", "Nikola", "Vinko", "Mihael",
    "Zdravko", "Patrik", "Kristijan", "Marin", "Kristijan", "Petar", "Mateo", "Bože", "Ivan-Kajo",
    "Matej", "Karlo", "Ana", "Lucija", "Bože", "Emanuel", "Ante-Roko", "Blaž", "Marijanela",
    "Leonarda", "Antonio", "Ana-Maria", "Petra", "Leo", "Mario", "Marijana", "Jelena", "Stjepan",
    "Dario", "Matej"
]

ucenici = {}
brojOcjena = {}
polozeno = 0

for student in imena:
    randomOcjena = random.randint(1, 5)
    ucenici[student] = randomOcjena
    if randomOcjena in brojOcjena:
        brojOcjena[randomOcjena] += 1
    else:
        brojOcjena[randomOcjena] = 1
    if randomOcjena > 1:
        polozeno += 1

postotak = int(polozeno / len(imena) * 100)

print(ucenici, "\n\nbroj ocjena: ", brojOcjena, "\n\nPostotak prolaznosti: ", postotak, "%")
