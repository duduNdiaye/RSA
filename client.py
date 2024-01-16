import socket
import pickle
from rsa import encrypt
# Configuration du client
HOST = '127.0.0.1'
PORT = 12345

# Création du socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Recption de cle publique

serialized_public_keys = client_socket.recv(4096)
received_key = pickle.loads(serialized_public_keys)

public_key = received_key['public_key']
message = input('Quel est le message a envoyer au serveur: ')

# Chiffrement du message
messageChiffre = encrypt(int(message), public_key)

# Envoie du message chiffre
messageChiffre_to_send = {'messageChiffre': messageChiffre}
serialized_messageChiffre = pickle.dumps(messageChiffre_to_send)
client_socket.sendall(serialized_messageChiffre)

# Envoi de données au serveur
# message = "Salut serveur, c'est le client !"
# client_socket.sendall(message.encode())

# Fermeture du socket client
client_socket.close()
