from helper import *
from CertificateAuthority import CA
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import logging, datetime


class Horodateur:
    def __init__ (self, certAuthrity:CA):
        self.logger = logging.getLogger(__name__)
        
        self.privateKey, self.publicKey = generateRSAKeys()
        self.logger.info("Generated RSA key")
        
        self.certificate = certAuthrity.createCertificateForClient(self.publicKey, __name__)
        self.logger.info("Certificate received")
        
        self.logger.info("{} Ready".format(__name__))
    
    def generateProof(self, docHash, signerCert):
        self.logger.info("Generated signature proof")
        date = datetime.datetime.now(datetime.timezone.utc)
        proof = {'date': date, 'hash':docHash, 'cert':signerCert}
        
        s = self.privateKey.sign(bytearray(str(proof), "utf-8"), padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256())
        
        out = {'proof':proof, 'signature':s}
        return out


