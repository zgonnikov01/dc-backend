FROM python:3.10

RUN mkdir /code 

WORKDIR /code

COPY requirements.txt .

#RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install --upgrade -r requirements.txt

COPY . .

WORKDIR app

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
