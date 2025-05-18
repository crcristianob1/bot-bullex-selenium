from bot import executar_bot, entradas_log
from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Bullex está rodando na nuvem com OCR, IA e estratégia Fibonacci..."

@app.route("/entradas")
def ver_entradas():
    if not entradas_log:
        return "Nenhuma entrada registrada ainda."
    return "<br>".join(entradas_log)

def iniciar_servidor():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor).start()
    executar_bot()
