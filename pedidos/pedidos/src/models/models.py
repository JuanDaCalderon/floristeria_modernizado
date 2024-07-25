from sqlalchemy import BigInteger, Column, String, Boolean, Integer, DateTime
from ..database import database


class Pedidos(database.Base):
    __tablename__ = "PEDIDOS"
    IDPEDIDO = Column(BigInteger, primary_key=True, autoincrement=True)
    PARA = Column(String)
    DE = Column(String)
    DIRECCIONENTREGA = Column(String)
    PAGO = Column(Boolean)
    VALOR = Column(Integer)
    VALORDOMICILIO = Column(Integer)
    FECHAENTREGA = Column(DateTime)
    FECHACOBRO = Column(DateTime)
    FECHAGENERACION = Column(DateTime)
    DIRECCIONCOBRO = Column(String)
    TELEFONOENTREGA = Column(String)
    TELEFONOCOBRO = Column(String)
    ENTREGADO = Column(Boolean)
    HORA = Column(DateTime)
    COMENTARIO = Column(String)
    MOTIVO = Column(String)
    CLIENTE = Column(BigInteger)


database.Base.metadata.create_all(bind=database.engine)
