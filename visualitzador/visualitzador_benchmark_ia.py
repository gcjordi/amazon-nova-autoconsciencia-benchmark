import pandas as pd
import plotly.express as px
import glob
from datetime import datetime
import os

# Carrega tots els fitxers CSV de resultats
fitxers = glob.glob("resultats_*.csv")

# Llegeix i concatena tots els fitxers en un DataFrame amb identificador de sessió i data
avui = datetime.today().date()
dades = []

for fitxer in fitxers:
    df = pd.read_csv(fitxer)
    sessio_id = fitxer.replace("resultats_", "").replace(".csv", "")
    df["sessio_id"] = sessio_id
    df["data"] = avui
    dades.append(df)

# Combina totes les dades
df_total = pd.concat(dades, ignore_index=True) if dades else pd.DataFrame()

# Crea interfície web simple per selecció de filtre
if not df_total.empty:
    df_total['puntuacio_ia'] = pd.to_numeric(df_total['puntuacio_ia'], errors='coerce')
    models_disponibles = sorted(df_total['model_usuari'].unique())
    dates_disponibles = sorted(df_total['data'].astype(str).unique())

    with open("filtrat_selector.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n<html lang='ca'>\n<head><meta charset='UTF-8'><title>Filtre de Resultats IA</title>")
        f.write("<style>body{font-family:sans-serif;max-width:800px;margin:20px auto;padding:20px;}select,button{font-size:1rem;margin-top:10px;}iframe{width:100%;height:600px;margin-top:20px;border:none;}</style>")
        f.write("</head><body><h1>Filtrar Resultats IA</h1>")

        f.write("<label for='model'>Model:</label><select id='model'>")
        for model in models_disponibles:
            f.write(f"<option value='{model}'>{model}</option>")
        f.write("</select><br>")

        f.write("<label for='data'>Data:</label><select id='data'>")
        for data in dates_disponibles:
            f.write(f"<option value='{data}'>{data}</option>")
        f.write("</select><br>")

        f.write("<button onclick='carregarGrafica()'>Aplicar filtre</button>")
        f.write("<iframe id='grafic' src=''></iframe>")

        f.write("<script>")
        f.write("function carregarGrafica() { const model = document.getElementById('model').value; const data = document.getElementById('data').value; const url = `filtrat_${model.replace(/[^a-zA-Z0-9]/g, '')}_${data}.html`; document.getElementById('grafic').src = url; }")
        f.write("</script></body></html>")

    print("✅ Pàgina de selecció de filtre generada: filtrat_selector.html")

    # Genera tots els gràfics filtrats
    for model in models_disponibles:
        for data in dates_disponibles:
            df_filtrat = df_total[(df_total['model_usuari'] == model) & (df_total['data'].astype(str) == data)]
            if not df_filtrat.empty:
                resum = df_filtrat.groupby("model_usuari").agg(
                    preguntes=('pregunta', 'count'),
                    mitjana_huma=('puntuacio_humana', 'mean'),
                    mitjana_ia=('puntuacio_ia', 'mean')
                ).reset_index()
                fig = px.bar(resum, x="model_usuari", y=["mitjana_huma", "mitjana_ia"], barmode="group",
                             title=f"Model: {model} | Data: {data}")
                fitxer_html = f"filtrat_{model.replace(' ', '').replace('-', '').replace('.', '')}_{data}.html"
                fig.write_html(fitxer_html)
                print(f"🔹 Gràfic exportat: {fitxer_html}")
else:
    print("⚠️ No s'han trobat dades per generar gràfics filtrats.")
