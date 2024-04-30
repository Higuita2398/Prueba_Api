from fastapi import APIRouter, HTTPException, Path
from typing import List

# Se crea un enrutador APIRouter para las rutas relacionadas con experiencias
router = APIRouter()

# Datos dummy para inicializar el API
experiencias = [
    {
        "id": 1,
        "nombre": "EXPLORAMÓVIL",
        "descripcion": "Salimos del museo y llevamos las experiencias interactivas y actividades experimentales hasta tu colegio para promover el desarrollo de competencias científicas y ciudadanas.",
        "sala": 1,
        "imagen": "https://www.parqueexplora.org/_next/image?url=https%3A%2F%2Fimgix.cosmicjs.com%2Ff22381a0-b785-11ed-a33c-958e5b2068f9-6-Thumb-exploramovil.jpg%3Ffit%3Dcrop%26w%3D490%26h%3D255&w=1920&q=75"
    },
    {
        "id": 2,
        "nombre": "DOMO PORTATIL",
        "descripcion": "Explora actividades nuevas en tu colegio navegando por el universo a través de un domo inflable. Aprenderán sobre las constelaciones, el origen del universo, viajarán entre planetas y mucho más. Con un sistema digital podrán visualizar los shows de astronomía del Planetario de Medellín.",
        "sala": 2,
        "imagen": "https://www.parqueexplora.org/_next/image?url=https%3A%2F%2Fimgix.cosmicjs.com%2F83f8e160-b786-11ed-a33c-958e5b2068f9-7-thumb-domo.jpg%3Ffit%3Dcrop%26w%3D490%26h%3D255&w=1920&q=75"
    },
    {
        "id": 3,
        "nombre": "PANTALLA INFLABLE",
        "descripcion": "Vive una experiencia diferente en tu  colegio viajando por el espacio a través de una pantalla inflable de gran formato. ¡Aprenderás sobre el origen del sistema solar, las constelaciones, la estructura del universo y más!",
        "sala": 3,
        "imagen": "https://www.parqueexplora.org/_next/image?url=https%3A%2F%2Fimgix.cosmicjs.com%2F55b66fe0-af65-11ec-b9ac-8518f92a3fbe-pantalla-inflable.jpg%3Ffit%3Dcrop%26w%3D490%26h%3D255&w=1920&q=75"
    }
]

# Ruta para obtener todas las experiencias
@router.get("/experiencias/", response_model=List[dict])
async def listar_experiencias():
    return experiencias

# Ruta para crear una nueva experiencia
@router.post("/experiencias/", response_model=dict)
async def crear_experiencia(nombre: str, descripcion: str, sala: int, imagen: str = None):
    nueva_experiencia = {
        "id": len(experiencias) + 1,
        "nombre": nombre,
        "descripcion": descripcion,
        "sala": sala,
        "imagen": imagen
    }
    experiencias.append(nueva_experiencia)
    return nueva_experiencia

# Ruta para obtener una experiencia por su ID
@router.get("/experiencias/{experiencia_id}", response_model=dict)
async def obtener_experiencia(experiencia_id: int = Path(..., title="ID de la experiencia")):
    for exp in experiencias:
        if exp["id"] == experiencia_id:
            return exp
    raise HTTPException(status_code=404, detail="Experiencia no encontrada")

# Ruta para actualizar una experiencia por su ID
@router.put("/experiencias/{experiencia_id}", response_model=dict)
async def actualizar_experiencia(experiencia_id: int, nombre: str, descripcion: str, sala: int, imagen: str = None):
    for exp in experiencias:
        if exp["id"] == experiencia_id:
            exp.update({"nombre": nombre, "descripcion": descripcion, "sala": sala, "imagen": imagen})
            return exp
    raise HTTPException(status_code=404, detail="Experiencia no encontrada")

# Ruta para eliminar una experiencia por su ID
@router.delete("/experiencias/{experiencia_id}")
async def borrar_experiencia(experiencia_id: int):
    for i, exp in enumerate(experiencias):
        if exp["id"] == experiencia_id:
            del experiencias[i]
            return {"message": "Experiencia eliminada"}
    raise HTTPException(status_code=404, detail="Experiencia no encontrada")

# Ruta para obtener experiencias filtradas por el número de sala
@router.get("/experiencias/salas/{nombre}", response_model=List[dict])
async def experiencias_por_sala(id: int):
    return [exp for exp in experiencias if exp["sala"] == id]
