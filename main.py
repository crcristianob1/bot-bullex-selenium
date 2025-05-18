from bot import executar_bot
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Bullex está rodando!"

def iniciar_servidor():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor).start()
    executar_bot()
