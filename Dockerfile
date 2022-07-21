FROM python:3.10

WORKDIR /workspace

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "127.0.0.1", "--port", "80", "--reload"]
