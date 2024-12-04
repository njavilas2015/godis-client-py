from main import client

host: str = "localhost"
port: int = 6480

response: str = client(host, port, "HSET food country ar")

print(f"Respuesta del servidor: {response}")

response: str = client(host, port, "HGET food country")

print(f"Respuesta del servidor: {response}")