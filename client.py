import socket
import pickle
from rsa import encrypt

# Configuration du client
HOST = '127.0.0.1'
PORT = 12345

# Création du socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Réception de la clé publique
serialized_public_keys = client_socket.recv(4096)
received_key = pickle.loads(serialized_public_keys)
public_key = received_key['public_key']

# Saisie du message à envoyer au serveur
user_input = input('Quel est le message à envoyer au serveur: ')

# Vérifier si l'entrée de l'utilisateur est un nombre ou une chaîne de caractères
if user_input.isdigit():
    # Si c'est un nombre, chiffrez-le directement
    message_chiffre = encrypt(int(user_input), public_key)
else:
    # Si c'est une chaîne de caractères, convertissez chaque caractère en sa représentation numérique
    message_numerical = [ord(char) for char in user_input]
    message_chiffre = [encrypt(char, public_key) for char in message_numerical]

# Envoi du message chiffré
message_chiffre_to_send = {'message_chiffre': message_chiffre}
serialized_message_chiffre = pickle.dumps(message_chiffre_to_send)
client_socket.sendall(serialized_message_chiffre)

# Fermeture du socket client
client_socket.close()
