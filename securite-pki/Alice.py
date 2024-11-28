from helper import *
from CertificateAuthority import CA
from Horodateur import Horodateur
import logging

class Alice:
    def __init__ (self, mydoc, certAuthrity:CA):
        self.logger = logging.getLogger(__name__)
        
        self.name = "Alice"
        self.mydoc = mydoc
        
        self.privateKey, self.publicKey = generateRSAKeys()
        self.logger.info("Generated RSA key")
        
        self.certificate = certAuthrity.createCertificateForClient(self.publicKey, self.name)
        self.logger.info("Certificate received")
        
        self.logger.info("Alice Ready")
    
    def getProof(self, h:Horodateur):
        self.proof = h.generateProof(self.mydoc, self.certificate)
        