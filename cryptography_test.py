#pip install cryptography
#Asymmetic Encryption
#Source: nitratine.net

import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
public_key = private_key.public_key()

# Storing the keys

pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
with open('private_key.pem', 'wb') as f:
    f.write(pem)

pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
with open('public_key.pem', 'wb') as f:
    f.write(pem)

# Reading the keys back in (in other modules)
with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

# Encrypting: in main module
f = open('test.txt', 'rb')
message = f.read()
f.close()

encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
f = open('test.encrypted', 'wb')
f.write(encrypted)
f.close()


#Decrypting: in modules
f = open('test.encrypted', 'rb')
decrypted_message = f.read()
f.close()

original_message = private_key.decrypt(
        decrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

f = open('decrypted_message.txt', 'wb')
f.write(original_message)
f.close()