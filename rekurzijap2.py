def ispis_sa_zada(a):
    if a=="":
        return
    ispis_sa_zada(a[1:])
    print(a[0], end="")

tekst="Programiranje"
ispis_sa_zada(tekst)
print()
    
