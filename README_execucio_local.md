# ▶️ Execució local del projecte Amazon Nova Autoconsciència Benchmark (Demo)

Aquesta guia explica pas a pas com posar en marxa aquest projecte de forma local per fer proves amb 5 preguntes i visualitzar les respostes i puntuacions.

---

## 1. Clonar el projecte

```bash
git clone https://github.com/EL_TEU_USUARI/amazon-nova-autoconsciencia-benchmark.git
cd amazon-nova-autoconsciencia-benchmark
```

---

## 2. Crear un entorn virtual i instal·lar dependències

```bash
python -m venv venv
source venv/bin/activate  # O bé .\venv\Scripts\activate al Windows
pip install -r requirements.txt
```

---

## 3. Executar el servidor FastAPI (backend)

```bash
cd backend
uvicorn main:app --reload
```

Accedeix a la documentació automàtica:
👉 http://127.0.0.1:8000/docs

---

## 4. Obrir la interfície (frontend)

Obre amb el navegador el fitxer:

```
frontend/index.html
```

---

## 5. Analitzar resultats

Executa el script de visualització:

```bash
cd visualitzador
python visualitzador_benchmark_ia.py
```

Això generarà:
- Gràfics `.html` per sessió i globals
- `index.html` amb galeria visual
- `filtrat_selector.html` per aplicar filtres per data o model

---

## 6. Consultar resultats

Obre el fitxer:

```
visualitzador/index.html
```

---

## ✅ Notes finals

- Només hi ha 5 preguntes per sessió per simplificar la demo.
- El sistema es pot escalar amb base de dades, múltiples models, sessions per usuari, etc.

---

Per qualsevol dubte o millora, contacta amb l'autor del projecte o obre un issue al repositori GitHub.
