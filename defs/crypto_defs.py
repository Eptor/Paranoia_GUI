import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# The base process was grabbed from the Docs:
# https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet


def encrypt(mode, data, password):
    """ Encrypts the data given by the user """

    salt = b'\xbd\x10\xcb\x8aK\x88Dw\xd8\x1b!\x909.\x07e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # Generates a secure password using the given password in the parameters
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    if mode == 'file':
        with open(data, 'rb') as file_encryption:
            text_from_file = file_encryption.read()
            # Encrypts the bytes grabbed above
            EncryptedToken = f.encrypt(text_from_file)
    elif mode == 'text':
        EncryptedToken = f.encrypt(data)
    return EncryptedToken


def decrypt(mode, data, password):
    """ Decrypts the data given by the user """

    salt = b'\xbd\x10\xcb\x8aK\x88Dw\xd8\x1b!\x909.\x07e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # Generates a secure password using the given password in the parameters
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    if mode == 'file':
        with open(data, 'rb') as file_encryption:
            text_from_file = file_encryption.read()
            # Decrypts the bytes grabbed above
            DecryptedToken = f.decrypt(text_from_file)
    elif mode == 'text':
        DecryptedToken = f.decrypt(data)
    return DecryptedToken
    