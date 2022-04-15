import jwt
import time
from generate_rsa import generate_rsa_files

def readFileAsStr(file_name):
    text_file = open(file_name, "r")
    data = text_file.read()
    text_file.close()
    return data

generate_rsa_files("example-rsa")
private_key = readFileAsStr('example-rsa.pem')
public_key = readFileAsStr('example-rsa.pub')

payload = {
    "iss": "service_a",
    "exp": time.time() + 24 * 3600, # Expire after a day
    "aud": "service_b",
    "iat": time.time(),
    "kid": "0.0.0", # RSA key version
}

encoded = jwt.encode(payload, private_key, algorithm="RS256")
print("JWT token: " + encoded)
decoded = jwt.decode(encoded, public_key, algorithms=["RS256"], audience="service_b")
print("Decoded payload:")
print(decoded)
