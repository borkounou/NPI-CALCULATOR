# Stage 1 - Builder 
FROM python:3.10.12 as builder


WORKDIR /app 

COPY app/requirements.txt .

RUN pip install --co-cache-dir -r requirements.txt

# RUN apt-get update && apt-get upgrade -qqy

RUN python -m pip install requests numpy gunicorn pandas Jinja2 && pip install fastapi && pip install python-multipart && pip install "uvicorn[standard]"


# Stage - Production build
FROM python:3.10.12

WORKDIR /app 

COPY --from=builder /usr/local/lib/python3.10.12/site-packages /usr/local/lib/python3.10.12/site-package

COPY app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
