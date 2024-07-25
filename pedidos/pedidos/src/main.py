from dotenv import find_dotenv, load_dotenv
from fastapi import Body, FastAPI, status, Depends
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import requests
from .database import database
from .models import models

from .schemas import schemas
from .tasks import tasks
from .utility import utility


env_file = find_dotenv('.env.pedidos')
loaded = load_dotenv(env_file)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return RedirectResponse(url="/docs/")


@app.post("/pedido/new", status_code=status.HTTP_201_CREATED)
def create_pedido(pedido: schemas.PedidosRegister = Body(default=None), db: Session = Depends(database.get_db)):
    if not pedido:
        return utility.get_json_response('E422', 'El body de la petición esta vacio')
    elif not pedido.para or not pedido.de or not pedido.cliente or not pedido.motivo:
        return utility.get_json_response('E400', 'de, para, cliente y motivo son campos obligatorios')
    else:
        response = requests.get(f'http://localhost:8000/cliente/'+str(pedido.cliente))
        if response.status_code == 200:
            pedido: models.Pedidos = tasks.create_pedidos(db=db, pedidos=pedido)
            return {
                "IDPEDIDO": pedido.IDPEDIDO,
                "PARA": pedido.PARA,
                "DE": pedido.DE,
                "DIRECCIONENTREGA": pedido.DIRECCIONENTREGA,
                "PAGO": pedido.PAGO,
                "VALOR": pedido.VALOR,
                "VALORDOMICILIO": pedido.VALORDOMICILIO,
                "FECHAENTREGA": pedido.FECHAENTREGA,
                "FECHACOBRO": pedido.FECHACOBRO,
                "FECHAGENERACION": pedido.FECHAGENERACION,
                "DIRECCIONCOBRO": pedido.DIRECCIONCOBRO,
                "TELEFONOCOBRO": pedido.TELEFONOCOBRO,
                "TELEFONOENTREGA": pedido.TELEFONOENTREGA,
                "ENTREGADO": pedido.ENTREGADO,
                "HORA": pedido.HORA,
                "COMENTARIO": pedido.COMENTARIO,
                "MOTIVO": pedido.MOTIVO,
                "CLIENTE": response.json(),
            }
        else:
            return utility.get_json_response('E404', f"El Cliente con el Id {pedido.cliente} no fue encontrado para crear este pedido")


@app.get("/pedido/ping", status_code=status.HTTP_200_OK)
def verify_health_pedido():
    return {"msg": "Pong"}


@app.post("/pedido/reset", status_code=status.HTTP_200_OK)
def reset_pedidos(db: Session = Depends(database.get_db)):
    tasks.reset_db(db=db)
    return {"msg": "Todos los pedidos fueron eliminados"}
