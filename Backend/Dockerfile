FROM python:3.10-alpine

# RUN apt-get update && apt-get upgrade -qqy
WORKDIR /app 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]