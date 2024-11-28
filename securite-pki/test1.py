import Alice, CertificateAuthority, Horodateur
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


verySecure = CertificateAuthority.CA()
alice = Alice.Alice("My very own document actualy!", verySecure)
horodateur = Horodateur.Horodateur(verySecure)
alice.getProof(horodateur)
print(alice.proof)