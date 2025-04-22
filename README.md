# 📊 Amazon Nova Autoconsciència Benchmark (Demo)

Aquest projecte és una eina de **benchmark, visualització i avaluació** d'intel·ligència artificial centrada en els models **Amazon Nova**, dins l'entorn **AWS Bedrock**.

> 🧪 Aquesta versió és **només una demo**:
> - Limitada a 5 preguntes per sessió
> - Sense persistència de dades real
> - Pensada per mostrar el potencial del sistema

## 🔧 Estructura del sistema

### 1. Backend amb FastAPI (`backend/main.py`)
- Fa preguntes al model seleccionat
- Recull puntuació humana
- Avalua la resposta amb una altra IA

### 2. Frontend (`frontend/`)
- Formulari per preguntar i puntuar (HTML)
- Interfícies visuals per veure gràfics de sessions
- Selecció de sessions, filtres per data i model

### 3. Visualització (`visualitzador/visualitzador_benchmark_ia.py`)
- Analitza els resultats i genera:
  - Gràfic global
  - Gràfics per sessió
  - Pàgina de filtre per model/data
  - Pàgina index.html amb tots els gràfics incrustats

## ▶️ Com executar

### Prerequisits:
- Python 3.10+
- AWS CLI configurat amb accés a Bedrock
- Paquets Python:
```bash
pip install fastapi uvicorn boto3 pandas plotly
```

### Backend:
```bash
cd backend
uvicorn main:app --reload
```

### Frontend:
Obre `frontend/index.html` al navegador

### Anàlisi:
```bash
cd visualitzador
python visualitzador_benchmark_ia.py
```

## 📈 Escalabilitat

Aquest projecte pot evolucionar fàcilment en:
- Una aplicació amb base de dades
- Un panell interactiu en Streamlit/Dash
- Un sistema automatitzat de benchmarking per comparativa contínua entre models

## 📣 Centrat en Amazon Nova

Totes les proves i consultes es basen principalment en els models **Nova d'Amazon**, pensats per ser avaluats en el seu nivell de comprensió, autoconsciència i resposta davant preguntes específiques de consciència i identitat.
