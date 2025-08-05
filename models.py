# models.py

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import datetime

class UnidadTransporte(Base):
    __tablename__ = "unidades_transporte"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)

    eventos = relationship("Evento", back_populates="unidad")

class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True, index=True)
    id_unidad = Column(Integer, ForeignKey("unidades_transporte.id"))
    pasajeros = Column(Integer)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    unidad = relationship("UnidadTransporte", back_populates="eventos")
