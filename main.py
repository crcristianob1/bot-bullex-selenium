from flask import Flask
import threading
from bot import executar_bot, get_entradas_log

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Bullex está rodando na nuvem com OCR, IA e estratégia Fibonacci..."

@app.route('/entradas')
def mostrar_entradas():
    return "<br>".join(get_entradas_log())

def iniciar_servidor():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor).start()
    executar_bot()
