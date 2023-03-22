from datetime import date

korisnik={}

korisnik['ime']=str(input('Unesite ime korisnika:')).capitalize()
korisnik['prezime']=str(input('Unesite prezime korisnika:')).capitalize()
korisnik['telefon']=int(input('Unesite broj telefona korisnika:'))
korisnik['email']=str(input('Unesite email korisnika:')).strip()

artikl={}

artikl['naslov']=str(input('Unesite naslov artikla:'))
artikl['opis']=str(input('Unesite opis artikla:'))
artikl['cijena']=float(input('Unesite cijenu artikla:'))

prodaja={}

prodaja['korisnik']=korisnik
prodaja['artikl']=artikl
godina=int(input('Unesiste godinu isteka prodaje:'))
mjesec=int(input('Unesite mjesec isteka prodaje:'))
dan=int(input('Unesite dan isteka prodaje:'))
prodaja['datum']=date(godina,mjesec,dan)

print('Informacije o artiklu:')
print('Naslov:',prodaja['artikl']['naslov'])
print('Opis:',prodaja['artikl']['opis'])
print('Cijena:',prodaja['artikl']['cijena'])
print('Datum isteka prodaje:')
print('Dan:',prodaja['datum'].day)
print('Mjesec:',prodaja['datum'].month)
print('Godina:',prodaja['datum'].year)
print('Informacije o korisniku:')
print(prodaja['korisnik']['ime'],prodaja['korisnik']['prezime'])
print('Telefon:',prodaja['korisnik']['telefon'])
print('Email:',prodaja['korisnik']['email'])


