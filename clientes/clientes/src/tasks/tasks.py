from typing import TypedDict
from sqlalchemy.orm import Session
from ..models import models
from ..schemas import schemas
from ..utility import utility


class CreationCliente(TypedDict):
    cliente: models.Clientes
    token: str


def verify_if_cliente_already_exist(db: Session, email: str):
    cliente = db.query(models.Clientes).filter(models.Clientes.EMAIL == email).first()
    return cliente if cliente else False


def get_cliente_by_id(db: Session, idcliente: str):
    cliente = db.query(models.Clientes).filter(models.Clientes.IDCLIENTE == idcliente).first()
    return cliente if cliente else False


def get_access_token(email: str):
    return utility.generate_jwt(email)


def create_cliente(db: Session, cliente: schemas.ClientesRegister) -> CreationCliente:
    access_token = get_access_token(email=cliente.email.lower())
    new_cliente = models.Clientes(
        EMAIL=cliente.email.lower(),
        TELEFONO=cliente.telefono.lower(),
        NUMCLIENTE=cliente.numcliente.lower(),
        NOMBRE=cliente.nombre.lower(),
        APELLIDOS=cliente.apellidos.lower(),
        CELULAR=cliente.celular.lower()
    )
    db.add(new_cliente)
    db.commit()
    db.refresh(new_cliente)
    return dict(
        cliente=new_cliente,
        token=access_token,
    )


def reset_db(db: Session):
    db.query(models.Clientes).delete()
    db.commit()
