#!/usr/bin/env python3

from private import PrivateKey
from public import PublicKey
from csr import CSR
from sign import SignedKey

if __name__ == "__main__":
    # Generate CA's private key
    ca_private_key = PrivateKey.generate()
    ca_private_key.save("PrivateP@assw0rd", "ca-private-key.pem")

    # Generate CA's public key
    name_dict = {"country": "IN",
                 "state": "Karnatak",
                 "locality": "BTM",
                 "org": "Sachin certificate authority",
                 "hostname": "sachin.example.com"}
    ca_public_key = PublicKey.generate(ca_private_key, name_dict)
    ca_public_key.save("ca-public-key.pem")

    # Generate private key for server
    server_private_key = PrivateKey.generate()
    server_private_key.save("ServerP@ssw0rd", "server-private-key.pem")

    # Generate CSR
    name_dict = {"country": "IN",
                 "state": "Bihar",
                 "locality": "Badka Diyan",
                 "org": "Sachin Co",
                 "hostname": "sachin1.example.com"}

    alt_names = ["localhost", "sachin1.example.com"]
    csr = CSR.generate(server_private_key, alt_names, name_dict)
    csr.save("server-csr.pem")

    # CA signs CSR, creating server's certificate / public key.
    signed_key = SignedKey.generate(csr,
                                    ca_public_key,
                                    ca_private_key)
    signed_key.save("server-public-key.pem")
