FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY pedidos /app/pedidos

EXPOSE 8001

CMD ["python", "pedidos/main.py"]