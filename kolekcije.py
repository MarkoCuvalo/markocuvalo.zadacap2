import random

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 
         'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 
             'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

radnici = []

def randomRadnici(brojRadnika):
    for i in range(brojRadnika):
        radnik = {}
        imeIndex = random.randint(0, len(imena) - 1)
        ime = imena[imeIndex]
        prezimeIndex = random.randint(0, len(prezimena) - 1)
        prezime = prezimena[prezimeIndex]
        radnik["ime"] = ime
        radnik["prezime"] = prezime
        radnici.append(radnik)

randomRadnici(15)

def randomSati():
    for osoba in radnici:
        satnica = "%.2f" % random.uniform(4, 6)
        osoba["satnica"] = satnica
        tjedna_satnica = random.randint(20, 31)
        osoba["tjednaSatnica"] = tjedna_satnica
    
randomSati()

kraj = []

def isplata():
    for osoba in radnici:
        isplata = float(osoba["satnica"]) * int(osoba["tjednaSatnica"])
        osoba["isplata"] = int(isplata)
        ime = osoba["ime"]
        prezime = osoba["prezime"]
        isplata = osoba["isplata"]
        kraj.append((ime, prezime, isplata))

isplata()
print("sve podatke: ")
for osoba in kraj:
    print(osoba)

def ukupnoIProsjecno():
    ukupno = 0
    for i in range(len(kraj)):
        ukupno += kraj[i][2]
    print("Ukupno: ", ukupno)
    prosjecno = ukupno / len(kraj)
    print("Prosjecno: ", "%.2f" % prosjecno)
    print("Imena od svih radnika koji imaju vise od prosjecno: ")
    for radnik in kraj:
        if radnik[2] > prosjecno:
            print(radnik[0])

ukupnoIProsjecno()

