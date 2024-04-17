# Citim numele filmului de la tastatură
nume_film = input("Introduceți numele filmului: ")

# Definim numele filmului preferat
nume_preferat = "Inception"  # Înlocuiți cu numele filmului vostru preferat

# Verificăm dacă numele filmului introdus corespunde cu numele filmului preferat
if nume_film.lower() == nume_preferat.lower():
    print("Acesta este filmul meu preferat")
else:
    print("Din păcate nu este filmul meu preferat")