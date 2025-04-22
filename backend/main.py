from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def llegir_arrel():
    return {"missatge": "Servidor FastAPI operatiu - Backend de Benchmark Nova IA"}
