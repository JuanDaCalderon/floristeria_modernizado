from datetime import datetime
from sqlalchemy.orm import Session
from ..models import models
from ..schemas import schemas


def create_pedidos(db: Session, pedidos: schemas.PedidosRegister) -> models.Pedidos:
    date_format = '%Y-%m-%d'
    time_format = '%H:%M'
    new_pedido = models.Pedidos(
        PARA=pedidos.para.lower(),
        DE=pedidos.de.lower(),
        DIRECCIONENTREGA=pedidos.direccionEntrega.lower(),
        PAGO=pedidos.pago,
        VALOR=pedidos.valor,
        VALORDOMICILIO=pedidos.valorDomicilio,
        FECHAENTREGA=datetime.strptime(pedidos.fechaEntrega, date_format),
        FECHACOBRO=datetime.strptime(pedidos.fechaCobro, date_format),
        FECHAGENERACION=datetime.strptime(pedidos.fechaGeneracion, date_format),
        DIRECCIONCOBRO=pedidos.direccionCobro.lower(),
        TELEFONOCOBRO=pedidos.telefonoCobro.lower(),
        TELEFONOENTREGA=pedidos.telefonoEntrega.lower(),
        ENTREGADO=pedidos.entregado,
        HORA=datetime.strptime(pedidos.hora, time_format),
        COMENTARIO=pedidos.comentario.lower(),
        MOTIVO=pedidos.motivo.lower(),
        CLIENTE=pedidos.cliente
    )
    db.add(new_pedido)
    db.commit()
    db.refresh(new_pedido)
    return new_pedido


def reset_db(db: Session):
    db.query(models.Pedidos).delete()
    db.commit()
