'''
Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo imena + prezime.
X predstavlja bilo koji broj (može reći u beskonačnost), a taj broj ne mora postojati (može biti samo iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
'''
import re

email = input("Enter email (name.surname@fpmoz.sum.ba): ")
eduid = input("Enter eduId (isurnameX@sum.ba): ")


regex = r'^[a-z]+\.[a-z]+@fpmoz\.sum\.ba$'
reg = r'^[a-z][a-z]+[0-9]*@sum\.ba$'

if re.match(regex, email):
    print("Email is valid.")
else:
    print("Email is not valid.")

if re.match(reg, eduid):
    print("EduId is valid.")
else:
    print("EduId is not valid.")


   
