from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
import crud
import schemas_app as schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/evento", response_model=schemas.OcupacionOut)
def registrar_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    return crud.crear_evento(db, evento)

@app.get("/ocupacion/{id_unidad}", response_model=schemas.OcupacionOut)
def leer_ocupacion(id_unidad: int, db: Session = Depends(get_db)):
    return crud.obtener_ocupacion_actual(db, id_unidad)

@app.get("/alertas/{id_unidad}", response_model=list[schemas.AlertaOut])
def leer_alertas(id_unidad: int, db: Session = Depends(get_db)):
    return crud.obtener_alertas(db, id_unidad)
