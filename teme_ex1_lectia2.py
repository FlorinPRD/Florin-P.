# Citim prețul biletului de la tastatură
pret_bilet = float(input("Introduceți prețul biletului: "))

# Verificăm dacă clientul are peste 65 de ani
varsta = int(input("Introduceți vârsta: "))
este_senior = varsta >= 65

# Verificăm dacă călătoria are loc în timpul iernii
este_iarna = input("Este călătoria în timpul iernii? (da/nu): ").lower() == "da"

# Verificăm dacă călătoria are loc la clasa I
este_clasa_I = input("Este călătoria la clasa I? (da/nu): ").lower() == "da"

# Verificăm dacă călătoria este cu cel puțin un copil
calatoria_cu_copil = input("Este călătoria cu cel puțin un copil? (da/nu): ").lower() == "da"

# Inițializăm prețul final al biletului
pret_final = pret_bilet

# Aplicăm reducerea și taxele conform cerințelor
if este_senior:
    pret_final *= 0.85  # Reducere de 15% pentru seniori

    if este_iarna:
        pret_final *= 0.9  # Reducere suplimentară de 10% în timpul iernii

    if este_clasa_I:
        pret_final *= 1.03  # Taxă de lux de 3% pentru călătorii la clasa I
    else:
        pret_final *= 1.01  # Taxă de gestiune de 1% în caz contrar
elif calatoria_cu_copil:
    pret_final *= 0.9  # Reducere de 10% pentru călătorii cu copii

    if este_iarna:
        pret_final *= 0.9  # Reducere suplimentară de 10% în timpul iernii

    if este_clasa_I:
        pret_final *= 1.03  # Taxă de lux de 3% pentru călătorii la clasa I
    else:
        pret_final *= 1.01  # Taxă de gestiune de 1% în caz contrar

# Afișăm prețul final al biletului
print("Prețul final al biletului este:", pret_final)