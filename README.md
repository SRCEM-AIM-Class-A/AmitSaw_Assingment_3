Web Applications with Flask, Django, and Docker Compose

Overview
This project involves creating two web applications: one using Flask and the other using Django. 
The goal is to learn how to build basic web applications, integrate databases, create forms, and handle errors.
Additionally, the project will cover containerization of both applications using Docker and Docker Compose for deployment.

Project Structure
The project consists of three main parts:
1. Flask Application
2. Django Application
3. Docker Compose Setup

Instructions to Run the Project

1. Cloning the Repository

git clone https://github.com/yourusername/web-applications-flask-django-docker.git
cd web-applications-flask-django-docker

2. Setting Up the Flask Application

The Flask application has two routes:
- A homepage route that displays a "Hello, World!" message.
- A second route that accepts the user's name and age via a form and displays a greeting message.
- Error handling for invalid inputs.

cd flask-app

Install dependencies
pip install -r requirements.txt

Run the Flask application
python app.py

The Flask app should now be running at http://localhost:5000

3. Setting Up the Django Application

The Django application includes:
- A homepage that lists items (books/tasks/products).
- An admin panel to add or modify items.
- A form on the homepage to add new items to the list.

cd django-app

Set up the virtual environment
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

Install dependencies
pip install -r requirements.txt

Apply database migrations
python manage.py migrate

Create a superuser for the admin panel
python manage.py createsuperuser

Run the Django application
python manage.py runserver

The Django app should now be running at http://localhost:8000

4. Setting Up Docker and Docker Compose

Both Flask and Django applications are containerized using Docker. 
The following steps will help you set up Docker Compose to manage both applications.

Dockerize Flask Application:
In the flask-app directory, create a Dockerfile that defines the container image for the Flask app.

Dockerize Django Application:
In the django-app directory, create a Dockerfile that defines the container image for the Django app.

Create Docker Compose File:
In the root directory of the project, create a docker-compose.yml file to orchestrate the Flask and Django containers.

Build and start containers using Docker Compose
docker-compose up --build

This command will build and start both the Flask and Django applications in separate containers.

To access the applications:
- Flask will be available at http://localhost:5000
- Django will be available at http://localhost:8000

5. Accessing the Admin Panel for Django

To access the Django admin panel:
1. Visit http://localhost:8000/admin
2. Log in using the superuser credentials created during the setup process.

6. Pushing to Docker Hub

Once you have built the Docker images for both applications, you can push them to Docker Hub:

Log in to Docker Hub
docker login

Tag the Flask image
docker tag flask-app yourdockerhubusername/flask-app:latest

Push the Flask image to Docker Hub
docker push yourdockerhubusername/flask-app:latest

Tag the Django image
docker tag django-app yourdockerhubusername/django-app:latest

Push the Django image to Docker Hub
docker push yourdockerhubusername/django-app:latest

7. GitHub Repository & Docker Hub

Make sure to:
- Push all your code to your public GitHub repository.
- Push the Docker images to your Docker Hub account.
- Include the links to both your GitHub repository and Docker Hub in the assignment3_results sheet.

8. Important Files

The following files are essential for the setup:
- Dockerfile (for both Flask and Django applications)
- docker-compose.yml (to manage the containers)
- requirements.txt (for both Flask and Django applications)
- app.py (Flask application code)
- manage.py (Django application code)

9. README File

This README file explains the project setup and instructions on running the web applications with Docker Compose.
Ensure that all dependencies are installed and containers are correctly configured for smooth execution.

Conclusion

This project demonstrates how to build basic web applications with Flask and Django and containerize them using Docker.
By following the steps above, you should be able to deploy both applications and manage them using Docker Compose, making the setup and deployment process streamlined and consistent across environments.
