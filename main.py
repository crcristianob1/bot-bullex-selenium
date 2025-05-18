from bot import executar_bot
from flask import Flask, send_file
import threading
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import requests
import time

app = Flask(__name__)
log_path = "logs.csv"

@app.route("/")
def home():
    return "Bot Bullex está rodando na nuvem com OCR, IA e estratégia Fibonacci..."

@app.route("/grafico")
def gerar_grafico():
    try:
        df = pd.read_csv(log_path)
        contagem = df["resultado"].value_counts()

        fig, ax = plt.subplots()
        ax.pie(contagem, labels=contagem.index, autopct='%1.1f%%')
        ax.set_title("Resultados: Win vs Loss")
        fig.savefig("grafico.png")

        return send_file("grafico.png", mimetype='image/png')
    except Exception as e:
        return f"Erro ao gerar gráfico: {e}"

@app.route("/registrar/<par>/<resultado>")
def registrar(par, resultado):
    registrar_entrada(par, resultado)
    return f"Entrada registrada: {par} - {resultado}"

def registrar_entrada(par, resultado, tipo="Compra"):
    dados = {
        "horario": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "par": [par],
        "resultado": [resultado],
        "tipo": [tipo]
    }

    df_novo = pd.DataFrame(dados)
    try:
        df_antigo = pd.read_csv(log_path)
        df_total = pd.concat([df_antigo, df_novo], ignore_index=True)
    except FileNotFoundError:
        df_total = df_novo

    df_total.to_csv(log_path, index=False)

def manter_ativo():
    while True:
        try:
            requests.get("https://bot-bullex-selenium-4.onrender.com/")
        except:
            pass
        time.sleep(600)

if __name__ == "__main__":
    threading.Thread(target=executar_bot).start()
    threading.Thread(target=manter_ativo).start()
    app.run(host="0.0.0.0", port=10000)
