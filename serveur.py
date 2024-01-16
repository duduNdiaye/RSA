import socket
import pickle
from rsa import generate_keypair, encrypt, decrypt

# Configuration du serveur
HOST = '127.0.0.1'
PORT = 12345

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Serveur en attente sur {HOST}:{PORT}")

# Generation de cles prive et public

# Attente de la connexion du client
client_socket, client_address = server_socket.accept()
print(f"Connexion établie avec {client_address}")

public_key, private_key = generate_keypair()
public_keys_to_send = {'public_key': public_key}
serialized_public_keys = pickle.dumps(public_keys_to_send)
client_socket.sendall(serialized_public_keys)


# Recption de cle publique

serialized_messageChiffre = client_socket.recv(4096)
received_message = pickle.loads(serialized_messageChiffre)
messageChiffre = received_message['messageChiffre']

messageClair = decrypt(messageChiffre, private_key)

print(f"le message  clair est :{messageClair}")
# Fermeture des sockets
client_socket.close()
server_socket.close()
