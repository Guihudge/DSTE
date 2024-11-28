from cryptography.hazmat.primitives.asymmetric import rsa

def generateRSAKeys():
    privateKey = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    publicKey = privateKey.public_key()
    return privateKey,publicKey
