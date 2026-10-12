import os
import socket
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host=os.getenv("REDIS_HOST", "db-service"), port=6379)

@app.route("/")
def hello():
    hits = cache.incr("hits")
    return f"Bonjour ! Cette page a été vue {hits} fois. Je suis le conteneur {socket.gethostname()}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("APP_PORT", "5000")))
