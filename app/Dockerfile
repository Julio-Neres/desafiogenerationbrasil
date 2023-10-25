
FROM python:3.8


WORKDIR /app

COPY . .


RUN pip install Flask Flask-SQLAlchemy psycopg2 flasgger


EXPOSE 8080

CMD ["python", "app.py"]