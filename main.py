from fastapi import FastAPI, HTTPException
from Rutas import experiencias  # Importa el enrutador de experiencias
import requests

# Crea una instancia de FastAPI
app = FastAPI()

# Agrega el enrutador de experiencias a la aplicación principal con el prefijo /api
app.include_router(experiencias.router, prefix="/api")

# Función para obtener una imagen aleatoria de Unsplash
def obtener_imagen_aleatoria(palabra_clave: str):
    access_key = 'lxikk0yRMWKW_hyJen--yR0fe-qe7OJRqrZ6G_Sb-gQ'  # Clave de API de Unsplash
    url = 'https://api.unsplash.com/photos/random'  # URL del endpoint del API

    # Parámetros de la solicitud
    params = {'query': palabra_clave, 'client_id': access_key}

    try:
        # Realiza la solicitud al API de Unsplash
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lanza una excepción si hay un error en la solicitud

        # Procesa la respuesta y devuelve la URL de la imagen regular
        data = response.json()
        imagen_aleatoria = data['urls']['regular']
        return imagen_aleatoria
    except requests.RequestException as e:
        # Si hay un error en la solicitud, lanza una excepción con un mensaje específico
        raise HTTPException(status_code=500, detail=f"No se pudo obtener la imagen aleatoria: Error en la solicitud a Unsplash")

# Ruta para obtener una imagen aleatoria por palabra clave
@app.get("/imagen-aleatoria/{palabra_clave}", response_model=dict)
async def obtener_imagen_aleatoria_por_palabra_clave(palabra_clave: str):
    imagen_aleatoria = obtener_imagen_aleatoria(palabra_clave)
    return {"imagen_aleatoria": imagen_aleatoria}
