FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install django
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
