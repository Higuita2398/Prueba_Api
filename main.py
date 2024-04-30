from fastapi import FastAPI, HTTPException
from Rutas import experiencias
import requests

app = FastAPI()

app.include_router(experiencias.router, prefix="/api")

def obtener_imagen_aleatoria(palabra_clave: str):
    # Clave de API de Unsplash
    access_key = 'lxikk0yRMWKW_hyJen--yR0fe-qe7OJRqrZ6G_Sb-gQ'

    # URL del endpoint del API
    url = 'https://api.unsplash.com/photos/random'

    # Parámetros de la solicitud
    params = {'query': palabra_clave, 'client_id': access_key}

    try:
        # Realiza la solicitud al API de Unsplash
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lanza una excepción si hay un error en la solicitud

        # Procesa la respuesta
        data = response.json()
        imagen_aleatoria = data['urls']['regular']
        return imagen_aleatoria
    except requests.RequestException as e:
        # Si hay un error en la solicitud, lanza una excepción con un mensaje específico
        raise HTTPException(status_code=500, detail=f"No se pudo obtener la imagen aleatoria: {e}")

@app.get("/imagen-aleatoria/{palabra_clave}", response_model=dict)
async def obtener_imagen_aleatoria_por_palabra_clave(palabra_clave: str):
    imagen_aleatoria = obtener_imagen_aleatoria(palabra_clave)
    return {"imagen_aleatoria": imagen_aleatoria}
