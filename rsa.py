import random
from sympy import mod_inverse, isprime


def generate_keypair(bits=1024):
    # Générer deux nombres premiers aléatoires
    p = generate_prime(bits)
    q = generate_prime(bits)

    # Calculer le modulo n
    n = p * q

    # Calculer la fonction d'Euler (indicatrice d'Euler) phi(n)
    phi_n = (p - 1) * (q - 1)

    # Choisir un exposant public e (habituellement un petit nombre premier)
    e = 65537

    # Calculer l'exposant privé d
    d = mod_inverse(e, phi_n)

    # Retourner la clé publique et privée
    return ((n, e), (n, d))


def generate_prime(bits):
    # Générer un nombre premier aléatoire avec le nombre de bits spécifié
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num


def encrypt(message, public_key):
    # Déballer la clé publique
    n, e = public_key

    # Chiffrer le message en utilisant l'exponentiation modulaire
    ciphertext = pow(message, e, n)

    return ciphertext


def decrypt(ciphertext, private_key):
    # Déballer la clé privée
    n, d = private_key

    # Déchiffrer le message en utilisant l'exponentiation modulaire
    message = pow(ciphertext, d, n)

    return message


# # Exemple d'utilisation
# if __name__ == "__main__":
#     # Génération des clés
#     public_key, private_key = generate_keypair()

#     # Message à chiffrer
#     message = 42

#     # Chiffrement du message
#     ciphertext = encrypt(message, public_key)
#     print("Message chiffré:", ciphertext)

#     print('\n\n')
#     # Déchiffrement du message
#     decrypted_message = decrypt(ciphertext, private_key)
#     print("Message déchiffré:", decrypted_message)
