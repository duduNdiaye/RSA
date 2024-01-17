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

# Attente de la connexion du client
client_socket, client_address = server_socket.accept()
print(f"Connexion établie avec {client_address}")

# Génération de clés privées et publiques
public_key, private_key = generate_keypair()
public_keys_to_send = {'public_key': public_key}
serialized_public_keys = pickle.dumps(public_keys_to_send)
client_socket.sendall(serialized_public_keys)

# Réception du message chiffré
serialized_message_chiffre = client_socket.recv(4096)
received_message = pickle.loads(serialized_message_chiffre)
message_chiffre = received_message['message_chiffre']

# Vérifier le type de données reçues et déchiffrer en conséquence
if isinstance(message_chiffre, int):
    # Si c'est un nombre, déchiffrer directement
    message_clair = decrypt(message_chiffre, private_key)
    print(f"Le message clair est : {message_clair}")
elif isinstance(message_chiffre, list):
    # Si c'est une liste (chaîne de caractères chiffrée), déchiffrer chaque caractère
    message_numerical = [decrypt(char, private_key) for char in message_chiffre]
    message_clair = ''.join([chr(num) for num in message_numerical])
    print(f"Le message clair est : {message_clair}")

# Fermeture des sockets
client_socket.close()
server_socket.close()
