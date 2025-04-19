# Step 1: Use an official Python runtime as a parent image
FROM python:3.12-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Step 4: Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container
COPY . /app/

# Step 6: Expose the port that Django will run on
EXPOSE 8000

# Step 7: Set environment variables
ENV PYTHONUNBUFFERED 1

# Step 8: Run Django migrations and start the server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
