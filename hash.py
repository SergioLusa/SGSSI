import os
import hashlib
import sys

OG = sys.argv[1]
CARPETA = sys.argv[2]

print(OG)

print("Original")

for nombreFoto in os.listdir(CARPETA):
    rutaCompleta = os.path.join(CARPETA, nombreFoto)

    with open(rutaCompleta, 'rb') as archivo:
        md5_hash = hashlib.md5()
        while True:
            data = archivo.read(8192)
            if not data:
                break
            md5_hash.update(data)

    res = md5_hash.hexdigest()

    if res == OG:
        print(nombreFoto)
        sys.exit(0)

sys.exit(1)
