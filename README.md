# Certificate-generation-Htpps

- Intall the dependencies from ***requirements.tsxt***
- cmd: chmod +x generate_key.py
- Run ***generate_key.py*** to generate the keys.
- cmd: chmod +x server.py 
- Run ***server.py*** to run the flask server.
- Run the below command to test the https secured connections. 
- curl --cacert ca-public-key.pem https://localhost:port/
