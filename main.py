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
from flask import send_file
import matplotlib.pyplot as plt
import io

@app.route('/entradas')
def mostrar_grafico():
    plt.clf()
    plt.figure(figsize=(10, 4))
    plt.title("Entradas Executadas")
    plt.plot(range(len(entradas_log)), list(range(len(entradas_log))), marker='o')
    plt.xlabel("Entrada")
    plt.ylabel("Número")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')
