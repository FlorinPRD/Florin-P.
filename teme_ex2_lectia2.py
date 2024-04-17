# Citim tipul clientului și numărul de unități comandate de la tastatură
tip_client = input("Introduceți tipul clientului (wholesale/retail): ").lower()
numar_unitati = int(input("Introduceți numărul de unități comandate: "))

# Inițializăm prețul unitar al unei mărfuri
pret_unitar = 10  # Presupunem un preț unitar arbitrar de 10 dolari

# Inițializăm discount-urile
discount_total = 0

# Verificăm tipul clientului și aplicăm discount-urile corespunzătoare
if tip_client == "wholesale":
    discount_total += 2  # Reducere de 2% pentru clienții wholesale

if numar_unitati >= 50:
    discount_total += 2  # Reducere de 2% pentru comenzile de 50 sau mai multe unități

# Adăugăm discount-ul pentru plata ramburs la livrare
discount_total += 2

# Calculăm prețul total după aplicarea discount-urilor
pret_total = pret_unitar * numar_unitati * (1 - discount_total / 100)

# Afișăm prețul total
print("Prețul total al comenzii este:", pret_total)