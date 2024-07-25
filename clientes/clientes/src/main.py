from dotenv import find_dotenv, load_dotenv
from fastapi import Body, FastAPI, status, Depends
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from operator import itemgetter
from sqlalchemy.orm import Session
from .database import database

from .schemas import schemas
from .tasks import tasks
from .utility import utility

env_file = find_dotenv('.env.clientes')
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


@app.post("/cliente/new", status_code=status.HTTP_201_CREATED)
def create_clientes(cliente: schemas.ClientesRegister = Body(default=None), db: Session = Depends(database.get_db)):
    if not cliente:
        return utility.get_json_response('E422', 'El body de la petición esta vacio')
    elif not cliente.email or not cliente.numCliente or not cliente.nombre or not cliente.apellidos or not cliente.celular or not cliente.telefono:
        return utility.get_json_response('E400', 'email, numcliente, nombre, apellidos, celular y telefono son campos obligatorios')
    elif not utility.is_valid_email(cliente.email):
        return utility.get_json_response('E400', 'El email no tiene el formato correcto')
    else:
        email = cliente.email
        cliente_db = tasks.verify_if_cliente_already_exist(db=db, email=email)
        if cliente_db:
            return utility.get_json_response('E412', 'Este cliente ya existe con este email')
        else:
            cliente, token = itemgetter('cliente', 'token')(tasks.create_cliente(db=db, cliente=cliente))
            return {
                "IDCLIENTE": cliente.IDCLIENTE,
                "EMAIL": cliente.EMAIL,
                "NUMCLIENTE": cliente.NUMCLIENTE,
                "NOMBRE": cliente.NOMBRE,
                "APELLIDOS": cliente.APELLIDOS,
                "TELEFONO": cliente.TELEFONO,
                "CELULAR": cliente.CELULAR,
                "TOKEN": token,
            }

@app.get("/cliente/ping", status_code=status.HTTP_200_OK)
def verify_health_clientes():
    return {"msg": "Pong"}

@app.get("/cliente/{idcliente}", status_code=status.HTTP_200_OK)
def get_cliente(idcliente: str, db: Session = Depends(database.get_db)):
    cliente = tasks.get_cliente_by_id(db=db, idcliente=idcliente)
    if not cliente:
        return utility.get_json_response('E404', f"El Cliente con el Id {idcliente} no fue encontrado")
    else:
        return cliente



@app.post("/cliente/reset", status_code=status.HTTP_200_OK)
def reset_clientes(db: Session = Depends(database.get_db)):
    tasks.reset_db(db=db)
    return {"msg": "Todos los clientes fueron eliminados"}
