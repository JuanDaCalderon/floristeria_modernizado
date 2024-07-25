from sqlalchemy import BigInteger, Column, String
from ..database import database


class Clientes(database.Base):
    __tablename__ = "CLIENTES"
    IDCLIENTE = Column(BigInteger, primary_key=True, autoincrement=True)
    EMAIL = Column(String, unique=True)
    NUMCLIENTE = Column(String)
    NOMBRE = Column(String)
    APELLIDOS = Column(String)
    TELEFONO = Column(String)
    CELULAR = Column(String)


database.Base.metadata.create_all(bind=database.engine)
