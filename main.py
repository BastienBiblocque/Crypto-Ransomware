from cryptography.fernet import Fernet
import os

# Générer une clé de chiffrement (à faire une seule fois)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Sauvegarder la clé dans un fichier (pour usage ultérieur)
with open('secret.key', 'wb') as key_file:
    key_file.write(key)


# Fonction pour chiffrer un fichier
def encrypt_file(file_path, cipher_suite):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    print("Fichier chiffré avec succès.")


# Fonction pour déchiffrer un fichier
def decrypt_file(encrypted_file_path, cipher_suite):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
    original_file_path = encrypted_file_path.replace('.encrypted', '.decrypted')
    with open(original_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    print("Fichier déchiffré avec succès.")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Le fichier {file_path} a été supprimé avec succès.")
    else:
        print(f"Le fichier {file_path} n'existe pas.")

# Chemin vers le fichier à chiffrer
file_path = 'logo.png'

# Chiffrer le fichier
encrypt_file(file_path, cipher_suite)

# Charger la clé pour déchiffrer (depuis le fichier sauvegardé)
with open('secret.key', 'rb') as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

# Chemin vers le fichier chiffré
encrypted_file_path = file_path + '.encrypted'

# Déchiffrer le fichier
decrypt_file(encrypted_file_path, cipher_suite)



# Supprimer le fichier chiffré
delete_file(encrypted_file_path)

# Supprimer le fichier original (optionnel)
delete_file(file_path)