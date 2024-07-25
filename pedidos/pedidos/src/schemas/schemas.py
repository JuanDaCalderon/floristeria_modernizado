from typing import Union
from pydantic import BaseModel


class PedidosRegister(BaseModel):
    para: Union[str, None] = None
    de: Union[str, None] = None
    direccionEntrega: Union[str, None] = None
    pago: Union[bool, None] = None
    valor: Union[int, None] = None
    valorDomicilio: Union[int, None] = None
    fechaEntrega: Union[str, None] = None
    fechaCobro: Union[str, None] = None
    fechaGeneracion: Union[str, None] = None
    direccionCobro: Union[str, None] = None
    telefonoEntrega: Union[str, None] = None
    telefonoCobro: Union[str, None] = None
    entregado: Union[bool, None] = None
    hora: Union[str, None] = None
    comentario: Union[str, None] = None
    motivo: Union[str, None] = None
    cliente: Union[int, None] = None

    class Config:
        from_attributes = True
