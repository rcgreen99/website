FROM python:3.10

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p /var/sockets

EXPOSE 8000

CMD ["uvicorn", "src.main:web_app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--uds", "/var/sockets/uvicorn.sock"]

# local run
# CMD ["uvicorn", "src.main:web_app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
