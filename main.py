from bot import executar_bot
from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Bullex está rodando na nuvem com OCR, IA e estratégia Fibonacci..."

def iniciar_servidor():
    port = int(os.environ.get("PORT", 10000))  # Porta dinâmica da Render
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    print("[INIT] Iniciando bot Bullex na nuvem...")
    print("[LOG] Bot rodando com OCR, IA e estratégia Fibonacci...")
    print("[LOG] Avaliando gráfico, aplicando análise técnica e IA...")
    threading.Thread(target=iniciar_servidor).start()
    executar_bot()
