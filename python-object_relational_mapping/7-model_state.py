#!/usr/bin/python3
"""
Définition du modèle State pour SQLAlchemy ORM
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Création de la classe de base pour tous les modèles
Base = declarative_base()


class State(Base):
    """
    Modèle représentant un état dans la base de données

    Attributes:
        id (int): Identifiant unique de l'état (clé primaire)
        name (str): Nom de l'état (jusqu'à 128 caractères)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
