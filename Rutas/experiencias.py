from fastapi import APIRouter, HTTPException, Path
from typing import List

router = APIRouter()

# Datos dummy para inicializar el API
experiencias = [
    {
        "id": 1,
        "nombre": "Experiencia 1",
        "descripcion": "Descripción de la Experiencia 1",
        "sala": 1,
        "imagen": "imagen1.jpg"
    },
    {
        "id": 2,
        "nombre": "Experiencia 2",
        "descripcion": "Descripción de la Experiencia 2",
        "sala": 2,
        "imagen": "imagen2.jpg"
    }
]

@router.get("/experiencias/", response_model=List[dict])
async def listar_experiencias():
    return experiencias

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

@router.get("/experiencias/{experiencia_id}", response_model=dict)
async def obtener_experiencia(experiencia_id: int = Path(..., title="ID de la experiencia")):
    for exp in experiencias:
        if exp["id"] == experiencia_id:
            return exp
    raise HTTPException(status_code=404, detail="Experiencia no encontrada")

@router.put("/experiencias/{experiencia_id}", response_model=dict)
async def actualizar_experiencia(experiencia_id: int, nombre: str, descripcion: str, sala: int, imagen: str = None):
    for exp in experiencias:
        if exp["id"] == experiencia_id:
            exp.update({"nombre": nombre, "descripcion": descripcion, "sala": sala, "imagen": imagen})
            return exp
    raise HTTPException(status_code=404, detail="Experiencia no encontrada")

@router.delete("/experiencias/{experiencia_id}")
async def borrar_experiencia(experiencia_id: int):
    for i, exp in enumerate(experiencias):
        if exp["id"] == experiencia_id:
            del experiencias[i]
            return {"message": "Experiencia eliminada"}
    raise HTTPException(status_code=404, detail="Experiencia no encontrada")

@router.get("/experiencias/salas/{nombre}", response_model=List[dict])
async def experiencias_por_sala(nombre: int):
    return [exp for exp in experiencias if exp["sala"] == nombre]
