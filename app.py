from flask import Flask, render_template, request, redirect, session
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "segredo_muito_forte"

def carregar_treinamentos():
   with open("treinamentos.json", "r", encoding="utf-8") as f:
       return json.load(f)

def salvar_treinamentos(lista):
   with open("treinamentos.json", "w", encoding="utf-8") as f:
       json.dump(lista, f, indent=4)

@app.route("/")
def index():
   treinamentos = carregar_treinamentos()
   for t in treinamentos:
       # parse DD-MM-YYYY HH:MM
       t["data_hora"] = datetime.strptime(
           f"{t['data']} {t['horario']}",
           "%d-%m-%Y %H:%M"
       )
   treinamentos.sort(key=lambda x: x["data_hora"])
   return render_template("index.html", treinamentos=treinamentos)

@app.route("/login", methods=["GET", "POST"])
def login():
   if request.method == "POST":
       if request.form["senha"] == "quartzolit123":
           session["logado"] = True
           return redirect("/editar")
       else:
           return "<h2>Senha incorreta</h2><a href='/login'>Tentar novamente</a>"
   return render_template("login.html")

@app.route("/editar", methods=["GET", "POST"])
def editar():
   if not session.get("logado"):
       return redirect("/login")
   
   treinamentos = carregar_treinamentos()
   if request.method == "POST":
       if "excluir" in request.form:
           index = int(request.form["excluir"])
           if 0 <= index < len(treinamentos):
               treinamentos.pop(index)
               salvar_treinamentos(treinamentos)
       else:
           # converte o input YYYY-MM-DD para um datetime
           dt = datetime.strptime(request.form["data"], "%Y-%m-%d")
           # formata para DD-MM-YYYY
           data_br = dt.strftime("%d-%m-%Y")
           novo = {
             "tema":        request.form["tema"],
             "data":        data_br,
             "horario":     request.form["horario"],
             "setor":       request.form["setor"],
             "local":       request.form["local"],
             "responsavel": request.form["responsavel"]
           }
           treinamentos.append(novo)
           salvar_treinamentos(treinamentos)
       return redirect("/editar")
   return render_template("editar.html", treinamentos=treinamentos)

@app.route("/logout")
def logout():
   session.clear()
   return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
