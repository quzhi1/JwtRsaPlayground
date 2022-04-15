from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_rsa_files(file_name_prefix):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    unencrypted_pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    private_key_file = open(file_name_prefix + ".pem", "w")
    private_key_file.write(unencrypted_pem_private_key.decode())
    private_key_file.close()

    pem_public_key = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    public_key_file = open(file_name_prefix + ".pub", "w")
    public_key_file.write(pem_public_key.decode())
    public_key_file.close()