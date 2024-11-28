from helper import *
from cryptography import x509
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.x509 import NameOID
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
import datetime
import logging


class CA:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # On crée les clé Privé/Public
        self.privateKey, self.publicKey = generateRSAKeys()
        self.logger.info("RSA key par generated")
        

        # On génère le certificat racine pour l'autorité
        subject = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, "FR"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Very Secure CA"),
            x509.NameAttribute(NameOID.COMMON_NAME, "VerySecure.local"),
        ])
        self.ca_certificate = x509.CertificateBuilder().subject_name(subject).issuer_name(subject).public_key(self.publicKey).serial_number(x509.random_serial_number()).not_valid_before(datetime.datetime.utcnow()).not_valid_after(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365)).sign(self.privateKey, SHA256())
        self.logger.info("Root cetificat generated")
        self.logger.info("CA Ready")

    def createCertificateForClient(self, clientPubKey:RSAPublicKey, clientName:str):
        subject = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, "FR"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, clientName),
            x509.NameAttribute(NameOID.COMMON_NAME, clientName+".local"),
        ])
        certificate = x509.CertificateBuilder()\
        .subject_name(subject)\
        .issuer_name(self.ca_certificate.subject)\
        .public_key(clientPubKey)\
        .serial_number(x509.random_serial_number())\
        .not_valid_before(datetime.datetime.utcnow())\
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))\
        .sign(self.privateKey, SHA256())
        self.logger.info("Cretifacte delivered to {}".format(clientName))
        return certificate