# Ex_1 - Folosiți funcția print() și printați în consolă 4 propoziții folosind cele 4 variabile.
# Rezolvați nepotrivirile de tip pe rând prin toate modalitățile cunoscute

var1 = "Ana are mere"
var2 = 123
var3 = 3.14
var4 = True

# Convertim variabilele în șiruri de caractere și le printăm
print(str(var1))
print(str(var2))
print(str(var3))
print(str(var4))

# Ex_2 - Citiți de la tastatură numele și prenumele unei persoane și salvați-le în câte o variabilă.
# Afișați pe ecran următoarea propoziție: 'Numele complet are x caractere'.
nume = input("Introduceți numele: ")
prenume = input("Introduceți prenumele: ")
nume_complet = nume + " " + prenume
print("Numele complet are", len(nume_complet), "caractere.")

# Ex_3 - Citiți de la tastatură lungimea și lățimea unui dreptunghi și salvați-le în câte o variabilă.
# Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.
lungime = float(input("Introduceți lungimea dreptunghiului: "))
latime = float(input("Introduceți lățimea dreptunghiului: "))
aria = lungime * latime
print("Aria dreptunghiului este", aria)

# Ex_4 - Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# afișați de câte ori apare cuvântul 'the' în acest string
text = 'Coral is either the stupidest animal or the smartest rock'
aparitii = text.count("the")
print("Numărul de apariții ale cuvântului 'the' este:", aparitii)

# EX_5 Folosindu-vă de string-ul de la exercițiul 4, înlocuiți “the” cu “THE” peste tot (inclusiv în cuvântul “either”)
# și afișați pe ecran rezultatul
text_modificat = text.replace("the", "THE")
print(text_modificat)

# Ex_6 Folosindu-vă de string-ul de la exercițiul 4 folosiți un assert ca să verificați dacă acest string conține doar numere.
# Vom folosi metoda isnumeric() pentru a verifica dacă fiecare cuvânt din șir este numeric sau nu.
assert all(word.isnumeric() for word in text.split()), "Șirul nu conține doar numere."
print("Șirul conține doar numere.")