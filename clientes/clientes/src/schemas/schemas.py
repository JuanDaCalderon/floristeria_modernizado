from typing import Union
from pydantic import BaseModel


class ClientesRegister(BaseModel):
    email: Union[str, None] = None
    numCliente: Union[str, None] = None
    nombre: Union[str, None] = None
    apellidos: Union[str, None] = None
    telefono: Union[str, None] = None
    celular: Union[str, None] = None

    class Config:
        from_attributes = True
